# Task: Revisão Editorial em Batch (Camadas 1+2)

**Agent:** Lens (quality-editor)
**Command:** `*review-batch-editorial`
**Type:** recurring (semanal)
**PRD:** FR-004 (camadas 1+2)
**Depends on:** `write-batch-copy.md` ou `atomize-master-piece.md`

---

## Objetivo

Executar revisão editorial completa em batch de peças (camadas 1 e 2 do QC), verificando gramática, tom de voz, brand consistency, adequação ao brief, specs técnicos, e consistência entre peças atomizadas.

## Pre-Conditions

- [ ] Peças prontas para revisão (copy + visual)
- [ ] `data/brand-guidelines.yaml` disponível
- [ ] `data/claims-bank.yaml` disponível
- [ ] `data/prohibited-terms.yaml` disponível
- [ ] `data/platform-specs.yaml` disponível
- [ ] `checklists/copy-quality.md` disponível

## Steps

### Camada 1 — Verificação Automatizada (por peça)

- [ ] Ortografia e gramática corretas (pt-BR)
- [ ] Brand guidelines: cores, fontes, logo na posição correta
- [ ] Dimensões corretas para a plataforma
- [ ] Claims utilizados existem no banco (IDs válidos)
- [ ] Nenhum termo de `prohibited-terms.yaml` encontrado
- [ ] Char limit respeitado por plataforma
- [ ] Hashtags na quantidade correta

### Camada 2 — Revisão Editorial (por peça)

- [ ] Tom de voz correto para a marca (Salk=consultivo, Mendel=técnico, Manager=acolhedor, Dayho=industrial)
- [ ] Qualidade do copy: clareza, persuasão, hook eficiente
- [ ] Adequação ao briefing original (pilar, produto, persona, objetivo)
- [ ] CTA claro e adequado à etapa do funil
- [ ] Legibilidade mobile (fontes 24pt+ em visual, texto não truncado)
- [ ] Consistência entre peças atomizadas (mesma mensagem-core, mesmos claims)
- [ ] Nível técnico adequado para a plataforma (LI=8/10, IG=5/10, FB=4/10)

### Resultado por peça

Para cada peça, emitir veredito:

| Veredito | Ação |
|----------|------|
| **APROVADO** | Avança para Shield (compliance) se tem claims técnicos |
| **CORREÇÃO MENOR** | Helix corrige (typo, hashtag, formato) — não bloqueia |
| **CORREÇÃO MAIOR** | Helix reescreve seção — bloqueia até correção |
| **REJEITADO** | Reescrever do zero — não atende ao brief |

### Feedback Construtivo

Para cada correção, SEMPRE incluir:
- O que está errado
- Por que está errado
- Como corrigir (exemplo concreto)

## Output

```
=== EDITORIAL REVIEW — Batch {Semana} ===

Total peças: {N}
Aprovadas: {N} ({%})
Correção menor: {N}
Correção maior: {N}
Rejeitadas: {N}

--- Peça {Brief ID} ---
Veredito: APROVADO / CORREÇÃO MENOR / CORREÇÃO MAIOR / REJEITADO
Camada 1: ✅ / ❌ {detalhes}
Camada 2: ✅ / ❌ {detalhes}
Correções:
  1. [Tom de voz] "..." → Sugestão: "..."
  2. [Claim] Claim LEV-19 não existe no banco → Usar LEV-01
Encaminhar para Shield: Sim/Não
```

## Post-Conditions

- Peças aprovadas prontas para `*review-batch-compliance` (Shield)
- Peças com correção devolvidas para Helix/Apex
- Relatório de padrões de erro (para calibragem futura)

## Error Handling

- Se > 30% das peças rejeitadas → Escalar para Atlas, possível problema no briefing
- Se tom de marca inconsistente por 3+ peças → Sessão de calibragem com Helix
