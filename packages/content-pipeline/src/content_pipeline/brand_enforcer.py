"""
Brand Enforcer — Design System como Cabresto.

Valida conteudo contra brandbook YAML da marca.
Cada violacao BLOQUEIA — nao e sugestao, e constraint.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import yaml


@dataclass
class BrandViolation:
    """Uma violacao detectada contra o brandbook."""
    rule: str
    severity: str  # BLOQUEANTE | ALTA | MEDIA
    detail: str
    suggestion: str = ""


@dataclass
class BrandCheckResult:
    """Resultado da validacao de marca."""
    brand: str
    passed: bool
    violations: list[BrandViolation] = field(default_factory=list)
    warnings: list[BrandViolation] = field(default_factory=list)

    @property
    def blocker_count(self) -> int:
        return sum(1 for v in self.violations if v.severity == "BLOQUEANTE")

    def to_dict(self) -> dict:
        return {
            "brand": self.brand,
            "passed": self.passed,
            "blocker_count": self.blocker_count,
            "violations": [
                {"rule": v.rule, "severity": v.severity, "detail": v.detail, "suggestion": v.suggestion}
                for v in self.violations
            ],
            "warnings": [
                {"rule": v.rule, "severity": v.severity, "detail": v.detail, "suggestion": v.suggestion}
                for v in self.warnings
            ],
        }


class BrandEnforcer:
    """Valida conteudo contra brandbook YAML."""

    def __init__(self, brandbooks_dir: Path) -> None:
        self._dir = brandbooks_dir
        self._cache: dict[str, dict] = {}

    def _load(self, brand: str) -> Optional[dict]:
        if brand in self._cache:
            return self._cache[brand]
        path = self._dir / f"{brand}.yaml"
        if not path.exists():
            return None
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        self._cache[brand] = data
        return data

    def validate(self, text: str, brand: str, context: str = "copy") -> BrandCheckResult:
        """
        Valida texto contra brandbook da marca.

        Args:
            text: Conteudo a validar (copy, prompt, headline, etc.)
            brand: Slug da marca (salk, mendel, manager-grupo, dayho)
            context: Tipo de conteudo (copy, prompt, headline)

        Returns:
            BrandCheckResult com violacoes e warnings
        """
        bb = self._load(brand)
        if bb is None:
            return BrandCheckResult(brand=brand, passed=True)

        violations: list[BrandViolation] = []
        warnings: list[BrandViolation] = []
        text_lower = text.lower()

        # 1. Termos proibidos do brandbook
        self._check_prohibited_terms(text_lower, bb, violations)

        # 2. Tom de voz proibido
        self._check_tone_violations(text_lower, bb, violations, warnings)

        # 3. Regras visuais (para prompts NB2)
        if context == "prompt":
            self._check_visual_rules(text_lower, bb, brand, violations)

        # 4. Produtos bloqueados
        self._check_blocked_products(text_lower, bb, violations)

        # 5. Regras especificas de produto
        self._check_product_specific_rules(text_lower, bb, brand, violations, warnings)

        passed = len(violations) == 0
        return BrandCheckResult(
            brand=brand,
            passed=passed,
            violations=violations,
            warnings=warnings,
        )

    def get_prompt_constraints(self, brand: str) -> str:
        """Retorna constraints do brandbook formatados para injetar em prompts NB2."""
        bb = self._load(brand)
        if bb is None:
            return ""

        constraints: list[str] = []
        visual = bb.get("visual_rules", {})

        for key, rule in visual.items():
            if isinstance(rule, str) and "NUNCA" in rule:
                constraints.append(f"CONSTRAINT: {rule}")

        # Regras especificas de produtos
        for product in bb.get("products", []):
            for rule in product.get("special_rules", []):
                constraints.append(f"PRODUCT {product['name']}: {rule}")

        return "\n".join(constraints)

    # ------------------------------------------------------------------
    # Checks individuais
    # ------------------------------------------------------------------

    def _check_prohibited_terms(
        self, text: str, bb: dict, violations: list[BrandViolation]
    ) -> None:
        for term in bb.get("prohibited_terms", []):
            term_lower = term.lower()
            if term_lower in text:
                violations.append(BrandViolation(
                    rule="prohibited_term",
                    severity="BLOQUEANTE",
                    detail=f"Termo proibido detectado: '{term}'",
                    suggestion=f"Remover '{term}' do texto",
                ))

    def _check_tone_violations(
        self, text: str, bb: dict, violations: list[BrandViolation],
        warnings: list[BrandViolation]
    ) -> None:
        tone = bb.get("tone_of_voice", {})
        prohibited_tones = [t.lower() for t in tone.get("prohibited", [])]

        # Detectar tons proibidos via keywords associados
        tone_keywords = {
            "agressivo": ["compre agora", "ultima chance", "nao perca", "urgente", "imperdivel"],
            "vendedor": ["promocao", "desconto", "oferta", "gratis", "barato"],
            "arrogante": ["somos os melhores", "ninguem faz igual", "incomparavel"],
            "superficial": ["incrivel", "maravilhoso", "fantastico", "espetacular"],
            "informal": ["galera", "fala pessoal", "e ai", "top demais"],
            "hype": ["revolucionario", "disruptivo", "game changer", "nunca visto"],
            "corporativo frio": [],  # dificil detectar automaticamente
            "generico": [],
            "tecnico demais": [],
            "marketing puro": [],
        }

        for prohibited_tone in prohibited_tones:
            keywords = tone_keywords.get(prohibited_tone, [])
            for kw in keywords:
                if kw in text:
                    warnings.append(BrandViolation(
                        rule="tone_violation",
                        severity="ALTA",
                        detail=f"Tom '{prohibited_tone}' detectado (keyword: '{kw}')",
                        suggestion=f"Ajustar tom para: {tone.get('primary', '')}",
                    ))

    def _check_visual_rules(
        self, text: str, bb: dict, brand: str, violations: list[BrandViolation]
    ) -> None:
        visual = bb.get("visual_rules", {})

        # Pessoas geradas por IA
        people_keywords = ["person", "people", "doctor", "nurse", "medico", "enfermeiro",
                          "paciente", "patient", "human", "man", "woman", "face", "portrait"]
        for kw in people_keywords:
            if kw in text:
                violations.append(BrandViolation(
                    rule="no_ai_people",
                    severity="BLOQUEANTE",
                    detail=f"Prompt pode gerar pessoa via IA (keyword: '{kw}')",
                    suggestion="Remover referencia a pessoas. NB2 = apenas cenario + produto.",
                ))
                break  # Uma violacao basta

        # Cenas clinicas
        clinical_keywords = ["surgery", "cirurgia", "operating room", "sala cirurgica",
                           "hospital room", "paciente na cama", "clinical scene"]
        for kw in clinical_keywords:
            if kw in text:
                violations.append(BrandViolation(
                    rule="no_ai_clinical",
                    severity="BLOQUEANTE",
                    detail=f"Prompt pode gerar cena clinica via IA (keyword: '{kw}')",
                    suggestion="Descrever apenas cenario/ambiente. Sem cenas clinicas geradas.",
                ))
                break

        # Texto/logo no prompt
        text_logo_keywords = ["text saying", "logo", "brand name", "escrito", "lettering",
                            "typography", "label", "texto"]
        for kw in text_logo_keywords:
            if kw in text:
                violations.append(BrandViolation(
                    rule="no_ai_text_logo",
                    severity="BLOQUEANTE",
                    detail=f"Prompt pede texto/logo via IA (keyword: '{kw}')",
                    suggestion="NUNCA gerar texto/logo via IA. Adicionar no Canva.",
                ))
                break

        # Equipamento concorrente
        competitor_keywords = ["medical equipment", "surgical light", "operating table",
                             "equipamento medico", "foco cirurgico", "mesa cirurgica"]
        # Só aplica se o prompt NÃO menciona o produto especifico
        products = [p.get("name", "").lower() for p in bb.get("products", [])
                   if p.get("status") == "ATIVO"]
        has_own_product = any(p in text for p in products)
        if not has_own_product:
            for kw in competitor_keywords:
                if kw in text:
                    violations.append(BrandViolation(
                        rule="no_competitor_equipment",
                        severity="BLOQUEANTE",
                        detail=f"Prompt pode gerar equipamento concorrente (keyword: '{kw}')",
                        suggestion="Descrever APENAS cenario. O produto real vem do PNG de referencia.",
                    ))
                    break

    def _check_blocked_products(
        self, text: str, bb: dict, violations: list[BrandViolation]
    ) -> None:
        for product in bb.get("products", []):
            if product.get("status") == "BLOQUEADO":
                name = product.get("name", "").lower()
                if name and name in text:
                    violations.append(BrandViolation(
                        rule="blocked_product",
                        severity="BLOQUEANTE",
                        detail=f"Produto BLOQUEADO mencionado: '{product['name']}'",
                        suggestion=f"Remover '{product['name']}'. Status: {product.get('status')}. "
                                  + " | ".join(product.get("special_rules", [])),
                    ))

    def _check_product_specific_rules(
        self, text: str, bb: dict, brand: str,
        violations: list[BrandViolation], warnings: list[BrandViolation]
    ) -> None:
        # Regra LEV especifica
        if brand == "salk" and "lev" in text:
            dispersion_keywords = ["glow", "rays", "spreading", "dispersa", "lateral",
                                  "scattered", "radiant", "beam spread", "light spread"]
            for kw in dispersion_keywords:
                if kw in text:
                    violations.append(BrandViolation(
                        rule="lev_light_direction",
                        severity="BLOQUEANTE",
                        detail=f"LEV: luz deve ser FOCADA para baixo, mas prompt sugere dispersao ('{kw}')",
                        suggestion="LEV = luz CONCENTRADA no campo cirurgico. Sem glow, rays ou dispersao.",
                    ))
                    break

        # Regra logo Mendel vs Salk
        logo = bb.get("logo_usage", {})
        if logo.get("decision_rule"):
            # Info para warnings
            warnings.append(BrandViolation(
                rule="logo_decision",
                severity="MEDIA",
                detail=f"Regra de logo: {logo['decision_rule']}",
                suggestion=logo.get("rule", ""),
            ))
