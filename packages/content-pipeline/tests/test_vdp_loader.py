"""Testes do VDP Loader — parsing de arquivos Visual Design Pack."""

from pathlib import Path
from textwrap import dedent

import pytest

from content_pipeline.nb2.vdp_loader import VDPLoader, VDPSpec


@pytest.fixture
def loader():
    return VDPLoader()


@pytest.fixture
def sample_vdp(tmp_path):
    """VDP de exemplo para testes."""
    content = dedent("""\
        # VDP — Hero Shot Produto Teste (Calibracao v1)

        **Produto:** Foco Cirurgico LEV 4LEV (Simplex Teto)
        **Marca:** Mendel Medical (conteudo tecnico)
        **Formato:** Feed Instagram 1080x1350 (4:5)
        **Conceito:** "Dramatic Studio — Precisao sob Controle"
        **PNG de Referencia:** `docs_user/imagem_produtos/Foco de Teto e Parede/Simplex_4LEV.png`

        ---

        ## 1. Prompt NB2 — Google AI Studio

        ```
        Place this EXACT uploaded surgical light in the scene.
        Do NOT modify the product design, shape, materials, colors, or proportions.

        SCENE DESCRIPTION:
        A dramatic dark studio environment.

        LIGHTING:
        Three-point lighting setup.

        TECHNICAL:
        Aspect ratio 4:5 (1080x1350 pixels). No text, no logos, no watermarks.
        ```

        ---

        ## 2. Instrucoes de Composicao Canva

        **Template:** Feed Instagram 1080x1350

        | Elemento | Especificacao |
        |----------|--------------|
        | **Logo** | `LogMendel-M-rev.jpg` (branca) — canto superior direito, 180px |
        | **Headline** | "Ra 99. A luz mais proxima da realidade." — 36pt bold, branco |
        | **Spec line** | "Foco Cirurgico LEV | Ra 99" — 18pt light, branco 70% |
        | **ANVISA badge** | "Reg. ANVISA 81205910005" — 12pt, branco 50% |
        | **Margens** | 60px em todos os lados |

        ---

        ## 3. Claims Utilizados

        | Claim ID | Texto |
        |----------|-------|
        | LEV-01 | Indice de Reproducao de Cor Ra 99 |
        | LEV-03 | Iluminancia central maxima de ate 160.000 lux |

        ---

        ## 4. Criterios de Aprovacao

        - [ ] Produto fiel ao PNG original
        - [ ] Reflexo suave no piso reflexivo
        - [ ] Sem equipamento concorrente
        - [ ] Qualidade de advertising premium

        ---
    """)
    vdp_file = tmp_path / "hero-test-v1.md"
    vdp_file.write_text(content, encoding="utf-8")
    return vdp_file


def test_load_header(loader, sample_vdp):
    spec = loader.load(sample_vdp)
    assert spec.produto == "Foco Cirurgico LEV 4LEV (Simplex Teto)"
    assert spec.marca == "Mendel Medical (conteudo tecnico)"
    assert spec.formato == "Feed Instagram 1080x1350 (4:5)"
    assert spec.conceito == "Dramatic Studio — Precisao sob Controle"
    assert "Simplex_4LEV.png" in spec.png_referencia


def test_load_prompt(loader, sample_vdp):
    spec = loader.load(sample_vdp)
    assert len(spec.prompt_nb2) > 100
    assert "Place this EXACT" in spec.prompt_nb2
    assert "LIGHTING:" in spec.prompt_nb2


def test_load_claims(loader, sample_vdp):
    spec = loader.load(sample_vdp)
    assert len(spec.claims) == 2
    assert spec.claims[0].claim_id == "LEV-01"
    assert "Ra 99" in spec.claims[0].texto
    assert spec.claims[1].claim_id == "LEV-03"


def test_load_criterios(loader, sample_vdp):
    spec = loader.load(sample_vdp)
    assert len(spec.criterios_aprovacao) == 4
    assert "Produto fiel" in spec.criterios_aprovacao[0]


def test_load_canva(loader, sample_vdp):
    spec = loader.load(sample_vdp)
    assert "1080x1350" in spec.canva.template
    assert "LogMendel" in spec.canva.logo
    assert "Ra 99" in spec.canva.headline
    assert "ANVISA" in spec.canva.anvisa_badge


def test_brand_detection(loader, sample_vdp):
    spec = loader.load(sample_vdp)
    assert spec.is_mendel is True
    assert spec.is_salk is False


def test_product_slug(loader, sample_vdp):
    spec = loader.load(sample_vdp)
    slug = spec.product_slug
    assert slug == "foco-cirurgico-lev-4lev-simplex-teto"


def test_missing_prompt_raises(loader, tmp_path):
    vdp = tmp_path / "empty.md"
    vdp.write_text("# VDP sem prompt\n**Produto:** Teste\n")
    with pytest.raises(ValueError, match="sem prompt NB2"):
        loader.load(vdp)


def test_missing_file_raises(loader):
    with pytest.raises(FileNotFoundError):
        loader.load(Path("/nonexistent/vdp.md"))


def test_load_directory(loader, tmp_path, sample_vdp):
    # Copia o sample_vdp para tmp_path (já está lá)
    specs = loader.load_directory(tmp_path)
    assert len(specs) == 1
    assert specs[0].produto == "Foco Cirurgico LEV 4LEV (Simplex Teto)"
