"""
Batch Approval — Gestora aprova semana inteira de conteudo de uma vez.

Workflow:
1. Lista todas as pecas de uma semana pendentes de aprovacao
2. Apresenta resumo (copy, visual, compliance status)
3. Gestora pode: aprovar tudo, rejeitar individual, ou aprovar com notas
4. Pecas aprovadas avancam para publicacao
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Optional

logger = logging.getLogger(__name__)


class BatchApproval:
    """Workflow de aprovacao em batch para a gestora."""

    def __init__(self, db=None, brand_enforcer=None):
        self.db = db
        self.brand_enforcer = brand_enforcer

    def get_pending_batch(
        self,
        week_id: str = "",
        brand: str = "",
    ) -> dict:
        """
        Lista pecas pendentes de aprovacao para uma semana.

        Returns:
            dict com pecas agrupadas por dia e status de compliance
        """
        if self.db is None:
            return {"error": "Database nao configurado", "pieces": []}

        # Buscar pecas em stage "review"
        pieces = self.db.list_pieces(stage="review", brand=brand)

        # Filtrar por semana se especificado
        if week_id:
            calendar = self.db.load_calendar(week_id)
            if calendar:
                piece_ids = {
                    slot.get("piece_id")
                    for slot in calendar.get("slots", [])
                    if slot.get("piece_id")
                }
                pieces = [p for p in pieces if p.get("id") in piece_ids]

        # Enriquecer com status de compliance
        enriched = []
        for piece in pieces:
            item = {
                **piece,
                "compliance_status": "unknown",
                "compliance_issues": [],
            }

            # Verificar compliance do copy
            copy_text = piece.get("copy_text", "")
            if copy_text and self.brand_enforcer:
                result = self.brand_enforcer.validate(
                    copy_text, piece.get("brand", "salk"), context="copy"
                )
                item["compliance_status"] = "passed" if result.is_valid else "failed"
                item["compliance_issues"] = [
                    {"rule": v.rule, "detail": v.detail, "severity": v.severity}
                    for v in result.violations
                ]

            enriched.append(item)

        return {
            "week_id": week_id,
            "brand": brand,
            "total_pieces": len(enriched),
            "all_compliant": all(
                p.get("compliance_status") != "failed" for p in enriched
            ),
            "pieces": enriched,
        }

    def approve_batch(
        self,
        piece_ids: list[str],
        approver: str = "gestora",
        notes: str = "",
    ) -> dict:
        """
        Aprova multiplas pecas de uma vez.

        Returns:
            dict com resultado da aprovacao
        """
        if self.db is None:
            return {"error": "Database nao configurado"}

        approved = []
        failed = []

        for pid in piece_ids:
            try:
                result = self.db.update_piece_stage(
                    pid, "approved",
                    notes=f"Batch approved by {approver}. {notes}".strip(),
                )
                if result:
                    approved.append(pid)

                    # Criar review automatico
                    self.db.create_review({
                        "piece_id": pid,
                        "reviewer": approver,
                        "verdict": "approved",
                        "comments": f"Batch approval: {notes}" if notes else "Batch approval",
                    })
                else:
                    failed.append({"id": pid, "reason": "Peca nao encontrada"})
            except Exception as e:
                failed.append({"id": pid, "reason": str(e)})

        return {
            "approved_count": len(approved),
            "failed_count": len(failed),
            "approved_ids": approved,
            "failed": failed,
            "approved_at": datetime.now().isoformat(),
            "approved_by": approver,
        }

    def reject_pieces(
        self,
        rejections: list[dict],
        reviewer: str = "gestora",
    ) -> dict:
        """
        Rejeita pecas individuais com feedback.

        Args:
            rejections: Lista de {"piece_id": str, "reason": str}
        """
        if self.db is None:
            return {"error": "Database nao configurado"}

        results = []
        for rej in rejections:
            pid = rej.get("piece_id", "")
            reason = rej.get("reason", "Rejeitado na revisao batch")

            try:
                self.db.update_piece_stage(pid, "copy", notes=f"Rejected: {reason}")
                self.db.create_review({
                    "piece_id": pid,
                    "reviewer": reviewer,
                    "verdict": "rejected",
                    "comments": reason,
                })
                results.append({"id": pid, "status": "rejected"})
            except Exception as e:
                results.append({"id": pid, "status": "error", "reason": str(e)})

        return {
            "rejected_count": len([r for r in results if r["status"] == "rejected"]),
            "results": results,
        }

    def get_approval_summary(self, week_id: str = "") -> dict:
        """Resumo de aprovacoes da semana."""
        if self.db is None:
            return {"total": 0}

        reviews = self.db.list_reviews()
        approved = [r for r in reviews if r.get("verdict") == "approved"]
        rejected = [r for r in reviews if r.get("verdict") == "rejected"]
        pending_pieces = self.db.list_pieces(stage="review")

        return {
            "total_approved": len(approved),
            "total_rejected": len(rejected),
            "pending_review": len(pending_pieces),
            "approval_rate": round(
                len(approved) / (len(approved) + len(rejected)) * 100
                if (approved or rejected) else 0, 1
            ),
        }
