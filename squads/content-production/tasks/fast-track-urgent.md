# Task: Pipeline Emergencial (Fast-Track)

**Agent:** Tempo (production-manager)
**Command:** `*fast-track-urgent`
**Type:** on-demand
**SLA:** 4 horas

---

## Objetivo

Pipeline de produção acelerado para conteúdo urgente (lançamento de produto, evento, oportunidade de mercado). Comprime o ciclo semanal em ~4 horas com revisão simplificada.

## Quando Usar

- Lançamento de produto não planejado
- Evento/data relevante de última hora
- Oportunidade de trending topic no setor
- Resposta a ação de concorrente
- Solicitação comercial urgente

## Fluxo Fast-Track (4h)

```
HORA 0-1: Brief + Copy (paralelo)
  - Atlas: Brief simplificado (15 min)
  - Helix: Copy direto (45 min)
  - [HUMAN GATE] Aprovação express do usuário

HORA 1-2: Visual (paralelo com copy review)
  - Apex: VDP simplificado (30 min)
  - [HUMAN GATE] Usuário executa no AI Studio + Canva (30 min)

HORA 2-3: Review Comprimido
  - Lens: Review rápido camadas 1+2 (15 min)
  - Shield: Review express camadas 3+4 (15 min)
  - [Se bloqueio] Fix imediato (30 min)

HORA 3-4: Publicação
  - [HUMAN GATE] Usuário publica imediatamente
  - Aplicar UTMs
```

## Regras do Fast-Track

| Regra | Detalhe |
|-------|---------|
| Máximo de peças | 3 (1 master + 2 derivados essenciais) |
| Plataformas | Máx. 2 (escolher as de maior impacto) |
| Atomização | SKIP — derivados só no próximo ciclo regular |
| Compliance | NÃO skip — Shield SEMPRE revisa (mesmo express) |
| Claims | APENAS claims já aprovados no banco — zero claims novos |

## Output

```
=== FAST-TRACK COMPLETE — {Data/Hora} ===

Motivo: {urgência}
Duração: {Xh}
Peças: {N}
Plataformas: {lista}
Shield: APROVADO / BLOQUEADO
Status: Publicado / Aguardando correção
```

## Error Handling

- Se Shield bloqueia → NÃO publicar. Corrigir mesmo que atrase
- Se tempo excede 4h → Considerar publicar no próximo dia (não perde qualidade por pressa)
