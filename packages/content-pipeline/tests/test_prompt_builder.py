"""Testes do Prompt Builder — construção de prompts NB2."""

import pytest

from content_pipeline.nb2.prompt_builder import (
    CAMERA_PRESETS,
    LIGHTING_PRESETS,
    NB2_RULES,
    SURFACE_PRESETS,
    PromptBuilder,
)


@pytest.fixture
def builder():
    return PromptBuilder()


def test_build_hero_prompt_basic(builder):
    prompt = builder.build_hero_prompt(
        product_type="surgical light",
        scene_description="A dramatic dark studio.",
    )
    assert "EXACT uploaded surgical light" in prompt
    assert "SCENE DESCRIPTION:" in prompt
    assert "LIGHTING:" in prompt
    assert "CAMERA:" in prompt
    assert "TECHNICAL:" in prompt
    assert "No text, no logos" in prompt
    assert "No other medical devices" in prompt


def test_lev_anti_scatter(builder):
    prompt = builder.build_hero_prompt(
        product_type="surgical light",
        scene_description="Dark studio.",
        is_lev=True,
    )
    assert "concentrated" in prompt
    assert "do NOT show scattered light" in prompt


def test_lev_no_scatter_absent_when_not_lev(builder):
    prompt = builder.build_hero_prompt(
        product_type="surgical table",
        scene_description="Dark studio.",
        is_lev=False,
    )
    assert "do NOT show scattered light" not in prompt


def test_camera_presets_exist():
    assert "dramatic_studio" in CAMERA_PRESETS
    assert "industrial_luxury" in CAMERA_PRESETS
    assert "tech_reveal" in CAMERA_PRESETS


def test_lighting_presets_exist():
    assert "dramatic_three_point" in LIGHTING_PRESETS
    assert "industrial_cinematic" in LIGHTING_PRESETS
    assert "symmetric_dual" in LIGHTING_PRESETS


def test_surface_presets_exist():
    assert "reflective_black" in SURFACE_PRESETS
    assert "polished_concrete" in SURFACE_PRESETS
    assert "brushed_metal" in SURFACE_PRESETS


def test_custom_style_and_mood(builder):
    prompt = builder.build_hero_prompt(
        product_type="surgical table",
        scene_description="Industrial studio.",
        style="German automotive advertising meets medical precision.",
        mood="Solid authority. Engineering confidence.",
    )
    assert "German automotive" in prompt
    assert "Solid authority" in prompt


def test_from_vdp_prompt_with_negatives(builder):
    raw = "Place this product. No text, no logos. No other medical devices."
    result = builder.from_vdp_prompt(raw)
    assert result == raw  # Already has negatives, no modification


def test_from_vdp_prompt_adds_negatives(builder):
    raw = "Place this product in a dramatic scene."
    result = builder.from_vdp_prompt(raw)
    assert len(result) > len(raw)
    assert "No text, no logos" in result
    assert "No other medical devices" in result


def test_nb2_rules_completeness():
    assert "product_fidelity" in NB2_RULES
    assert "negative_medical" in NB2_RULES
    assert "negative_text" in NB2_RULES
    assert "lev_no_scatter" in NB2_RULES
