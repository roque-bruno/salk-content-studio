# Epic 16: DRY Refactor — Eliminacao de Duplicacoes

**Status:** Done
**PRD:** docs/prd/PRD-DRY-REFACTOR.md
**Agente Lead:** @dev (Dex)
**QA:** @qa (Quinn)
**Arquitetura:** @architect (Aria)

---

## Stories

| # | Story | Agente | Status | Prioridade |
|---|-------|--------|--------|------------|
| 16.1 | Extrair constantes e defaults | @dev | DONE | P0 - Base |
| 16.2 | Funcoes utilitarias backend | @dev | DONE | P0 - Base |
| 16.3 | Consolidar endpoints de imagem | @dev | DONE | P1 - Critico |
| 16.4 | Consolidar endpoints de briefing/copy/prompt | @dev | DONE | P1 - Critico |
| 16.5 | Unificar pipeline de producao | @dev | DEFERRED | P1 - Critico |
| 16.6 | Endpoint factory para dados GET/PUT | @dev | DONE | P2 - Medio |
| 16.7 | Consolidar funcoes frontend | @dev | DONE | P1 - Critico |
| 16.8 | QA Gate — validacao completa | @qa | DONE | P0 - Final |

## Ordem de Execucao

```
16.1 (constantes) ──┐
                     ├──→ 16.3 (imagem) ──┐
16.2 (utils)     ──┘     16.4 (brief)  ──├──→ 16.5 (pipeline) ──→ 16.8 (QA)
                          16.6 (data)   ──┘
                          16.7 (front)  ──┘
```

Stories 16.1 e 16.2 sao pre-requisitos (criam a infraestrutura).
Stories 16.3-16.7 podem ser executadas em paralelo apos 16.1+16.2.
Story 16.8 e o gate final.

## Metodo de Qualidade: Snapshot Testing

**Antes de cada story:**
1. Capturar response de cada endpoint afetado (curl + save JSON)
2. Capturar comportamento frontend (quais funcoes chamam quais endpoints)

**Depois de cada story:**
3. Comparar responses — devem ser identicas
4. Testar fluxo E2E: criar peca → copy → prompt → imagem
5. Verificar logs no servidor (sem erros novos)
