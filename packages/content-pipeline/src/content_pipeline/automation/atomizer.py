"""
Atomizacao Semantica (Nova) — Master content → derivatives com logica semantica.

A partir de uma peca master (ex: carrossel Instagram), gera derivativos
adaptados para outros formatos e plataformas, mantendo a essencia.

Fluxos de atomizacao:
- Carrossel → Stories, Reels script, LinkedIn post, Email snippet
- Post unico → Story, Tweet thread, LinkedIn article intro
- Video longo → Clips curtos, GIF, Thumbnail, Caption

Regras:
- Cada derivativo e adaptado ao formato (nao apenas cortado)
- Tom ajustado por plataforma (LinkedIn mais formal, Stories mais casual)
- CTAs adaptados por plataforma
- Hashtags especificas por plataforma
- Limite de caracteres respeitado
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

import yaml

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Carregamento dinâmico de atomization-config.yaml
# ---------------------------------------------------------------------------
_ATOM_CONFIG_CACHE: Optional[dict] = None
_ATOM_DATA_DIR: Optional[Path] = None


def _load_atom_config() -> dict:
    global _ATOM_CONFIG_CACHE
    if _ATOM_CONFIG_CACHE is not None:
        return _ATOM_CONFIG_CACHE
    if _ATOM_DATA_DIR:
        path = _ATOM_DATA_DIR / "atomization-config.yaml"
        if path.exists():
            try:
                _ATOM_CONFIG_CACHE = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
                return _ATOM_CONFIG_CACHE
            except Exception as e:
                logger.warning("Falha ao carregar atomization-config.yaml: %s", e)
    _ATOM_CONFIG_CACHE = {}
    return _ATOM_CONFIG_CACHE


def init_atomization_config(data_dir: Path) -> None:
    """Inicializa data_dir para carregamento do YAML."""
    global _ATOM_DATA_DIR, _ATOM_CONFIG_CACHE
    _ATOM_DATA_DIR = data_dir
    _ATOM_CONFIG_CACHE = None


def get_platform_formats() -> dict:
    return _load_atom_config().get("platform_formats", {})


def get_atomization_map() -> dict:
    return _load_atom_config().get("atomization_map", {})


class SemanticAtomizer:
    """Atomizacao semantica de conteudo master em derivativos."""

    def __init__(self, llm_client=None):
        self.llm = llm_client

    async def atomize(
        self,
        master_content: str,
        master_type: str = "post_unico",
        brand: str = "salk",
        target_platforms: Optional[list[str]] = None,
        context: str = "",
    ) -> dict:
        """
        Atomiza conteudo master em derivativos.

        Args:
            master_content: Conteudo original (copy, briefing, etc)
            master_type: Tipo do master (carrossel, post_unico, video_longo, artigo)
            brand: Marca para manter tom consistente
            target_platforms: Plataformas alvo (ou auto via get_atomization_map())
            context: Contexto adicional (produto, campanha, etc)

        Returns:
            dict com derivativos gerados por plataforma
        """
        # Determinar plataformas alvo
        if target_platforms:
            platforms = target_platforms
        else:
            platforms = get_atomization_map().get(master_type, ["instagram_story", "linkedin_post"])

        derivatives = {}

        for platform in platforms:
            fmt = get_platform_formats().get(platform)
            if not fmt:
                logger.warning(f"Plataforma desconhecida: {platform}")
                continue

            if self.llm:
                derivative = await self._generate_with_llm(
                    master_content=master_content,
                    platform=platform,
                    fmt=fmt,
                    brand=brand,
                    context=context,
                )
            else:
                derivative = self._generate_basic(
                    master_content=master_content,
                    platform=platform,
                    fmt=fmt,
                )

            derivatives[platform] = derivative

        return {
            "master_type": master_type,
            "master_content": master_content[:200] + "..." if len(master_content) > 200 else master_content,
            "brand": brand,
            "derivatives_count": len(derivatives),
            "derivatives": derivatives,
        }

    async def _generate_with_llm(
        self,
        master_content: str,
        platform: str,
        fmt: dict,
        brand: str,
        context: str,
    ) -> dict:
        """Gera derivativo usando LLM."""
        system = f"""Voce e Nova, a especialista em atomizacao de conteudo do Manager Grupo.
Sua funcao e adaptar conteudo master para diferentes plataformas mantendo a essencia.

REGRAS:
- Adapte o TOM para a plataforma, nao apenas corte
- Respeite o limite de caracteres
- CTA deve ser nativo da plataforma
- Hashtags relevantes para o contexto
- Marca: {brand}
- NUNCA mencione ETRUS
- Mantenha a mensagem-chave do original"""

        prompt = f"""Adapte o conteudo abaixo para {platform}:

CONTEUDO MASTER:
{master_content}

{f'CONTEXTO: {context}' if context else ''}

RESTRICOES DA PLATAFORMA:
- Max caracteres: {fmt['max_chars']}
- Max hashtags: {fmt['hashtag_limit']}
- Tom: {fmt['tone_adjustment']}
- CTA style: {fmt['cta_style']}

Responda no formato:
COPY: (texto adaptado)
CTA: (call to action)
HASHTAGS: (lista separada por virgula)
NOTAS: (ajustes feitos)"""

        result = await self.llm.complete(
            task="copy",
            prompt=prompt,
            system_prompt=system,
        )

        return {
            "platform": platform,
            "content": result.get("text", ""),
            "max_chars": fmt["max_chars"],
            "tone": fmt["tone_adjustment"],
            "model_used": result.get("model", ""),
            "cost_usd": result.get("cost_usd", 0),
        }

    def _generate_basic(
        self,
        master_content: str,
        platform: str,
        fmt: dict,
    ) -> dict:
        """Gera derivativo basico sem LLM (truncamento inteligente)."""
        max_chars = fmt["max_chars"]

        # Truncamento inteligente: corta no ultimo ponto/paragrafo
        if len(master_content) <= max_chars:
            adapted = master_content
        else:
            truncated = master_content[:max_chars]
            last_period = truncated.rfind(".")
            last_newline = truncated.rfind("\n")
            cut_point = max(last_period, last_newline)
            if cut_point > max_chars * 0.5:
                adapted = truncated[:cut_point + 1]
            else:
                adapted = truncated.rstrip() + "..."

        return {
            "platform": platform,
            "content": adapted,
            "max_chars": max_chars,
            "tone": fmt["tone_adjustment"],
            "model_used": "basic_truncation",
            "cost_usd": 0,
        }

    async def suggest_derivatives(
        self,
        master_type: str,
    ) -> dict:
        """Sugere derivativos possiveis para um tipo de master."""
        platforms = get_atomization_map().get(master_type, [])
        suggestions = []
        for p in platforms:
            fmt = get_platform_formats().get(p, {})
            suggestions.append({
                "platform": p,
                "max_chars": fmt.get("max_chars", 0),
                "tone": fmt.get("tone_adjustment", ""),
                "cta_style": fmt.get("cta_style", ""),
            })

        return {
            "master_type": master_type,
            "available_derivatives": suggestions,
            "total": len(suggestions),
        }

    @staticmethod
    def list_master_types() -> list[str]:
        """Lista tipos de conteudo master disponiveis."""
        return list(get_atomization_map().keys())

    @staticmethod
    def list_platforms() -> list[dict]:
        """Lista plataformas e seus limites."""
        return [
            {"platform": k, **v}
            for k, v in get_platform_formats().items()
        ]
