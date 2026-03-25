# Task: Escrever Copy para Batch de Briefs

**Agent:** Helix (medical-copywriter)
**Command:** `*write-batch-copy`
**Type:** recurring (semanal)
**PRD:** FR-002, FR-009, FR-010, FR-011
**Depends on:** `create-weekly-briefs.md`

---

## Objetivo

Escrever copy profissional para todos os briefs aprovados do batch semanal, respeitando tom de voz por marca, nível técnico por plataforma, frameworks de copy selecionados, e usando EXCLUSIVAMENTE claims do banco pré-aprovado.

## Pre-Conditions

- [ ] Batch de briefs aprovado por Atlas
- [ ] `data/claims-bank.yaml` disponível
- [ ] `data/brand-guidelines.yaml` disponível (tom de voz)
- [ ] `data/buyer-personas.yaml` disponível
- [ ] `data/platform-specs.yaml` disponível (char limits, nível técnico)
- [ ] `data/prohibited-terms.yaml` disponível

## Inputs

| Input | Fonte | Obrigatório |
|-------|-------|:-----------:|
| Batch de briefs aprovados | Output de `create-weekly-briefs` | Sim |
| Claims bank | `data/claims-bank.yaml` | Sim |
| Termos proibidos | `data/prohibited-terms.yaml` | Sim |

## Steps

1. **Para cada brief do batch:**

   a. **Aplicar framework selecionado:**
      - PAS → Problema > Agitação > Solução
      - AIDA → Atenção > Interesse > Desejo > Ação
      - BAB → Antes > Depois > Ponte
      - SPIN → Situação > Problema > Implicação > Necessidade

   b. **Escrever copy por formato:**
      - **Carousel (IG):** Capa (hook) + 8-9 slides de conteúdo + CTA final
      - **Post (IG):** Caption 300-500 chars + hashtags
      - **Reel script:** Hook (0-3s) + Conteúdo (3-20s) + CTA (20-30s)
      - **LinkedIn texto:** Hook forte → contexto → insight → CTA (1.500-3.000 chars)
      - **LinkedIn PDF:** Capa + slides + CTA (8-12 páginas, texto por slide)
      - **YouTube script:** Intro + conteúdo + CTA + descrição
      - **Facebook:** Post conversacional 80-100 chars

   c. **Verificação automática por peça:**
      - [ ] Claims usados existem no banco (IDs válidos)?
      - [ ] Nenhum termo proibido (`prohibited-terms.yaml`)?
      - [ ] Tom de voz correto para a marca?
      - [ ] Nível técnico adequado para a plataforma?
      - [ ] Char limit respeitado?
      - [ ] CTA incluso e adequado?
      - [ ] Hashtags no formato correto?

2. **Auto-revisão do batch:**
   - Verificar consistência entre peças do mesmo produto
   - Verificar variação (não repetir hooks/estruturas)
   - Verificar que versões acessíveis dos claims são usadas no IG (não termos técnicos puros)

3. **Entregar batch para Apex (visual) e Lens (revisão)**

## Output

Para cada brief, entregar:

```
=== COPY SET — {Brief ID} ===

HEADLINE/HOOK: "..."
CORPO: "..."
CTA: "..."
HASHTAGS: "..."
CLAIMS UTILIZADOS: [LEV-01, LEV-06]

--- Notas para Apex (visual) ---
Sugestão visual: "..."
Texto overlay: "..."
```

## Post-Conditions

- Copy para todos os briefs entregue
- Claims rastreáveis (IDs listados por peça)
- Zero termos proibidos
- Pronto para `*create-visual-delivery-pack` (Apex) e `*review-batch-editorial` (Lens)

## Error Handling

- Se brief requer claim que não existe → NÃO inventar. Sinalizar e pular, ou usar versão genérica institucional
- Se char limit é excedido → Condensar mantendo claims core e CTA
