# Epico 1 — Calibracao & Primeiro Batch Real (Salk/Mendel)

**PRD:** docs/prd/PRD-content-production.md v2.0
**Status:** Em Execucao
**Inicio:** 2026-03-25
**Duracao Estimada:** 3 semanas (Semanas 2-4)
**Owner:** Orion (aiox-master) — orquestracao / @pm (Morgan) — gestao

---

## Objetivo

Calibrar qualidade do sistema em pecas individuais, validar pipeline end-to-end, e produzir primeiro batch real com 5 masters + derivados por semana para Salk Medical e Mendel Medical.

## Principio

> **Qualidade > Volume. Testar antes de escalar. 30 pecas a 9.0 > 60 pecas a 6.0.**

---

## Fases

### Fase 1: Preparacao & Pre-Requisitos (Stories 1.1-1.3)

**Objetivo:** Resolver todos os bloqueadores identificados na reuniao do squad antes de iniciar producao.

| Story | Titulo | Executor | Dependencia |
|-------|--------|----------|-------------|
| 1.1 | Atualizar PRD, squad.yaml e data files para v2.0 | @dev (Dex) | — |
| 1.2 | Preparar assets visuais (PNGs recortados, paleta HEX) | Usuario + Apex | 1.1 |
| 1.3 | Calibrar NB2 com hero shots individuais (LEV + KRATUS) | Apex + Usuario | 1.2 |

### Fase 2: Pipeline Validacao (Stories 1.4-1.5)

**Objetivo:** Validar pipeline completo end-to-end com 1 peca antes de escalar.

| Story | Titulo | Executor | Dependencia |
|-------|--------|----------|-------------|
| 1.4 | Executar pipeline completo com 1 peca LEV (end-to-end) | Squad completo | 1.3 |
| 1.5 | Review e ajuste do pipeline baseado na peca piloto | @qa (Quinn) + Squad | 1.4 |

### Fase 3: Primeiro Batch (Stories 1.6-1.8)

**Objetivo:** Produzir primeiro batch real com pipeline validado.

| Story | Titulo | Executor | Dependencia |
|-------|--------|----------|-------------|
| 1.6 | Produzir batch Semana 1: 5 masters + derivados | Squad completo | 1.5 |
| 1.7 | Publicar e coletar metricas do batch Semana 1 | Usuario + Pulse | 1.6 |
| 1.8 | Retrospectiva e otimizacao para escala | @sm (River) + Squad | 1.7 |

---

## Pre-Requisitos Bloqueantes

- [ ] Product PNGs recortados (LEV, KRATUS) com fundo transparente
- [ ] Teste NB2 aprovado pelo usuario (hero shot LEV + KRATUS)
- [ ] Templates Canva base criados
- [ ] Paleta de cores HEX confirmada por marca
- [ ] claims-bank.yaml limpo (sem ETRUS, sem inconsistencias)
- [ ] Pipeline testado end-to-end com 1 peca

## Success Metrics

| Metrica | Target Fase 1 | Target Fase 3 |
|---------|:-------------:|:-------------:|
| Hero shots NB2 aprovados | >= 2 | N/A |
| Pipeline end-to-end | 1 peca | 5+ pecas/sem |
| Qualidade visual | 100% aprovacao | >= 80% |
| Compliance | 0 violacoes | 0 violacoes |
| Derivados/master | N/A | 5-8 |
| Engagement 7d | N/A | IG>2%, LI>1.5% |

---

## Riscos do Epico

| Risco | Mitigacao |
|-------|-----------|
| PNGs nao disponiveis com transparencia | Photoroom API ou recorte manual; iniciar com imagens que ja tem fundo limpo |
| NB2 nao atinge qualidade | Iterar prompts (V2, V3...); tecnica Dramatic Studio validada para LEV |
| Pipeline lento demais | Identificar gargalos na peca piloto (Story 1.4-1.5) antes de escalar |
| Copy generico demais | Review intermediario Lens impede que copy fraco chegue ao visual |

---

**Epico 1 — Definido 2026-03-25 por Orion (aiox-master)**
