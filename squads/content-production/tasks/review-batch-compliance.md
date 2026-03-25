# Task: Revisão de Compliance em Batch (Camadas 3+4) — BLOCKING

**Agent:** Shield (compliance-guardian)
**Command:** `*review-batch-compliance`
**Type:** recurring (semanal)
**PRD:** FR-004 (camadas 3+4), CON-003
**Depends on:** `review-batch-editorial.md`
**BLOCKING:** Nenhuma peça é publicada sem aprovação desta task

---

## Objetivo

Executar revisão de compliance ANVISA/CFM em batch de peças aprovadas editorialmente por Lens (camadas 3 e 4 do QC). Esta é a última barreira antes da publicação. Gate BLOQUEANTE — peça que não passa, NÃO publica.

## Pre-Conditions

- [ ] Peças aprovadas por Lens (camadas 1+2)
- [ ] `data/claims-bank.yaml` disponível
- [ ] `data/prohibited-terms.yaml` disponível
- [ ] Referências regulatórias atualizadas

## Regulatory References

| Regulamentação | Escopo |
|----------------|--------|
| RDC 96/2008 | Publicidade de dispositivos médicos |
| RDC 751/2022 | Registro e cadastro de dispositivos |
| RDC 848/2024 | Atualizações regulatórias |
| CFM Res. 2.336/2023 | Publicidade médica |
| CONAR | Código de autorregulamentação publicitária |

## Steps

### Camada 3 — Revisão Técnica/Médica (por peça)

- [ ] Precisão de claims clínicos — cada dado confere com manual/registro ANVISA
- [ ] IDs dos claims são válidos no `claims-bank.yaml`
- [ ] Dados e estatísticas verificáveis (fonte citável)
- [ ] Terminologia médica correta e contextualizada
- [ ] Sem claims inventados ou exagerados (Article IV)
- [ ] Versão acessível dos claims é factualmente correta

### Camada 4 — Revisão Legal/Compliance (por peça)

- [ ] Conformidade com ANVISA (RDC 96/2008, 751/2022, 848/2024)
- [ ] Nenhum superlativo proibido ("o melhor", "o único", "garante")
- [ ] Nenhum comparativo direto depreciativo (sem nomes de concorrentes)
- [ ] Disclaimers obrigatórios presentes onde necessário
- [ ] Imagem do produto é foto REAL (não gerada por IA)
- [ ] Cenário NÃO sugere procedimento clínico com paciente
- [ ] Sem pessoas geradas por IA
- [ ] Cores e aparência do produto correspondem ao real
- [ ] Certificações exibidas são válidas e atuais
- [ ] Sem urgência falsa ou promessas de resultado
- [ ] Conformidade CFM (sem implicar resultado cirúrgico)

### Resultado por peça

| Veredito | Ação | Severidade |
|----------|------|:----------:|
| **APROVADO** | Pode publicar | — |
| **APROVADO COM NOTA** | Pode publicar com ajuste menor (disclaimer, nota) | Baixa |
| **BLOQUEADO** | NÃO publica até correção | ALTA |
| **REJEITADO** | Reescrever — violation grave | CRÍTICA |

### Para cada bloqueio, incluir:

- Regulamentação violada (RDC/CFM + artigo)
- O que está errado (citação exata)
- Como corrigir (sugestão específica)
- Severidade (alta/crítica)

## Output

```
=== COMPLIANCE REVIEW — Batch {Semana} ===

Total peças: {N}
APROVADO: {N} ({%})
APROVADO COM NOTA: {N}
BLOQUEADO: {N}
REJEITADO: {N}

First-pass approval rate: {%} (target: ≥ 70%)

--- Peça {Brief ID} ---
Veredito: APROVADO / APROVADO COM NOTA / BLOQUEADO / REJEITADO
Camada 3 (Técnica): ✅ / ❌
Camada 4 (Legal): ✅ / ❌
Violations:
  1. [RDC 96/2008 Art. X] Claim "o melhor foco do Brasil" — superlativo proibido
     Correção: "Referência em qualidade de iluminação cirúrgica"
     Severidade: ALTA
```

## Post-Conditions

- Peças APROVADAS prontas para publicação
- Peças BLOQUEADAS devolvidas para Helix/Apex com instruções de correção
- Registro de violations para análise de tendências
- First-pass approval rate registrado

## Error Handling

- Se claim não encontrado no banco → BLOQUEAR imediatamente
- Se imagem suspeita de alteração IA → BLOQUEAR, solicitar PNG original
- Se first-pass rate < 50% → Escalar para Atlas, problema sistêmico no briefing/copy
