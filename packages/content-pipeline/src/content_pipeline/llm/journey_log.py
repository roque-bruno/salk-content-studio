"""
Journey Log — Registro historico de todas as decisoes e resultados do pipeline.

Cada acao (geracao, validacao, rejeicao, publicacao) e registrada com contexto.
Usado pelo Pulse para self-learning: analisar padroes de sucesso/falha e ajustar parametros.

Exemplo de entrada:
    journey.log("generation", "nb2", piece_id="abc123", result="success",
                details={"prompt_length": 450, "attempts": 2, "elapsed_s": 12.5})
"""

from __future__ import annotations

import json
import logging
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


class JourneyLog:
    """Registro imutavel de todas as acoes do pipeline."""

    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
        self._init_db()

    def _get_conn(self) -> sqlite3.Connection:
        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._get_conn() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS journey (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    phase TEXT NOT NULL,
                    agent TEXT NOT NULL,
                    piece_id TEXT DEFAULT '',
                    brand TEXT DEFAULT '',
                    result TEXT NOT NULL,
                    details TEXT DEFAULT '{}',
                    cost_usd REAL DEFAULT 0,
                    elapsed_ms INTEGER DEFAULT 0,
                    recorded_at TEXT NOT NULL
                )
            """)
            conn.execute("CREATE INDEX IF NOT EXISTS idx_journey_phase ON journey(phase)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_journey_piece ON journey(piece_id)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_journey_result ON journey(result)")

    def log(
        self,
        phase: str,
        agent: str,
        piece_id: str = "",
        brand: str = "",
        result: str = "success",
        details: Optional[dict] = None,
        cost_usd: float = 0,
        elapsed_ms: int = 0,
    ) -> int:
        """
        Registra uma acao no Journey Log.

        Args:
            phase: briefing, copy, generation, compliance, review, publish, atomize
            agent: Atlas, Helix, Apex, Shield, Lens, Nova, Pulse
            piece_id: ID da peca (se aplicavel)
            brand: Marca (salk, mendel, etc.)
            result: success, failure, rejected, blocked, skipped
            details: Dados extras (prompt, score, motivo, etc.)
            cost_usd: Custo da operacao
            elapsed_ms: Tempo de execucao

        Returns:
            ID do registro
        """
        now = datetime.now().isoformat()
        with self._get_conn() as conn:
            cursor = conn.execute(
                """INSERT INTO journey
                   (phase, agent, piece_id, brand, result, details, cost_usd, elapsed_ms, recorded_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (phase, agent, piece_id, brand, result,
                 json.dumps(details or {}), cost_usd, elapsed_ms, now),
            )
            return cursor.lastrowid or 0

    def query(
        self,
        phase: Optional[str] = None,
        agent: Optional[str] = None,
        piece_id: Optional[str] = None,
        result: Optional[str] = None,
        limit: int = 50,
    ) -> list[dict]:
        """Consulta entradas do log."""
        query = "SELECT * FROM journey WHERE 1=1"
        params: list = []
        if phase:
            query += " AND phase = ?"
            params.append(phase)
        if agent:
            query += " AND agent = ?"
            params.append(agent)
        if piece_id:
            query += " AND piece_id = ?"
            params.append(piece_id)
        if result:
            query += " AND result = ?"
            params.append(result)
        query += " ORDER BY recorded_at DESC LIMIT ?"
        params.append(limit)

        with self._get_conn() as conn:
            rows = conn.execute(query, params).fetchall()

        entries = []
        for r in rows:
            d = dict(r)
            d["details"] = json.loads(d.get("details", "{}"))
            entries.append(d)
        return entries

    def get_stats(self) -> dict:
        """Estatisticas do Journey Log para self-learning."""
        with self._get_conn() as conn:
            # Total por resultado
            result_rows = conn.execute(
                "SELECT result, COUNT(*) as count FROM journey GROUP BY result"
            ).fetchall()

            # Total por fase
            phase_rows = conn.execute(
                "SELECT phase, COUNT(*) as count, "
                "SUM(CASE WHEN result='success' THEN 1 ELSE 0 END) as successes, "
                "SUM(cost_usd) as total_cost, "
                "AVG(elapsed_ms) as avg_elapsed "
                "FROM journey GROUP BY phase"
            ).fetchall()

            # Taxa de sucesso por agente
            agent_rows = conn.execute(
                "SELECT agent, COUNT(*) as count, "
                "SUM(CASE WHEN result='success' THEN 1 ELSE 0 END) as successes "
                "FROM journey GROUP BY agent"
            ).fetchall()

            total = conn.execute("SELECT COUNT(*) FROM journey").fetchone()[0]

        by_result = {r["result"]: r["count"] for r in result_rows}
        by_phase = {
            r["phase"]: {
                "total": r["count"],
                "successes": r["successes"],
                "success_rate": round(r["successes"] / r["count"] * 100, 1) if r["count"] > 0 else 0,
                "total_cost_usd": round(r["total_cost"], 4),
                "avg_elapsed_ms": round(r["avg_elapsed"], 0),
            }
            for r in phase_rows
        }
        by_agent = {
            r["agent"]: {
                "total": r["count"],
                "successes": r["successes"],
                "success_rate": round(r["successes"] / r["count"] * 100, 1) if r["count"] > 0 else 0,
            }
            for r in agent_rows
        }

        return {
            "total_entries": total,
            "by_result": by_result,
            "by_phase": by_phase,
            "by_agent": by_agent,
        }

    def get_piece_journey(self, piece_id: str) -> list[dict]:
        """Retorna toda a jornada de uma peca especifica."""
        return self.query(piece_id=piece_id, limit=100)
