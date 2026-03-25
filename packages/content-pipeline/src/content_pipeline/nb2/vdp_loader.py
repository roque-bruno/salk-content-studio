"""
VDP Loader — parser de arquivos Visual Design Pack (Markdown).

Extrai prompt NB2, metadados do produto, instruções de composição Canva,
claims utilizados e critérios de aprovação de arquivos .md estruturados.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class CanvaComposition:
    """Instruções de composição para Canva."""

    template: str = ""
    logo: str = ""
    headline: str = ""
    spec_line: str = ""
    anvisa_badge: str = ""
    gradiente_topo: str = ""
    gradiente_rodape: str = ""
    margens: str = "60px"
    zona_protegida: str = ""
    elements: dict[str, str] = field(default_factory=dict)


@dataclass
class Claim:
    """Claim regulatório utilizado no VDP."""

    claim_id: str
    texto: str
    fonte: str = ""


@dataclass
class VDPSpec:
    """
    Especificação completa de um Visual Design Pack.

    Contém tudo necessário para gerar e compor uma peça:
    - Metadados do produto
    - Prompt NB2 completo
    - Instruções de composição Canva
    - Claims regulatórios
    - Critérios de aprovação
    """

    file_path: Path
    produto: str = ""
    marca: str = ""
    formato: str = ""
    conceito: str = ""
    png_referencia: str = ""
    prompt_nb2: str = ""
    canva: CanvaComposition = field(default_factory=CanvaComposition)
    claims: list[Claim] = field(default_factory=list)
    criterios_aprovacao: list[str] = field(default_factory=list)
    versao: str = "v1"

    @property
    def product_slug(self) -> str:
        """Slug do produto para nomes de arquivo."""
        return re.sub(r"[^a-z0-9]+", "-", self.produto.lower()).strip("-")

    @property
    def is_salk(self) -> bool:
        """Verifica se é conteúdo Salk (comercial)."""
        return "salk" in self.marca.lower()

    @property
    def is_mendel(self) -> bool:
        """Verifica se é conteúdo Mendel (técnico)."""
        return "mendel" in self.marca.lower()


class VDPLoader:
    """
    Parser de arquivos VDP em formato Markdown.

    Extrai seções estruturadas de arquivos .md que seguem
    o template padrão do squad de produção de conteúdo.
    """

    def load(self, file_path: Path) -> VDPSpec:
        """
        Carrega e parseia um arquivo VDP.

        Args:
            file_path: Caminho para o arquivo .md do VDP.

        Returns:
            VDPSpec com todas as seções extraídas.

        Raises:
            FileNotFoundError: Se o arquivo não existir.
            ValueError: Se o arquivo não contiver prompt NB2.
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"VDP não encontrado: {path}")

        content = path.read_text(encoding="utf-8")
        logger.info("Carregando VDP: %s", path.name)

        spec = VDPSpec(file_path=path)

        self._parse_header(content, spec)
        self._parse_prompt(content, spec)
        self._parse_canva(content, spec)
        self._parse_claims(content, spec)
        self._parse_criterios(content, spec)

        if not spec.prompt_nb2:
            raise ValueError(f"VDP sem prompt NB2: {path.name}")

        logger.info(
            "VDP carregado: %s | prompt=%d chars | claims=%d",
            spec.produto,
            len(spec.prompt_nb2),
            len(spec.claims),
        )
        return spec

    def load_directory(self, dir_path: Path) -> list[VDPSpec]:
        """Carrega todos os VDPs de um diretório."""
        path = Path(dir_path)
        if not path.is_dir():
            raise NotADirectoryError(f"Diretório não encontrado: {path}")

        vdps = []
        for md_file in sorted(path.glob("*.md")):
            try:
                vdps.append(self.load(md_file))
            except (ValueError, Exception) as e:
                logger.warning("Ignorando %s: %s", md_file.name, e)

        logger.info("Carregados %d VDPs de %s", len(vdps), path)
        return vdps

    def _parse_header(self, content: str, spec: VDPSpec) -> None:
        """Extrai metadados do cabeçalho do VDP."""
        patterns = {
            "produto": r"\*\*Produto:\*\*\s*(.+)",
            "marca": r"\*\*Marca:\*\*\s*(.+)",
            "formato": r"\*\*Formato:\*\*\s*(.+)",
            "conceito": r"\*\*Conceito:\*\*\s*(.+)",
            "png_referencia": r"\*\*PNG de Refer[eê]ncia:\*\*\s*`(.+?)`",
        }
        for attr, pattern in patterns.items():
            match = re.search(pattern, content)
            if match:
                value = match.group(1).strip()
                if attr == "conceito":
                    value = value.strip('"').strip("'")
                setattr(spec, attr, value)

    def _parse_prompt(self, content: str, spec: VDPSpec) -> None:
        """Extrai o prompt NB2 do bloco de código."""
        code_blocks = re.findall(r"```\n(.*?)```", content, re.DOTALL)
        if not code_blocks:
            code_blocks = re.findall(r"```\s*\n(.*?)```", content, re.DOTALL)

        if code_blocks:
            spec.prompt_nb2 = code_blocks[0].strip()

    def _parse_canva(self, content: str, spec: VDPSpec) -> None:
        """Extrai instruções de composição Canva."""
        canva_section = re.search(
            r"##\s*\d+\.\s*Instru[cç][oõ]es de Composi[cç][aã]o Canva(.*?)(?=##\s*\d+\.|\n---\n|\Z)",
            content,
            re.DOTALL,
        )
        if not canva_section:
            return

        section = canva_section.group(1)

        template_match = re.search(r"\*\*Template:\*\*\s*(.+)", section)
        if template_match:
            spec.canva.template = template_match.group(1).strip()

        rows = re.findall(
            r"\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|",
            section,
        )
        for key, value in rows:
            key_lower = key.lower().strip()
            value = value.strip()
            spec.canva.elements[key] = value

            if "logo" in key_lower:
                spec.canva.logo = value
            elif "headline" in key_lower:
                spec.canva.headline = value
            elif "spec line" in key_lower:
                spec.canva.spec_line = value
            elif "anvisa" in key_lower:
                spec.canva.anvisa_badge = value
            elif "gradiente topo" in key_lower:
                spec.canva.gradiente_topo = value
            elif "gradiente rodape" in key_lower or "gradiente rodapé" in key_lower:
                spec.canva.gradiente_rodape = value
            elif "margens" in key_lower or "margem" in key_lower:
                spec.canva.margens = value
            elif "zona protegida" in key_lower:
                spec.canva.zona_protegida = value

    def _parse_claims(self, content: str, spec: VDPSpec) -> None:
        """Extrai claims regulatórios da tabela."""
        claims_section = re.search(
            r"##\s*\d+\.\s*Claims Utilizados(.*?)(?=##\s*\d+\.|\n---\n|\Z)",
            content,
            re.DOTALL,
        )
        if not claims_section:
            return

        for line in claims_section.group(1).splitlines():
            match = re.match(
                r"\|\s*(\w+-\d+)\s*\|\s*(.+?)\s*\|(?:\s*(.+?)\s*\|)?$",
                line.strip(),
            )
            if match:
                claim_id = match.group(1).strip()
                texto = match.group(2).strip().strip('"')
                fonte = match.group(3).strip() if match.group(3) else ""
                spec.claims.append(Claim(claim_id=claim_id, texto=texto, fonte=fonte))

    def _parse_criterios(self, content: str, spec: VDPSpec) -> None:
        """Extrai critérios de aprovação."""
        criterios_section = re.search(
            r"##\s*\d+\.\s*Crit[eé]rios de Aprova[cç][aã]o(.*?)(?=##\s*\d+\.|\n---\n|\Z)",
            content,
            re.DOTALL,
        )
        if not criterios_section:
            return

        items = re.findall(r"-\s*\[.\]\s*(.+)", criterios_section.group(1))
        spec.criterios_aprovacao = [item.strip() for item in items]
