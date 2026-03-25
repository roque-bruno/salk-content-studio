"""Fixtures compartilhadas para todos os testes."""

from __future__ import annotations

from pathlib import Path
from textwrap import dedent
from unittest.mock import MagicMock

import pytest
from PIL import Image


@pytest.fixture
def project_root(tmp_path):
    """Raiz de projeto simulada com estrutura completa."""
    # Criar estrutura de diretórios
    (tmp_path / "docs_user" / "imagem_produtos" / "Foco de Teto e Parede").mkdir(parents=True)
    (tmp_path / "docs_user" / "imagem_produtos" / "Mesa Cirurgica").mkdir(parents=True)
    (tmp_path / "docs_user" / "logos").mkdir(parents=True)
    (tmp_path / "squads" / "content-production" / "output" / "calibracao").mkdir(parents=True)
    (tmp_path / "output").mkdir()

    return tmp_path


@pytest.fixture
def sample_product_png(project_root):
    """PNG de produto simulado (imagem 200x200 com fundo transparente)."""
    img = Image.new("RGBA", (200, 200), (200, 200, 200, 255))
    path = project_root / "docs_user" / "imagem_produtos" / "Foco de Teto e Parede" / "Simplex_4LEV.png"
    img.save(str(path), "PNG")
    return path


@pytest.fixture
def sample_kratus_png(project_root):
    """PNG do KRATUS simulado."""
    img = Image.new("RGBA", (300, 200), (180, 180, 180, 255))
    path = project_root / "docs_user" / "imagem_produtos" / "Mesa Cirurgica" / "KRATUS-EH-460K-ML-clean01.png"
    img.save(str(path), "PNG")
    return path


@pytest.fixture
def sample_vdp_content():
    """Conteúdo VDP padrão para testes."""
    return dedent("""\
        # VDP — Hero Shot LEV 4LEV (Calibracao v1)

        **Produto:** Foco Cirurgico LEV 4LEV (Simplex Teto)
        **Marca:** Mendel Medical (conteudo tecnico)
        **Formato:** Feed Instagram 1080x1350 (4:5)
        **Conceito:** "Dramatic Studio — Precisao sob Controle"
        **PNG de Referencia:** `docs_user/imagem_produtos/Foco de Teto e Parede/Simplex_4LEV.png`

        ---

        ## 1. Prompt NB2 — Google AI Studio

        ```
        Place this EXACT uploaded surgical light product in the scene.
        Do NOT modify the product design, shape, materials, colors, or proportions.
        The product must remain exactly as shown in the reference image.

        SCENE DESCRIPTION:
        A dramatic dark studio environment. The surgical light is the absolute hero,
        suspended from above, occupying approximately 65% of the frame.
        The background is a seamless pure black (#000000).

        LIGHTING:
        Premium three-point studio lighting.
        - Key: Large octabox overhead, camera-left, 45 degrees
        - Fill: Subtle silver reflector camera-right
        - Rim: Thin strip light from behind at 170 degrees

        CAMERA:
        Shot on Hasselblad X2D 100C with a 90mm f/2.8 lens.
        Camera positioned slightly above eye level, 15 degrees downward.

        STYLE:
        Premium medical product photography. Clean, modern, professional.

        MOOD:
        Precision and authority. Engineering excellence.

        TECHNICAL:
        Aspect ratio 4:5 (1080x1350 pixels). No text, no logos, no watermarks.
        No other medical devices in the scene. Clean isolated product hero shot.
        ```

        ---

        ## 2. Instrucoes de Composicao Canva

        **Template:** Feed Instagram 1080x1350

        | Elemento | Especificacao |
        |----------|--------------|
        | **Logo** | `LogMendel-M-rev.jpg` (branca) — canto superior direito, 180px |
        | **Headline** | "Ra 99. A luz mais proxima da realidade." — 36pt bold, branco |
        | **Spec line** | "Foco Cirurgico LEV | Ra 99 | 160.000 lux" — 18pt light, branco 70% |
        | **ANVISA badge** | "Reg. ANVISA 81205910005" — 12pt, branco 50% |
        | **Gradiente topo** | Preto puro→transparente, 45% opacidade, 200px |
        | **Gradiente rodape** | Preto puro→transparente, 60% opacidade, 250px |
        | **Margens** | 60px em todos os lados |
        | **Zona protegida** | NUNCA colocar texto sobre a cupula ou reflexo |

        ---

        ## 3. Claims Utilizados

        | Claim ID | Texto |
        |----------|-------|
        | LEV-01 | Indice de Reproducao de Cor Ra 99 |
        | LEV-03 | Iluminancia central maxima de ate 160.000 lux |
        | LEV-05 | Protecao IP54 nas cupulas LEV |
        | LEV-12 | Fabricado no Brasil pela Mendel Medical |

        ---

        ## 4. Criterios de Aprovacao

        - [ ] Produto fiel ao PNG original
        - [ ] Reflexo suave no piso reflexivo preto
        - [ ] Iluminacao premium sem glow/dispersao
        - [ ] Sem equipamento concorrente
        - [ ] Sem texto/logo gerado pela IA
        - [ ] Qualidade de advertising profissional
        - [ ] Pararia meu scroll no LinkedIn

        ---

        **VDP gerado por Apex (visual-designer) — 2026-03-25**
    """)


@pytest.fixture
def sample_vdp_file(project_root, sample_vdp_content):
    """Arquivo VDP salvo no diretório de calibração."""
    path = project_root / "squads" / "content-production" / "output" / "calibracao" / "hero-lev-v1.md"
    path.write_text(sample_vdp_content, encoding="utf-8")
    return path


@pytest.fixture
def mock_generated_image():
    """Imagem simulada como se fosse gerada pelo Gemini."""
    return Image.new("RGB", (1080, 1350), (30, 30, 30))


@pytest.fixture
def mock_gemini_response(mock_generated_image):
    """Response simulado do Gemini com imagem inline."""
    import io

    buf = io.BytesIO()
    mock_generated_image.save(buf, format="PNG")
    image_bytes = buf.getvalue()

    inline_data = MagicMock()
    inline_data.data = image_bytes

    part = MagicMock()
    part.inline_data = inline_data

    content = MagicMock()
    content.parts = [part]

    candidate = MagicMock()
    candidate.content = content

    response = MagicMock()
    response.candidates = [candidate]

    return response
