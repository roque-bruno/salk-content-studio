"""
Auto-Briefing (Atlas) — Gera briefing automatico por slot do calendario.

Recebe: slot do calendario (dia, plataforma, pilar, marca, persona)
Produz: briefing completo com objetivo, mensagem-chave, CTA, tom, formato

Usa LLM barato (Flash) via OpenRouter para gerar.
"""

from __future__ import annotations

import logging
from typing import Optional

logger = logging.getLogger(__name__)

BRIEFING_SYSTEM_PROMPT = """Voce e Atlas, o estrategista de conteudo do Manager Grupo.
Sua funcao e criar briefings de conteudo para redes sociais B2B healthcare.

REGRAS INEGOCIAVEIS:
- ETRUS esta BLOQUEADO — nunca mencionar
- NUNCA prometer resultados medicos
- NUNCA usar superlativos (o melhor, o unico)
- Claims so de fontes aprovadas
- Tom deve seguir o brandbook da marca

Formato de saida (YAML):
```yaml
objetivo: "string"
mensagem_chave: "string"
cta: "string"
tom: "string"
formato_visual: "string"
hashtags_sugeridas: ["string"]
claims_sugeridos: ["string"]
notas_visuais: "string"
```"""


class AutoBriefing:
    """Gera briefings automaticos para slots do calendario."""

    def __init__(self, llm_client, brandbooks_loader=None, claims_loader=None):
        self.llm = llm_client
        self._load_brandbook = brandbooks_loader
        self._load_claims = claims_loader

    async def generate(
        self,
        brand: str,
        platform: str,
        pillar: str,
        product: str = "",
        persona: str = "",
        day: str = "",
        context: str = "",
    ) -> dict:
        """
        Gera briefing para um slot do calendario.

        Returns:
            dict com briefing completo + metadados LLM
        """
        # Carregar contexto do brandbook
        brand_context = ""
        if self._load_brandbook:
            bb = self._load_brandbook(brand)
            if bb:
                brand_context = f"""
Marca: {bb.get('full_name', brand)}
Tom: {bb.get('tone_of_voice', {}).get('primary', '')}
Foco: {bb.get('focus', '')}
"""

        prompt = f"""Crie um briefing de conteudo para:
- Marca: {brand}
- Plataforma: {platform}
- Pilar: {pillar}
- Produto: {product or 'institucional'}
- Persona-alvo: {persona or 'geral'}
- Dia: {day}
{f'- Contexto adicional: {context}' if context else ''}

{brand_context}

Gere o briefing completo no formato YAML especificado."""

        result = await self.llm.complete(
            task="briefing",
            prompt=prompt,
            system_prompt=BRIEFING_SYSTEM_PROMPT,
        )

        return {
            "briefing_text": result.get("text", ""),
            "brand": brand,
            "platform": platform,
            "pillar": pillar,
            "product": product,
            "persona": persona,
            "model_used": result.get("model", ""),
            "cost_usd": result.get("cost_usd", 0),
            "preview_mode": result.get("preview_mode", False),
        }

    async def generate_batch(self, slots: list[dict]) -> list[dict]:
        """Gera briefings para multiplos slots."""
        results = []
        for slot in slots:
            r = await self.generate(
                brand=slot.get("brand", "salk"),
                platform=slot.get("platform", "instagram"),
                pillar=slot.get("pillar", "produto"),
                product=slot.get("product", ""),
                persona=slot.get("persona_target", ""),
                day=slot.get("day", ""),
            )
            results.append(r)
        return results
