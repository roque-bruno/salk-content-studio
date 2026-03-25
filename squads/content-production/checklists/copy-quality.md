# Checklist: Qualidade de Copy

**Agente:** Lens (quality-editor) + Helix (medical-copywriter)
**Uso:** Verificação de qualidade de cada peça de copy antes da revisão visual

---

## Checklist por Peça

### Fundamentos (obrigatório)
- [ ] Ortografia e gramática corretas (pt-BR)
- [ ] Sem erros de digitação
- [ ] Pontuação adequada
- [ ] Acentuação correta

### Tom de Voz
- [ ] Tom correto para a marca:
  - Salk: Consultivo, confiante, orientado a resultados
  - Mendel: Técnico, preciso, autoritativo
  - Manager: Acolhedor, institucional, inspirador
  - Dayho: Industrial, técnico, sólido
- [ ] Nível técnico adequado para a plataforma (IG=5/10, LI=8/10, FB=4/10, YT=4-7/10)
- [ ] Vocabulário consistente com a persona alvo

### Claims e Compliance
- [ ] TODOS os claims têm ID válido no banco (`claims-bank.yaml`)
- [ ] Nenhum claim inventado
- [ ] Nenhum termo proibido de `prohibited-terms.yaml`
- [ ] Sem superlativos ("o melhor", "o único", "garante")
- [ ] Sem comparativo direto com concorrente nomeado
- [ ] Dados técnicos verificáveis contra manuais

### Estrutura e Formato
- [ ] Hook forte nos primeiros 3 segundos (vídeo) ou primeira frase (texto)
- [ ] Framework de copy aplicado corretamente (PAS/AIDA/BAB/SPIN)
- [ ] CTA claro e adequado à etapa do funil
- [ ] Char limit respeitado por plataforma
- [ ] Hashtags na quantidade correta (IG=11, LI=3-5)

### Adequação ao Brief
- [ ] Mensagem principal alinhada com o brief
- [ ] Pilar de conteúdo correto
- [ ] Produto correto
- [ ] Persona alvo atendida
- [ ] Objetivo de funil respeitado (awareness/consideração/conversão)

### Consistência (para derivados)
- [ ] Mesmos claims (IDs) que a peça-mãe
- [ ] Mensagem-core consistente entre derivados
- [ ] CTAs diferenciados por plataforma (não repetidos)

---

## Vereditos

| Resultado | Critério |
|-----------|----------|
| **APROVADO** | Todos os itens obrigatórios ✅ |
| **CORREÇÃO MENOR** | 1-2 itens não-críticos faltando |
| **CORREÇÃO MAIOR** | Claim inválido, tom errado, ou violação de compliance |
| **REJEITADO** | Múltiplas violações ou não atende ao brief |
