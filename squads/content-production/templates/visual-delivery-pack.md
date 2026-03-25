# Visual Delivery Pack — Template de Entrega por Peça

## Uso
Template OBRIGATÓRIO para cada imagem produzida pelo squad. Criado por @visual-designer (Apex).
Toda entrega visual DEVE conter os 4 blocos abaixo — sem exceção.

---

```
═══════════════════════════════════════════════════════════════
VISUAL DELIVERY PACK
═══════════════════════════════════════════════════════════════

ID: [MARCA]-[ANO]-W[SEMANA]-[NUMERO]
Ex: SALK-2026-W16-001

── BLOCO 1: PROMPT NANO BANANA 2 ────────────────────────────

Prompt:
"""
[Prompt completo otimizado para Nano Banana 2.
 Estrutura: Sujeito → Cenário → Iluminação → Câmera → Estilo → Propósito.
 INCLUIR produto real na cena (nome do equipamento + descrição visual).
 NUNCA incluir texto ou logo no prompt.]
"""

Modelo: Nano Banana 2 (gemini-3.1-flash-image)
Aspect Ratio: [1:1 | 4:5 | 9:16 | 16:9 | 3:4]
Resolução: [1K | 2K | 4K]
Variações: [1-3 opções a gerar]

Notas técnicas:
- [Dicas específicas para este prompt, ex: "se produto ficar cortado, adicionar 'full product visible, centered'"]

── BLOCO 2: PÓS-GERAÇÃO (Tasks Padrão) ─────────────────────

□ Remover marca d'água do Google (Canva Magic Eraser ou ferramenta similar)
□ Verificar fidelidade do produto (cor, formato, proporção vs foto real)
□ Verificar se NÃO há texto gerado pela IA na imagem
□ Verificar se NÃO há logo gerado pela IA na imagem
□ Verificar se NÃO há pessoas geradas pela IA
□ Verificar qualidade geral (artefatos, distorções, bordas)

── BLOCO 3: INSTRUÇÃO DE COMPOSIÇÃO (Canva Pro) ────────────

Template Canva: [Nome/ID do template]
Dimensão final: [1080x1350 | 1080x1080 | 1080x1920 | 1200x627]

Elementos a adicionar:

  LOGO:
    Arquivo: [salk-logo-branco.png | mendel-logo.png | manager-logo.png | dayho-logo.png]
    Posição: [canto inferior direito | canto superior esquerdo | centralizado inferior]
    Tamanho: [pequeno ~8% da largura | médio ~12% | grande ~18%]
    Opacidade: [100% | 80% | 60%]
    Efeito: [nenhum | sombra sutil | glow]

  TEXTO PRINCIPAL (Headline/Hook):
    Texto: "[texto exato]"
    Posição: [topo centralizado | centro | inferior esquerdo]
    Fonte: [Montserrat Bold | Poppins SemiBold | Inter Bold]
    Tamanho: [32pt | 40pt | 48pt | 56pt]
    Cor: [#FFFFFF | #1A3A5C | #0066CC | custom HEX]
    Alinhamento: [center | left | right]
    Largura máx: [80% da largura da imagem]
    Sombra texto: [sim - 2px blur #00000050 | não]

  TEXTO SECUNDÁRIO (Subtítulo/CTA):
    Texto: "[texto exato]"
    Posição: [abaixo do título | inferior centralizado]
    Fonte: [Montserrat Regular | Poppins Regular | Inter Regular]
    Tamanho: [18pt | 22pt | 26pt]
    Cor: [#FFFFFF | #CCCCCC | custom HEX]
    Alinhamento: [center | left]

  CTA BADGE (se aplicável):
    Texto: "[Saiba mais | Agende demonstração | Conheça]"
    Formato: [pill button | rectangle | underline]
    Cor fundo: [#0066CC | #FF6600 | custom HEX]
    Cor texto: [#FFFFFF]
    Posição: [inferior centralizado | inferior direito]

  ELEMENTOS EXTRAS:
    - [Barra de cor na borda superior: #0066CC, 4px]
    - [Selo "Registro ANVISA" canto inferior esquerdo]
    - [QR code para link na bio — posição: inferior direito, 80x80px]

── BLOCO 4: METADADOS DA PEÇA ──────────────────────────────

Marca: [Salk Medical | Mendel Medical | Manager Grupo | Dayho]
Produto: [LEV | KRATUS | OSTUS | KRONUS | COMMAND | Institucional]
Plataforma: [Instagram Feed | Instagram Story | LinkedIn | Facebook | YouTube]
Pilar: [Produto | Educacional | Cases | Bastidores | Thought Leadership]
Persona alvo: [Compras | Eng. Clínica | Equipe Médica | Administradores]
Funil: [Awareness | Consideração | Avaliação | Decisão]
Copy associado: [ID do copy — ex: SALK-2026-W16-001-COPY]
Claims utilizados: [LEV-01, LEV-05 | nenhum]

═══════════════════════════════════════════════════════════════
```

---

## Regras Inegociáveis

1. **NUNCA** incluir texto no prompt de IA — texto é adicionado no Canva
2. **NUNCA** incluir logo no prompt de IA — logo é adicionado no Canva
3. **SEMPRE** incluir o produto real no prompt (Nano Banana 2 integra produto na cena com sombras, reflexos e composição de cor natural)
4. **SEMPRE** remover marca d'água do Google como primeira task pós-geração
5. **SEMPRE** especificar TODOS os detalhes de composição (posição, fonte, tamanho, cor HEX) — nada subjetivo
6. **SEMPRE** verificar fidelidade do produto antes de compor
