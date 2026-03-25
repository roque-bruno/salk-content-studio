# Task: Orquestrar Ciclo Semanal Completo

**Agent:** Tempo (production-manager)
**Command:** `*execute-weekly-batch`
**Type:** recurring (semanal)
**PRD:** FR-007

---

## Objetivo

Orquestrar o ciclo completo de produção semanal (Seg-Sex), ativando cada agente na sequência correta e coordenando handoffs entre eles. Este é o "maestro" do pipeline.

## Fluxo Semanal

```
SEGUNDA (Copy Day):
  1. Atlas → *create-editorial-calendar (se não existe para a semana)
  2. Atlas → *create-weekly-briefs
  3. [HUMAN GATE] Usuário aprova briefs
  4. Helix → *write-batch-copy
  4.5 Lens → *review-copy-intermediate (NOVO — reduz retrabalho)
  [HUMAN GATE] Usuário aprova copies
  OUTPUT: Copy sets aprovados

TERÇA (Visual Day):
  5. Apex → *create-visual-delivery-pack
  6. [HUMAN GATE] Usuário executa VDPs no Google AI Studio + Canva
  OUTPUT: Composições visuais prontas

QUARTA (Atomização):
  7. Nova → *atomize-master-piece (para cada peça-mãe)
  8. [HUMAN GATE] Usuário cria derivados no Canva (resize, adapta)
  OUTPUT: Derivados cross-platform

QUINTA (Review):
  9. Lens → *review-batch-editorial (camadas 1+2)
  10. Shield → *review-batch-compliance (camadas 3+4) — BLOCKING
  11. [Se correções] → Loop de fix com Helix/Apex
  OUTPUT: Batch aprovado

SEXTA (Publicação):
  12. [HUMAN GATE] Usuário agenda manualmente
      - Meta Business Suite (Instagram + Facebook)
      - LinkedIn
      - YouTube Studio
  13. Aplicar UTMs de data/utm-patterns.yaml
  OUTPUT: 2 semanas de conteúdo agendado
```

## Human Gates

| Gate | Quando | Quem |
|------|--------|------|
| Aprovação de briefs | Após Atlas gerar | Usuário |
| Execução visual | Após Apex gerar VDPs | Usuário (AI Studio + Canva) |
| Criação de derivados | Após Nova mapear | Usuário (Canva resize) |
| Publicação | Após Shield aprovar | Usuário (scheduling) |

## Métricas do Ciclo

| Métrica | Target |
|---------|--------|
| Duração total | ≤ 5 dias úteis (Seg-Sex) |
| Peças no pipeline | ≥ 10 masters + derivados |
| First-pass rate (Shield) | ≥ 70% |
| Compliance violations | 0 |

## Output

Status report ao final do ciclo:

```
=== WEEKLY BATCH COMPLETE — {Semana} ===

Início: {Segunda}
Fim: {Sexta}
Duração: {dias}

Produção:
- Masters produzidos: {N}
- Derivados gerados: {N}
- Total de peças: {N}

Qualidade:
- Aprovados first-pass (Lens): {N} ({%})
- Aprovados first-pass (Shield): {N} ({%})
- Correções necessárias: {N}
- Violations: {N}

Publicação:
- Agendados: {N}
- Plataformas cobertas: {lista}

Próximos passos:
- {recomendação 1}
- {recomendação 2}
```
