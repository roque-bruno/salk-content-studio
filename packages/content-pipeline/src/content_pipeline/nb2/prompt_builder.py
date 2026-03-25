"""
Prompt Builder — construção de prompts NB2 com arquitetura de 8 dimensões.

Dimensões:
1. Subject (produto)
2. Action (posicionamento)
3. Setting (cenário)
4. Lighting (iluminação)
5. Camera (equipamento e ângulo)
6. Style (estilo fotográfico)
7. Mood (atmosfera)
8. Technical (specs de output)

Regras NB2 incorporadas:
- NUNCA descrever o produto (IA distorce) — apenas o cenário
- NUNCA pedir glow/dispersão para LEV (contradiz luz concentrada)
- NUNCA incluir equipamentos médicos além do produto-alvo
- SEMPRE incluir negative prompt para equipamentos concorrentes
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class PromptDimension:
    """Uma dimensão do prompt NB2."""

    name: str
    content: str
    order: int = 0


@dataclass
class NB2PromptSpec:
    """Especificação completa de um prompt NB2."""

    subject: str = ""
    action: str = ""
    setting: str = ""
    lighting: str = ""
    camera: str = ""
    style: str = ""
    mood: str = ""
    technical: str = ""
    negative: str = ""

    def build(self) -> str:
        """Compila o prompt final."""
        sections = []

        if self.subject:
            sections.append(self.subject)
        if self.action:
            sections.append(f"\nSCENE DESCRIPTION:\n{self.action}")
        if self.setting:
            sections.append(self.setting)
        if self.lighting:
            sections.append(f"\nLIGHTING:\n{self.lighting}")
        if self.camera:
            sections.append(f"\nCAMERA:\n{self.camera}")
        if self.style:
            sections.append(f"\nSTYLE:\n{self.style}")
        if self.mood:
            sections.append(f"\nMOOD:\n{self.mood}")
        if self.technical:
            sections.append(f"\nTECHNICAL:\n{self.technical}")
        if self.negative:
            sections.append(f"\nNEGATIVE:\n{self.negative}")

        return "\n".join(sections)


# Regras NB2 validadas — incorporam todo o feedback do squad
NB2_RULES = {
    "product_fidelity": (
        "Place this EXACT uploaded {product_type} product in the scene. "
        "Do NOT modify the product design, shape, materials, colors, or proportions. "
        "The product must remain exactly as shown in the reference image."
    ),
    "negative_medical": (
        "No other medical devices in the scene. No surgical lights (unless the product IS a surgical light), "
        "no ceiling equipment, no monitors, no IV stands, no anesthesia machines. "
        "Clean isolated product hero shot."
    ),
    "negative_text": (
        "No text, no logos, no watermarks, no brand names, no people, "
        "no hands, no faces."
    ),
    "lev_no_scatter": (
        "The light beam is concentrated and focused on the surgical field — "
        "do NOT show scattered light rays, lateral glow, light dispersion, "
        "or volumetric god-rays. The precision of the beam IS the product feature."
    ),
}


CAMERA_PRESETS = {
    "dramatic_studio": {
        "camera": "Shot on Hasselblad X2D 100C with a 90mm f/2.8 lens",
        "angle": "slightly above eye level, 15 degrees downward",
        "focus": "tack-sharp product with gentle falloff on background",
    },
    "industrial_luxury": {
        "camera": "Shot on Canon EOS R5 with a 50mm f/1.8 lens",
        "angle": "low angle, camera at product-height level, looking slightly upward",
        "focus": "shallow depth of field with nearest surface in sharp focus",
    },
    "tech_reveal": {
        "camera": "Shot on Phase One XF IQ4 with a 55mm Schneider lens",
        "angle": "perfectly centered, at product-height level",
        "focus": "edge-to-edge sharpness at f/4",
    },
    "editorial_hero": {
        "camera": "Shot on Sony A1 with a 85mm f/1.4 GM lens",
        "angle": "eye level, slightly angled 10 degrees",
        "focus": "product tack-sharp, background with bokeh",
    },
}


LIGHTING_PRESETS = {
    "dramatic_three_point": {
        "key": "Large octabox overhead, camera-left, 45 degrees. Creates soft gradient across product surface",
        "fill": "Subtle silver reflector camera-right, just enough to open shadows without flatting contrast",
        "rim": "Thin strip light from behind at 170 degrees. Creates sharp white edge light separating product from background",
    },
    "industrial_cinematic": {
        "key": "Large overhead softbox, slightly camera-left, 60 degrees downward",
        "accent": "Warm-neutral strip light from camera-right at low angle, catching edges",
        "ambient": "Very low fill — let shadows be present for drama",
    },
    "symmetric_dual": {
        "key": "Two matched softboxes, one above each product element, at 50 degrees",
        "rim": "Single rim light strip behind entire product at ceiling level — continuous edge glow",
        "accent": "Subtle warm accent from below, very faint",
    },
}


SURFACE_PRESETS = {
    "reflective_black": {
        "material": "glossy obsidian-black acrylic sheet",
        "reflection": "mirror-like reflection, about 40% opacity, crisp and undistorted",
        "background": "seamless pure black (#000000)",
    },
    "polished_concrete": {
        "material": "polished concrete flooring in dark charcoal grey",
        "reflection": "soft diffused reflection, not mirror-sharp, grounding the product",
        "background": "smooth gradient from dark charcoal (#2D2D2D) to lighter grey (#404040)",
    },
    "brushed_metal": {
        "material": "large sheet of brushed dark metal (anodized aluminum)",
        "reflection": "soft and stretched, about 30% opacity, creating visual symmetry",
        "background": "deep navy-black gradient (#0A0A1A to #1A1A2E)",
    },
}


class PromptBuilder:
    """
    Construtor de prompts NB2 com presets e regras de qualidade.

    Usa presets validados pelo squad para câmera, iluminação e superfícies,
    aplicando automaticamente as regras NB2 (sem descrever produto,
    sem equipamentos concorrentes, sem glow em LEV, etc.).
    """

    def build_hero_prompt(
        self,
        *,
        product_type: str,
        product_details: str = "",
        scene_description: str,
        lighting_preset: str = "dramatic_three_point",
        camera_preset: str = "dramatic_studio",
        surface_preset: str = "reflective_black",
        style: str = "",
        mood: str = "",
        aspect_ratio: str = "4:5",
        width: int = 1080,
        height: int = 1350,
        is_lev: bool = False,
        extra_negative: str = "",
    ) -> str:
        """
        Constrói prompt NB2 hero shot completo.

        Args:
            product_type: Tipo do produto (ex: "surgical light", "surgical table").
            product_details: Detalhes visuais do produto para preservação.
            scene_description: Descrição do cenário (NÃO do produto).
            lighting_preset: Preset de iluminação.
            camera_preset: Preset de câmera.
            surface_preset: Preset de superfície.
            style: Estilo fotográfico.
            mood: Atmosfera desejada.
            aspect_ratio: Proporção da imagem.
            width: Largura em pixels.
            height: Altura em pixels.
            is_lev: Se True, aplica regra anti-scatter para LEV.
            extra_negative: Instruções negativas adicionais.

        Returns:
            Prompt NB2 completo pronto para envio à API.
        """
        spec = NB2PromptSpec()

        # 1. Subject — fidelidade do produto
        subject = NB2_RULES["product_fidelity"].format(product_type=product_type)
        if product_details:
            subject += f" {product_details}"
        spec.subject = subject

        # 2-3. Scene + Setting
        surface = SURFACE_PRESETS.get(surface_preset, SURFACE_PRESETS["reflective_black"])
        scene_parts = [scene_description]
        scene_parts.append(
            f"\nThe surface below is {surface['material']}, "
            f"catching {surface['reflection']}. "
            f"The background is {surface['background']}."
        )
        spec.action = "\n".join(scene_parts)

        # 4. Lighting
        lighting = LIGHTING_PRESETS.get(lighting_preset, LIGHTING_PRESETS["dramatic_three_point"])
        lighting_parts = []
        for role, desc in lighting.items():
            lighting_parts.append(f"- {role.title()}: {desc}")
        if is_lev:
            lighting_parts.append(f"\n{NB2_RULES['lev_no_scatter']}")
        spec.lighting = "\n".join(lighting_parts)

        # 5. Camera
        cam = CAMERA_PRESETS.get(camera_preset, CAMERA_PRESETS["dramatic_studio"])
        spec.camera = (
            f"{cam['camera']}. "
            f"Camera positioned {cam['angle']}. "
            f"{cam['focus']}."
        )

        # 6. Style
        spec.style = style or (
            "Premium product photography. Clean, modern, professional. "
            "The image communicates engineering excellence and reliability."
        )

        # 7. Mood
        spec.mood = mood or (
            "Authority and precision. A visual statement of quality "
            "that would stop a decision-maker's scroll."
        )

        # 8. Technical + Negative
        tech_parts = [
            f"Aspect ratio {aspect_ratio} ({width}x{height} pixels).",
            NB2_RULES["negative_text"],
            NB2_RULES["negative_medical"],
        ]
        if extra_negative:
            tech_parts.append(extra_negative)
        spec.technical = " ".join(tech_parts)

        prompt = spec.build()
        logger.info(
            "Prompt construído: %d chars | preset=%s/%s/%s",
            len(prompt),
            camera_preset,
            lighting_preset,
            surface_preset,
        )
        return prompt

    def from_vdp_prompt(self, raw_prompt: str) -> str:
        """
        Usa prompt já pronto de um VDP (sem modificação).

        Validações aplicadas:
        - Verifica presença de negative prompt
        - Adiciona se ausente

        Args:
            raw_prompt: Prompt extraído do VDP.

        Returns:
            Prompt validado.
        """
        has_negative = any(
            term in raw_prompt.lower()
            for term in ["no text", "no logos", "no other medical"]
        )

        if not has_negative:
            logger.warning("VDP prompt sem negative — adicionando regras padrão")
            raw_prompt += (
                f"\n\nTECHNICAL CONSTRAINTS:\n"
                f"{NB2_RULES['negative_text']} "
                f"{NB2_RULES['negative_medical']}"
            )

        return raw_prompt
