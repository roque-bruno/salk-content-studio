# Task: Status Report do Pipeline

**Agent:** Tempo (production-manager)
**Command:** `*run-pipeline-status`
**Type:** on-demand
**PRD:** NFR-001

---

## Objetivo

Gerar relatório de status do pipeline de produção, mostrando onde cada peça está no fluxo, bottlenecks, e métricas de velocidade.

## Steps

1. **Coletar status por etapa:**

   | Etapa | Agente | Peças | Status |
   |-------|--------|:-----:|--------|
   | Briefing | Atlas | ? | Em andamento / Concluído |
   | Copy | Helix | ? | Pendente / Em andamento / Concluído |
   | Visual | Apex | ? | Pendente / Em andamento / Concluído |
   | Atomização | Nova | ? | Pendente / Em andamento / Concluído |
   | Revisão Editorial | Lens | ? | Pendente / Em andamento / Concluído |
   | Compliance | Shield | ? | Pendente / Em andamento / Concluído |
   | Publicação | Usuário | ? | Pendente / Agendado / Publicado |

2. **Calcular métricas:**
   - Peças totais no pipeline
   - Peças concluídas esta semana
   - Tempo médio por peça (brief → publicação)
   - Bottleneck atual (etapa com mais peças acumuladas)
   - First-pass approval rate (Shield)

3. **Identificar riscos:**
   - Peças atrasadas (> 5 dias no pipeline)
   - Etapas bloqueadas
   - Volume abaixo do target semanal

## Output

```
=== PIPELINE STATUS — {Data} ===

📊 Resumo
- Total no pipeline: {N}
- Concluídas esta semana: {N}
- Target semanal: {N}
- Progresso: {%}

⏱️ Velocidade
- Tempo médio/peça: {Xh}
- Bottleneck: {etapa} ({N} peças acumuladas)

✅ Qualidade
- First-pass rate (Shield): {%}
- Correções pendentes: {N}

⚠️ Riscos
- {risco 1}
- {risco 2}

📋 Detalhamento por Etapa
{tabela detalhada}
```

## Post-Conditions

- Status report entregue ao usuário
- Bottlenecks identificados com sugestão de ação
