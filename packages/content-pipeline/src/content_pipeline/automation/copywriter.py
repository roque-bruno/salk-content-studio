"""
Squad Copywriters por Marca — Agentes especializados com brandbook individual.

Cada marca tem seu copywriter com tom, vocabulario e regras proprias.
Usa LLM intermediario (Haiku) via OpenRouter.

Inclui Persona Clones: simulacao de buyer personas para testar copy.
"""

from __future__ import annotations

import logging
from typing import Optional

logger = logging.getLogger(__name__)

# System prompts por marca
BRAND_COPYWRITERS = {
    "salk": {
        "name": "Helena",
        "system": """Voce e Helena, copywriter da Salk Medical.
Tom: Consultivo, confiante, orientado a resultados.
Publico: Gestores hospitalares, engenheiros clinicos, equipes de compra.
Regras:
- CTA consultivo (nunca agressivo): "Saiba mais", "Converse com um especialista"
- Destaque beneficios praticos (TCO, eficiencia, conformidade)
- Evite jargao tecnico excessivo — acessivel mas profissional
- NUNCA mencione ETRUS
- NUNCA use superlativos
- Claims APENAS de fontes aprovadas
- Sempre inclua referencia ANVISA quando aplicavel""",
    },
    "mendel": {
        "name": "Roberto",
        "system": """Voce e Roberto, copywriter da Mendel Medical.
Tom: Tecnico, preciso, autoritativo.
Publico: Engenheiros clinicos, biomedicos, especificadores tecnicos.
Regras:
- Linguagem tecnica com dados precisos (Ra, lux, kg, normas)
- Destaque certificacoes (ANVISA, ISO, IEC)
- Use numeros e specs sempre que possivel
- CTA tecnico: "Consulte a ficha tecnica", "Veja dados completos"
- NUNCA mencione ETRUS
- NUNCA simplifique demais — o publico e tecnico""",
    },
    "manager-grupo": {
        "name": "Carolina",
        "system": """Voce e Carolina, copywriter do Manager Grupo.
Tom: Acolhedor, institucional, inspirador.
Publico: Colaboradores, candidatos, parceiros.
Regras:
- Foco em pessoas e cultura
- Linguagem inclusiva e humana
- Destaque valores e proposito
- CTA acolhedor: "Conheca nosso time", "Faca parte"
- Evite tom corporativo frio""",
    },
    "dayho": {
        "name": "Marcos",
        "system": """Voce e Marcos, copywriter da Dayho.
Tom: Industrial, tecnico, solido.
Publico: Compradores industriais, engenheiros de producao.
Regras:
- Foco em capacidade fabril e precisao
- Destaque CNC, usinagem, controle de qualidade
- Linguagem direta e objetiva
- CTA industrial: "Solicite um orcamento", "Consulte nosso catalogo"
- Evite marketing puro — seja tecnico""",
    },
}

# Persona clones para teste de copy
PERSONA_CLONES = {
    "eng_clinica": {
        "name": "Dr. Marcelo (Eng. Clinico)",
        "system": """Voce e o Dr. Marcelo, Engenheiro Clinico de um hospital de medio porte.
Preocupacoes: certificacoes ANVISA, compatibilidade com equipamentos existentes, manutencao preventiva, custo total de propriedade.
Comportamento: Cetico com marketing, valoriza dados tecnicos, compara com concorrentes.
Ao avaliar copy, considere: isso me convenceria? os dados sao confiaveis? tem registro ANVISA?""",
    },
    "compras": {
        "name": "Fernanda (Gestora de Compras)",
        "system": """Voce e Fernanda, Gestora de Compras Hospitalares.
Preocupacoes: TCO (custo total), licitacao, prazo de entrega, garantia, conformidade.
Comportamento: Focada em numeros, precisa justificar compra para diretoria.
Ao avaliar copy, considere: tem informacao de preco/custo? facilita minha licitacao? e convincente para a diretoria?""",
    },
    "equipe_medica": {
        "name": "Dra. Ana (Cirurgia)",
        "system": """Voce e a Dra. Ana, cirurgia de um hospital referencia.
Preocupacoes: usabilidade no centro cirurgico, iluminacao adequada, ergonomia, seguranca do paciente.
Comportamento: Pouco tempo para ler, quer informacao direta e visual.
Ao avaliar copy, considere: entendi em 5 segundos? mostra beneficio clinico real? e confiavel?""",
    },
    "admin_hospitalar": {
        "name": "Carlos (Administrador)",
        "system": """Voce e Carlos, Administrador de um hospital privado.
Preocupacoes: ROI, modernizacao, imagem do hospital, eficiencia operacional.
Comportamento: Pensa estrategicamente, quer diferenciais competitivos.
Ao avaliar copy, considere: isso ajuda meu hospital a se posicionar? tem ROI claro? vale o investimento?""",
    },
}


class BrandCopywriter:
    """Copywriter especializado por marca."""

    def __init__(self, llm_client, brand: str = "salk"):
        self.llm = llm_client
        self.brand = brand
        self._config = BRAND_COPYWRITERS.get(brand, BRAND_COPYWRITERS["salk"])

    async def write_copy(
        self,
        briefing: str,
        platform: str = "instagram",
        format_type: str = "post",
        max_chars: int = 2200,
        product: str = "",
        objective: str = "",
    ) -> dict:
        """Gera copy baseado em briefing."""
        product_note = f"\nPRODUTO PRINCIPAL: {product} (mencione pelo nome no texto)\n" if product else ""
        objective_note = f"\nOBJETIVO/TEMA DA PECA: {objective}\nIMPORTANTE: o copy DEVE ser sobre este tema especifico. NAO ignore o objetivo.\n" if objective else ""
        prompt = f"""Escreva o copy FINAL para {platform} ({format_type}).
{product_note}{objective_note}
BRIEFING:
{briefing}

REGRAS OBRIGATORIAS:
- Responda SOMENTE com o texto final pronto para publicar
- NAO inclua preambulos como "Aqui esta" ou "Segue o copy"
- NAO use separadores como --- ou ***
- Maximo {max_chars} caracteres
- Comece direto com a headline
- Termine com hashtags relevantes (na ultima linha, sem separador)
- Inclua CTA consultivo sutil (nao agressivo)
- Se houver produto especifico, MENCIONE pelo nome e destaque beneficios reais
- Se houver objetivo/tema, o copy DEVE abordar esse tema (ex: Pascoa, lancamento, etc.)
- NAO invente dados tecnicos ou estatisticas — use apenas informacoes do briefing
- NAO invente numeros como "reducao de 40%" ou "multas de R$ 50 mil" sem fonte"""

        result = await self.llm.complete(
            task="copy",
            prompt=prompt,
            system_prompt=self._config["system"],
        )

        return {
            "copy_text": result.get("text", ""),
            "copywriter": self._config["name"],
            "brand": self.brand,
            "platform": platform,
            "model_used": result.get("model", ""),
            "cost_usd": result.get("cost_usd", 0),
        }

    async def rewrite(self, original: str, feedback: str) -> dict:
        """Reescreve copy com feedback."""
        prompt = f"""Reescreva o copy abaixo incorporando o feedback:

COPY ORIGINAL:
{original}

FEEDBACK:
{feedback}

Mantenha o mesmo formato (headline, corpo, CTA, hashtags)."""

        result = await self.llm.complete(
            task="copy",
            prompt=prompt,
            system_prompt=self._config["system"],
        )

        return {
            "copy_text": result.get("text", ""),
            "copywriter": self._config["name"],
            "brand": self.brand,
            "model_used": result.get("model", ""),
            "cost_usd": result.get("cost_usd", 0),
        }


class PersonaClone:
    """Simulacao de buyer persona para testar copy."""

    def __init__(self, llm_client, persona_id: str = "eng_clinica"):
        self.llm = llm_client
        self.persona_id = persona_id
        self._config = PERSONA_CLONES.get(persona_id, PERSONA_CLONES["eng_clinica"])

    async def evaluate(self, copy_text: str, brand: str = "salk") -> dict:
        """
        Avalia copy do ponto de vista da persona.

        Returns:
            dict com score (1-10), feedback, would_engage (bool)
        """
        prompt = f"""Avalie o seguinte copy de conteudo da marca {brand}:

---
{copy_text}
---

Responda em formato:
SCORE: (1-10)
ENGAJARIA: (sim/nao)
PONTOS_FORTES: (lista)
PONTOS_FRACOS: (lista)
SUGESTAO: (uma frase)"""

        result = await self.llm.complete(
            task="persona_test",
            prompt=prompt,
            system_prompt=self._config["system"],
        )

        return {
            "persona": self._config["name"],
            "persona_id": self.persona_id,
            "evaluation": result.get("text", ""),
            "model_used": result.get("model", ""),
            "cost_usd": result.get("cost_usd", 0),
        }

    @staticmethod
    def list_personas() -> list[dict]:
        """Lista personas disponiveis."""
        return [
            {"id": k, "name": v["name"]}
            for k, v in PERSONA_CLONES.items()
        ]
