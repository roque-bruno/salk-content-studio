# Task: Criar Visual Delivery Packs

**Agent:** Apex (visual-designer)
**Command:** `*create-visual-delivery-pack`
**Type:** recurring (semanal)
**PRD:** FR-003
**Depends on:** `write-batch-copy.md`

---

## Objetivo

Gerar Visual Delivery Packs (VDPs) completos para cada peça do batch. Cada VDP contém: prompt NB2 para geração de cenário, instruções de composição, texto overlay, metadata de dimensões, e referências de marca.

## Pre-Conditions

- [ ] Copy aprovado de Helix disponível
- [ ] `data/brand-guidelines.yaml` disponível
- [ ] `data/platform-specs.yaml` disponível
- [ ] `templates/visual-delivery-pack.md` disponível
- [ ] PNGs dos produtos disponíveis (fotos reais)

## Inputs

| Input | Fonte | Obrigatório |
|-------|-------|:-----------:|
| Copy sets aprovados | Output de `write-batch-copy` | Sim |
| Brand guidelines | `data/brand-guidelines.yaml` | Sim |
| Platform specs | `data/platform-specs.yaml` | Sim |
| VDP template | `templates/visual-delivery-pack.md` | Sim |

## Steps

1. **Para cada peça do batch:**

   a. **Gerar prompt NB2 (Nano Banana):**
      - Cenário profissional adequado ao produto
      - Estilo: clean, médico, showroom, hospitalar moderno
      - SEM pessoas, SEM procedimentos clínicos
      - Iluminação suave, fundo neutro ou contextualizado
      - Resolução: 4K, fotorrealista

      Exemplo:
      ```
      Professional medical showroom, clean white environment,
      soft LED lighting, modern hospital corridor background,
      no people, empty room, photorealistic, 4K, shallow depth of field
      ```

   b. **Instruções de composição:**
      - Posição do produto no frame (centro, regra dos terços)
      - Escala relativa ao cenário
      - Sombras e reflexos necessários
      - Ângulo do produto (frontal, 3/4, perspectiva)

   c. **Overlay de texto:**
      - Headline (posição, tamanho fonte, cor)
      - Claims/specs (posição, tamanho)
      - CTA (posição, estilo de botão)
      - Logo (posição conforme brand-guidelines)
      - Badge ANVISA (se aplicável)

   d. **Metadata técnico:**
      - Dimensões exatas por plataforma
      - Formato de exportação (JPG/PNG)
      - Variantes necessárias (4:5 + 1:1 + 9:16)

   e. **Referências de marca:**
      - Cores HEX a usar
      - Tipografia
      - Template Canva a aplicar

2. **Validar batch de VDPs:**
   - [ ] Cada VDP tem prompt NB2 completo?
   - [ ] Instruções de composição claras para execução no Canva?
   - [ ] Dimensões corretas por plataforma?
   - [ ] Brand guidelines respeitadas (cores, logo, fonte)?
   - [ ] Nenhum VDP pede pessoas IA ou cena clínica IA?

3. **Entregar VDPs para execução pelo usuário**

## Output

Para cada peça:

```
=== VISUAL DELIVERY PACK — {Brief ID} ===

## 1. Prompt NB2 (Google AI Studio / Gemini)
"..."

## 2. Composição (Canva)
- Produto: {nome} — usar PNG: {arquivo}
- Posição: {centro/regra dos terços}
- Ângulo: {frontal/3-4/perspectiva}
- Escala: {proporção no frame}

## 3. Texto Overlay
- Headline: "{texto}" — {posição}, {tamanho}pt, {cor HEX}
- Spec: "{texto}" — {posição}, {tamanho}pt
- CTA: "{texto}" — {posição}, estilo botão
- Logo: {posição conforme brand guidelines}

## 4. Exportação
- Instagram Feed: 1080x1350 (4:5) — JPG
- LinkedIn: 1200x1200 (1:1) — JPG
- Stories/Reels: 1080x1920 (9:16) — JPG

## 5. Template Canva
- Template: {ID/nome do template}
```

## Post-Conditions

- VDPs prontos para execução no Google AI Studio + Canva
- Usuário pode executar cada VDP de forma autônoma
- Pronto para `*review-batch-editorial` (Lens) após produção visual

## Error Handling

- Se PNG do produto não disponível → Sinalizar, sugerir produto alternativo ou pular peça
- Se formato requer vídeo → Gerar VDP estático + nota para futuro Flux
