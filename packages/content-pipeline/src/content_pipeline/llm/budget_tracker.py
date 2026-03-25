"""
Budget Tracker — Controle de gastos API em tempo real.

Registra custos de: NB2 (Gemini), Video (Kling), LLM (OpenRouter), TTS (ElevenLabs).
Limites mensais configuráveis. Alertas quando proximo do teto.

Teto mensal: R$ 1.974 (~$349 USD) conforme BUDGET-GERACAO-AI-IMAGEM-VIDEO.md
"""

from __future__ import annotations

import json
import logging
import sqlite3
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class BudgetLimits:
    """Limites mensais em USD."""
    nb2_images: float = 19.80       # 396 imgs x $0.05
    video_kling: float = 269.92     # 1928s x $0.14
    llm_openrouter: float = 30.00   # estimativa LLM
    tts_elevenlabs: float = 29.00   # ~482s narracao
    total: float = 349.00           # teto mensal USD


class BudgetTracker:
    """Rastreia gastos de API em tempo real com SQLite."""

    def __init__(self, db_path: Path, limits: Optional[BudgetLimits] = None) -> None:
        self.db_path = db_path
        self.limits = limits or BudgetLimits()
        self._init_db()

    def _get_conn(self) -> sqlite3.Connection:
        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._get_conn() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS api_costs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT NOT NULL,
                    cost_usd REAL NOT NULL,
                    metadata TEXT DEFAULT '{}',
                    recorded_at TEXT NOT NULL,
                    month TEXT NOT NULL
                )
            """)
            conn.execute("CREATE INDEX IF NOT EXISTS idx_costs_month ON api_costs(month)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_costs_category ON api_costs(category)")

    def record(self, category: str, cost_usd: float, metadata: Optional[dict] = None) -> dict:
        """
        Registra um gasto de API.

        Args:
            category: nb2, video, llm, tts
            cost_usd: Custo em USD
            metadata: Dados extras (model, task, etc.)

        Returns:
            dict com id, alert (se proximo do limite)
        """
        now = datetime.now()
        month = now.strftime("%Y-%m")

        with self._get_conn() as conn:
            cursor = conn.execute(
                """INSERT INTO api_costs (category, cost_usd, metadata, recorded_at, month)
                   VALUES (?, ?, ?, ?, ?)""",
                (category, cost_usd, json.dumps(metadata or {}), now.isoformat(), month),
            )
            record_id = cursor.lastrowid

        # Verificar alertas
        summary = self.get_month_summary(month)
        alert = self._check_alerts(summary)

        return {
            "id": record_id,
            "category": category,
            "cost_usd": round(cost_usd, 6),
            "month_total": summary["total_usd"],
            "alert": alert,
        }

    def get_month_summary(self, month: Optional[str] = None) -> dict:
        """Resumo de gastos do mes."""
        if month is None:
            month = datetime.now().strftime("%Y-%m")

        with self._get_conn() as conn:
            rows = conn.execute(
                """SELECT category, SUM(cost_usd) as total, COUNT(*) as count
                   FROM api_costs WHERE month = ? GROUP BY category""",
                (month,),
            ).fetchall()

        by_category: dict[str, dict] = {}
        total = 0.0
        for row in rows:
            d = dict(row)
            cat = d["category"]
            by_category[cat] = {
                "total_usd": round(d["total"], 4),
                "count": d["count"],
                "limit_usd": getattr(self.limits, cat, 0) if hasattr(self.limits, cat) else 0,
            }
            total += d["total"]

        # Adicionar categorias com zero
        for cat in ["nb2_images", "video_kling", "llm_openrouter", "tts_elevenlabs"]:
            if cat not in by_category:
                by_category[cat] = {
                    "total_usd": 0,
                    "count": 0,
                    "limit_usd": getattr(self.limits, cat, 0),
                }

        # Calcular percentual
        pct = round((total / self.limits.total * 100) if self.limits.total > 0 else 0, 1)

        return {
            "month": month,
            "total_usd": round(total, 4),
            "limit_usd": self.limits.total,
            "percentage_used": pct,
            "by_category": by_category,
            "brl_estimate": round(total * 5.65, 2),  # USD→BRL estimativa
        }

    def get_daily_breakdown(self, month: Optional[str] = None) -> list[dict]:
        """Breakdown diario para grafico."""
        if month is None:
            month = datetime.now().strftime("%Y-%m")

        with self._get_conn() as conn:
            rows = conn.execute(
                """SELECT DATE(recorded_at) as day, category, SUM(cost_usd) as total
                   FROM api_costs WHERE month = ?
                   GROUP BY DATE(recorded_at), category
                   ORDER BY day""",
                (month,),
            ).fetchall()

        return [dict(r) for r in rows]

    def get_recent(self, limit: int = 20) -> list[dict]:
        """Ultimos registros de gasto."""
        with self._get_conn() as conn:
            rows = conn.execute(
                "SELECT * FROM api_costs ORDER BY recorded_at DESC LIMIT ?",
                (limit,),
            ).fetchall()

        result = []
        for r in rows:
            d = dict(r)
            d["metadata"] = json.loads(d.get("metadata", "{}"))
            result.append(d)
        return result

    def _check_alerts(self, summary: dict) -> Optional[dict]:
        """Verifica se proximo do limite."""
        pct = summary["percentage_used"]

        if pct >= 100:
            return {
                "level": "CRITICAL",
                "message": f"TETO ATINGIDO — {pct}% do orcamento mensal usado (${summary['total_usd']:.2f} / ${self.limits.total:.2f})",
            }
        elif pct >= 80:
            return {
                "level": "WARNING",
                "message": f"ALERTA — {pct}% do orcamento mensal usado (${summary['total_usd']:.2f} / ${self.limits.total:.2f})",
            }
        elif pct >= 60:
            return {
                "level": "INFO",
                "message": f"{pct}% do orcamento mensal usado",
            }
        return None
