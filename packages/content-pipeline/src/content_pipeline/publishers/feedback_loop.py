"""
Feedback Loop — Performance informa briefings futuros.

Analisa metricas de engajamento e ajusta parametros do pipeline:
- Quais pilares performam melhor por marca
- Quais formatos geram mais engajamento
- Quais horarios tem melhor alcance
- Quais personas respondem melhor

Alimenta o Auto-Briefing com dados historicos para melhorar
a qualidade das proximas geracoes.
"""

from __future__ import annotations

import logging
from collections import defaultdict
from typing import Optional

logger = logging.getLogger(__name__)


class FeedbackLoop:
    """Analisa performance e alimenta o pipeline com insights."""

    def __init__(self, db=None, journey_log=None):
        self.db = db
        self.journey_log = journey_log

    def analyze_performance(self, brand: str = "") -> dict:
        """
        Analisa performance geral e gera insights acionaveis.

        Returns:
            dict com insights por pilar, formato, horario, persona
        """
        if self.db is None:
            return {"error": "Database nao configurado"}

        metrics = self.db.list_metrics()
        pieces = self.db.list_pieces(brand=brand)

        if not metrics:
            return {
                "status": "insufficient_data",
                "message": "Sem metricas suficientes para analise. Publique e colete metricas primeiro.",
                "insights": [],
            }

        # Mapear metricas para pecas
        piece_map = {p.get("id", ""): p for p in pieces}
        enriched = []
        for m in metrics:
            piece = piece_map.get(m.get("piece_id", ""), {})
            enriched.append({
                **m,
                "pillar": piece.get("pillar", "unknown"),
                "format": piece.get("format", "unknown"),
                "platform": m.get("platform", piece.get("platform", "unknown")),
                "persona_target": piece.get("persona_target", "unknown"),
                "brand": piece.get("brand", brand or "unknown"),
            })

        insights = []

        # Insight 1: Melhor pilar por engajamento
        by_pillar = defaultdict(list)
        for e in enriched:
            by_pillar[e["pillar"]].append(e.get("engagement", 0))

        pillar_avg = {
            k: round(sum(v) / len(v), 1) if v else 0
            for k, v in by_pillar.items()
        }
        if pillar_avg:
            best_pillar = max(pillar_avg, key=pillar_avg.get)
            insights.append({
                "type": "pillar",
                "insight": f"Pilar '{best_pillar}' tem o melhor engajamento medio ({pillar_avg[best_pillar]})",
                "recommendation": f"Priorizar conteudo do pilar '{best_pillar}' na proxima semana",
                "data": pillar_avg,
            })

        # Insight 2: Melhor formato
        by_format = defaultdict(list)
        for e in enriched:
            by_format[e["format"]].append(e.get("engagement", 0))

        format_avg = {
            k: round(sum(v) / len(v), 1) if v else 0
            for k, v in by_format.items()
        }
        if format_avg:
            best_format = max(format_avg, key=format_avg.get)
            insights.append({
                "type": "format",
                "insight": f"Formato '{best_format}' gera mais engajamento ({format_avg[best_format]})",
                "recommendation": f"Aumentar producao de '{best_format}'",
                "data": format_avg,
            })

        # Insight 3: Melhor plataforma
        by_platform = defaultdict(list)
        for e in enriched:
            by_platform[e["platform"]].append(e.get("engagement", 0))

        platform_avg = {
            k: round(sum(v) / len(v), 1) if v else 0
            for k, v in by_platform.items()
        }
        if platform_avg:
            best_platform = max(platform_avg, key=platform_avg.get)
            insights.append({
                "type": "platform",
                "insight": f"Plataforma '{best_platform}' tem melhor engajamento",
                "recommendation": f"Concentrar esforcos em '{best_platform}'",
                "data": platform_avg,
            })

        # Insight 4: Engagement rate medio
        total_engagement = sum(e.get("engagement", 0) for e in enriched)
        total_reach = sum(e.get("reach", 0) for e in enriched)
        avg_rate = round((total_engagement / total_reach * 100) if total_reach > 0 else 0, 2)

        insights.append({
            "type": "engagement_rate",
            "insight": f"Taxa de engajamento media: {avg_rate}%",
            "recommendation": (
                "Acima de 3% e excelente para B2B healthcare"
                if avg_rate >= 3
                else "Abaixo de 3% — considere ajustar copy e visuais"
            ),
            "data": {"avg_rate": avg_rate, "total_posts": len(enriched)},
        })

        return {
            "status": "analyzed",
            "total_posts_analyzed": len(enriched),
            "insights": insights,
            "by_pillar": pillar_avg,
            "by_format": format_avg,
            "by_platform": platform_avg,
        }

    def get_briefing_recommendations(self, brand: str = "salk") -> dict:
        """
        Gera recomendacoes para o proximo ciclo de briefings
        baseado em dados historicos.
        """
        analysis = self.analyze_performance(brand=brand)

        if analysis.get("status") == "insufficient_data":
            return {
                "brand": brand,
                "recommendations": [
                    "Usar distribuicao padrao de pilares do editorial template",
                    "Testar todos os formatos disponíveis",
                    "Manter horarios sugeridos pelo platform-specs",
                ],
                "data_driven": False,
            }

        recommendations = []

        for insight in analysis.get("insights", []):
            if insight.get("recommendation"):
                recommendations.append(insight["recommendation"])

        # Adicionar insights do journey log se disponivel
        if self.journey_log:
            stats = self.journey_log.get_stats()
            by_phase = stats.get("by_phase", {})
            for phase, data in by_phase.items():
                success_rate = data.get("success_rate", 100)
                if success_rate < 80:
                    recommendations.append(
                        f"Fase '{phase}' tem taxa de sucesso de {success_rate}% — revisar processo"
                    )

        return {
            "brand": brand,
            "recommendations": recommendations,
            "data_driven": True,
            "analysis_summary": {
                "best_pillar": analysis.get("by_pillar", {}),
                "best_format": analysis.get("by_format", {}),
                "best_platform": analysis.get("by_platform", {}),
            },
        }
