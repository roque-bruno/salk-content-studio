"""
Content Pipeline — Constantes e Defaults centralizados.

Modulo criado pelo Epic 16 (DRY Refactor) para eliminar hardcodes espalhados.
"""

# ---------------------------------------------------------------------------
# Brand & Platform defaults
# ---------------------------------------------------------------------------
DEFAULT_BRAND = "salk"
DEFAULT_PLATFORM = "instagram"
DEFAULT_FORMAT = "post"
DEFAULT_PILLAR = "produto"

# ---------------------------------------------------------------------------
# Image Generation defaults
# ---------------------------------------------------------------------------
DEFAULT_NEGATIVE_PROMPT = "text, logo, watermark, blurry, low quality"
DEFAULT_IMAGE_MODEL = "nb2"
DEFAULT_IMAGE_WIDTH = 1080
DEFAULT_IMAGE_HEIGHT = 1350

# ---------------------------------------------------------------------------
# Prompt defaults (Auto-Prompt NB2 / Apex)
# ---------------------------------------------------------------------------
DEFAULT_PRODUCT = "lev"
DEFAULT_TECHNIQUE = "dramatic_studio"
DEFAULT_LIGHTING = "dramatic_rim"
DEFAULT_SCENE = "studio_neutro"
DEFAULT_COMPOSITION = "central_hero"
DEFAULT_ATMOSPHERE = "premium_tech"
DEFAULT_FORMAT_PRESET = "square_social"

# ---------------------------------------------------------------------------
# Copy parsing — keywords para detectar CTA
# ---------------------------------------------------------------------------
CTA_KEYWORDS = [
    "saiba mais", "converse", "consulte", "conheça", "fale com",
    "acesse", "solicite", "confira", "agende", "faca parte", "descubra",
]

# ---------------------------------------------------------------------------
# Pilares institucionais (NB2 prompt-only, sem inferencia de produto)
# ---------------------------------------------------------------------------
INSTITUTIONAL_PILLARS = ("datas_comemorativas", "institucional")

# ---------------------------------------------------------------------------
# A/B Test — conceitos visuais
# ---------------------------------------------------------------------------
AB_TEST_VISUAL_CONCEPTS = [
    "dramatic_studio", "clinical_modern", "premium_clean",
    "warm_ambient", "hero_closeup", "environment_wide",
    "tech_detail", "action_use", "atmospheric_mood",
    "minimalist_white", "dark_contrast", "golden_hour",
    "architectural", "reflection_glass", "depth_of_field",
    "symmetry", "silhouette_backlit", "macro_detail",
    "editorial_spread", "brand_lifestyle",
]
