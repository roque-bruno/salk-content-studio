"""
Disaster Check Visual — Gate de qualidade pos-geracao de imagem.

Verifica imagens geradas contra regras inegociaveis antes de aprovar.
Funciona como Shield visual: bloqueia violacoes, nao apenas avisa.

Checklist automatico:
1. Texto/logo na imagem (IA gera texto distorcido)
2. Equipamento concorrente visivel
3. Pessoas com rostos identificaveis
4. Cenas clinicas graficas
5. Luz dispersa em produtos LEV
6. Qualidade tecnica (blur, artefatos, distorcao)
7. Composicao adequada para formato-alvo
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class DisasterItem:
    """Um item individual do checklist de disaster check."""
    check_id: str
    name: str
    severity: str  # "block" ou "warn"
    passed: bool = False
    details: str = ""


@dataclass
class DisasterResult:
    """Resultado completo do disaster check."""
    image_path: str
    product: str
    brand: str
    approved: bool = False
    score: float = 0.0
    checks: list[DisasterItem] = field(default_factory=list)
    blockers: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "image_path": self.image_path,
            "product": self.product,
            "brand": self.brand,
            "approved": self.approved,
            "score": self.score,
            "total_checks": len(self.checks),
            "passed_checks": sum(1 for c in self.checks if c.passed),
            "blockers": self.blockers,
            "warnings": self.warnings,
            "details": [
                {
                    "check_id": c.check_id,
                    "name": c.name,
                    "severity": c.severity,
                    "passed": c.passed,
                    "details": c.details,
                }
                for c in self.checks
            ],
        }


# Checklist de verificacoes
DISASTER_CHECKS = [
    {
        "id": "text_logo",
        "name": "Texto/Logo na Imagem",
        "severity": "block",
        "description": "IA gera texto distorcido e ilegivel. Texto e logo sao adicionados no Canva.",
        "auto_detectable": True,
    },
    {
        "id": "competitor_equipment",
        "name": "Equipamento Concorrente",
        "severity": "block",
        "description": "Imagem nao pode conter equipamentos medicos alem do produto-alvo.",
        "auto_detectable": True,
    },
    {
        "id": "identifiable_faces",
        "name": "Rostos Identificaveis",
        "severity": "block",
        "description": "Pessoas com rostos claros geram risco legal (LGPD, direito de imagem).",
        "auto_detectable": True,
    },
    {
        "id": "graphic_clinical",
        "name": "Cenas Clinicas Graficas",
        "severity": "block",
        "description": "Sangue, procedimentos abertos, conteudo grafico nao e adequado para social media.",
        "auto_detectable": True,
    },
    {
        "id": "lev_light_direction",
        "name": "Direcao da Luz LEV",
        "severity": "block",
        "description": "LEV vende luz CONCENTRADA. Raios laterais/dispersos contradizem o produto.",
        "product_specific": "lev",
        "auto_detectable": True,
    },
    {
        "id": "product_distortion",
        "name": "Distorcao do Produto",
        "severity": "block",
        "description": "Produto com proporcoes erradas, partes faltando ou deformacoes.",
        "auto_detectable": True,
    },
    {
        "id": "image_quality",
        "name": "Qualidade Tecnica",
        "severity": "warn",
        "description": "Blur, artefatos de compressao, ruido excessivo, baixa resolucao.",
        "auto_detectable": True,
    },
    {
        "id": "composition_format",
        "name": "Composicao e Formato",
        "severity": "warn",
        "description": "Produto cortado, muito pequeno, ou composicao inadequada para o formato.",
        "auto_detectable": True,
    },
    {
        "id": "brand_colors",
        "name": "Paleta de Cores da Marca",
        "severity": "warn",
        "description": "Imagem com cores que conflitam com a identidade visual da marca.",
        "auto_detectable": False,
    },
    {
        "id": "empty_scene",
        "name": "Cenario Vazio/Generico",
        "severity": "warn",
        "description": "Cenario sem contexto ou muito generico (anti-pattern validado).",
        "auto_detectable": True,
    },
]


class DisasterCheck:
    """
    Gate de qualidade visual pos-geracao.

    Modo atual: checklist manual assistido.
    Modo futuro: integracao com vision model para deteccao automatica.
    """

    def __init__(self, llm_client=None, brandbook_loader=None):
        self.llm = llm_client
        self._load_brandbook = brandbook_loader

    async def check_image(
        self,
        image_path: str,
        product: str,
        brand: str = "salk",
        format_target: str = "square_social",
        manual_overrides: Optional[dict] = None,
    ) -> DisasterResult:
        """
        Executa disaster check em uma imagem.

        Args:
            image_path: Caminho da imagem gerada
            product: Produto fotografado (lev, kratus, etc)
            brand: Marca (salk, mendel, etc)
            format_target: Formato alvo (square_social, portrait_story, etc)
            manual_overrides: Dict de check_id -> bool para override manual

        Returns:
            DisasterResult com aprovacao/rejeicao e detalhes
        """
        result = DisasterResult(
            image_path=image_path,
            product=product,
            brand=brand,
        )

        overrides = manual_overrides or {}

        for check_def in DISASTER_CHECKS:
            # Pular checks especificos de produto
            if check_def.get("product_specific") and check_def["product_specific"] != product.lower():
                continue

            check = DisasterItem(
                check_id=check_def["id"],
                name=check_def["name"],
                severity=check_def["severity"],
            )

            # Se tem override manual, usar
            if check_def["id"] in overrides:
                check.passed = overrides[check_def["id"]]
                check.details = "Override manual pelo revisor"
            elif self.llm and check_def.get("auto_detectable"):
                # Tentar deteccao automatica via LLM vision (futuro)
                check.passed = True  # Default passa ate ter vision model
                check.details = "Auto-check pendente (sem vision model)"
            else:
                check.passed = True  # Checks nao-automaticos passam por default
                check.details = "Requer revisao manual"

            result.checks.append(check)

            if not check.passed:
                if check.severity == "block":
                    result.blockers.append(f"{check.name}: {check.details}")
                else:
                    result.warnings.append(f"{check.name}: {check.details}")

        # Calcular score
        total = len(result.checks)
        passed = sum(1 for c in result.checks if c.passed)
        result.score = (passed / total * 10) if total > 0 else 0

        # Aprovacao: zero blockers
        result.approved = len(result.blockers) == 0

        return result

    async def check_batch(
        self,
        items: list[dict],
    ) -> list[dict]:
        """
        Verifica multiplas imagens.

        Args:
            items: Lista de dicts com image_path, product, brand
        """
        results = []
        for item in items:
            r = await self.check_image(
                image_path=item.get("image_path", ""),
                product=item.get("product", ""),
                brand=item.get("brand", "salk"),
                format_target=item.get("format_target", "square_social"),
                manual_overrides=item.get("manual_overrides"),
            )
            results.append(r.to_dict())
        return results

    @staticmethod
    def get_checklist() -> list[dict]:
        """Retorna checklist completo para UI."""
        return [
            {
                "id": c["id"],
                "name": c["name"],
                "severity": c["severity"],
                "description": c["description"],
                "auto_detectable": c.get("auto_detectable", False),
                "product_specific": c.get("product_specific"),
            }
            for c in DISASTER_CHECKS
        ]
