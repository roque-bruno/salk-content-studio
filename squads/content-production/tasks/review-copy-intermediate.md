# Task: Review Intermediário de Copy (Antes do Design)

**Agent:** Lens (quality-editor)
**Command:** `*review-copy-intermediate`
**Type:** recurring (semanal — após copy, antes de design)
**PRD:** FR-005

---

## Objetivo

Revisar copies ANTES de enviar para Apex (design), evitando que VDPs sejam criados para copies que serão reprovados. Reduz retrabalho estimado em 30%.

## Quando

- **Pipeline normal:** Segunda-feira após Helix entregar batch de copies
- **Fast-track:** Imediatamente após copy, antes de qualquer produção visual

## Escopo (Review Leve — NÃO é o review completo de quinta-feira)

Verificar APENAS:
1. [ ] Hook é forte o suficiente? (teste de 3 segundos)
2. [ ] Conceito criativo de Atlas está refletido?
3. [ ] Claims utilizados existem no banco (IDs válidos)?
4. [ ] Tom correto para marca + persona?
5. [ ] CTA presente e adequado?
6. [ ] Produtos não lançados (ETRUS) não mencionados?
7. [ ] Nenhum superlativo proibido?

## NÃO verificar agora (fica para quinta-feira)

- Ortografia detalhada
- Brand guidelines visuais
- Compliance ANVISA completo (Shield faz na quinta)
- Cross-platform consistency (Nova ainda não atomizou)

## Output

```
COPY INTERMEDIATE REVIEW — {Semana}

Total copies: {N}
Aprovados: {N} ({%}) → seguem para Apex
Devolvidos: {N} ({%}) → voltam para Helix com feedback

Feedback consolidado:
- {issue 1}: {N} copies afetados → {ação}
- {issue 2}: {N} copies afetados → {ação}
```

## Decisão

- **≥80% aprovados:** Pipeline segue normalmente
- **60-80% aprovados:** Helix corrige e Lens re-review no mesmo dia
- **<60% aprovados:** PARAR. Reunir com Atlas para re-briefar. Problema provavelmente está no brief, não no copy.
