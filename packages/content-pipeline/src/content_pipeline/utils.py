"""
Content Pipeline — Funcoes utilitarias compartilhadas.

Modulo criado pelo Epic 16 (DRY Refactor) para eliminar duplicacoes.
"""

from __future__ import annotations

import json
import logging
from typing import Any

from content_pipeline.constants import CTA_KEYWORDS

logger = logging.getLogger(__name__)


def parse_piece_notes(piece_or_notes: Any, default: dict | None = None) -> dict:
    """Safely parse JSON from piece.notes field.

    Accepts either:
      - A dict (piece) with a "notes" key
      - A raw string (notes JSON)
      - None / empty
    """
    if default is None:
        default = {}
    if piece_or_notes is None:
        return default
    if isinstance(piece_or_notes, dict):
        raw = piece_or_notes.get("notes", "")
    else:
        raw = piece_or_notes
    if not raw:
        return default
    try:
        parsed = json.loads(raw)
        return parsed if isinstance(parsed, dict) else default
    except (ValueError, TypeError):
        return default


def parse_copy_components(raw_copy: str) -> dict:
    """Parse raw copy text into headline, hashtags, CTA, and clean body.

    Returns dict with keys: headline, hashtags, cta, body
    """
    lines = [line for line in raw_copy.split("\n") if line.strip()]
    headline = ""
    hashtags: list[str] = []
    cta = ""
    body_lines: list[str] = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#") and stripped.count("#") >= 2 and not stripped.startswith("##"):
            hashtags = [t.strip() for t in stripped.split() if t.startswith("#")]
            continue
        if not headline and len(stripped) < 100 and not stripped.startswith("http"):
            headline = stripped.lstrip("#").lstrip("*").rstrip("*").strip()
            continue
        body_lines.append(line)

    for bl in reversed(body_lines):
        if any(kw in bl.lower() for kw in CTA_KEYWORDS):
            cta = bl.strip()
            body_lines.remove(bl)
            break

    return {
        "headline": headline,
        "hashtags": hashtags,
        "cta": cta,
        "body": "\n".join(body_lines).strip(),
    }
