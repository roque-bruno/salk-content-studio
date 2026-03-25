# Task: Analisar Performance Semanal

**Agent:** Pulse (performance-analyst)
**Command:** `*analyze-weekly-performance`
**Type:** recurring (semanal)
**PRD:** FR-006

---

## Objetivo

Analisar métricas de performance pós-publicação e gerar insights acionáveis que alimentam Atlas (content-strategist) para otimização contínua do calendário editorial e briefings.

## Pre-Conditions

- [ ] Peças publicadas há ≥ 7 dias (para métricas estabilizarem)
- [ ] Acesso às métricas nativas (Instagram Insights, LinkedIn Analytics, YouTube Studio, Facebook Insights)
- [ ] Benchmarks definidos em `data/platform-specs.yaml`

## Inputs

| Input | Fonte | Obrigatório |
|-------|-------|:-----------:|
| Métricas nativas | Plataformas (manual) | Sim |
| Brief IDs das peças | Atlas | Sim |
| Benchmarks | PRD NFR-005 | Sim |

## Steps

1. **Coletar métricas por peça publicada:**

   | Métrica | Instagram | LinkedIn | YouTube | Facebook |
   |---------|:---------:|:--------:|:-------:|:--------:|
   | Impressões | ✅ | ✅ | ✅ | ✅ |
   | Alcance | ✅ | ✅ | ✅ | ✅ |
   | Engagement Rate | ✅ | ✅ | ✅ | ✅ |
   | Saves | ✅ | — | — | — |
   | Shares | ✅ | ✅ | ✅ | ✅ |
   | Comments | ✅ | ✅ | ✅ | ✅ |
   | Click-throughs | ✅ (bio) | ✅ | ✅ | ✅ |
   | Completion Rate | ✅ (Reels) | ✅ (vídeo) | ✅ | ✅ |
   | Dwell Time | — | ✅ | ✅ | — |

2. **Analisar por dimensão:**
   - **Por plataforma:** Qual plataforma performa melhor?
   - **Por pilar:** Produto vs Educacional vs Cases — qual engaja mais?
   - **Por formato:** Carousel vs Reel vs Post vs PDF — qual converte?
   - **Por marca:** Performance relativa entre marcas
   - **Por produto:** LEV vs KRATUS vs OSTUS — qual gera mais interesse?
   - **Por horário:** Validar horários de publicação

3. **Comparar com benchmarks:**
   - Instagram: > 4.0% engagement (benchmark healthcare: 3.89%)
   - LinkedIn: > 3.5% (benchmark: 3.61%)
   - Facebook: > 2.0% (benchmark: 2.22%)
   - YouTube: > 4% completion rate

4. **Gerar insights e recomendações:**
   - Top 3 peças da semana (por engagement)
   - Bottom 3 peças (oportunidades de melhoria)
   - Padrões identificados (formato, horário, pilar)
   - Recomendações para próxima semana

## Output

```
=== PERFORMANCE REPORT — Semana {N} ===

📊 Overview
- Total publicado: {N} peças
- Engagement médio: {%}
- Impressões totais: {N}
- Alcance total: {N}

🏆 Top 3
1. {Brief ID} — {plataforma} — {engagement%} — Motivo provável: {insight}
2. ...
3. ...

📉 Bottom 3
1. {Brief ID} — {plataforma} — {engagement%} — Hipótese: {análise}
...

📈 Insights por Dimensão
- Melhor pilar: {pilar} ({engagement médio})
- Melhor formato: {formato} ({engagement médio})
- Melhor horário: {horário}
- Melhor produto: {produto}

🎯 Recomendações para Atlas
1. Aumentar % de {pilar} no calendário (performance +{X}% vs média)
2. Priorizar formato {formato} no Instagram
3. Testar horário {X} no LinkedIn
4. Reduzir {pilar} por baixo engajamento

🔄 Feedback Loop → Atlas
{JSON ou YAML com dados estruturados para alimentar próximo calendário}
```

## Post-Conditions

- Report entregue ao usuário
- Feedback estruturado entregue para Atlas
- Métricas registradas para tracking de tendências
