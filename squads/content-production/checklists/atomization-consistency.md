# Checklist: Consistência de Atomização Cross-Platform

**Agente:** Lens (quality-editor) + Nova (content-atomizer)
**Uso:** Verificar consistência entre derivados de uma mesma peça-mãe
**PRD:** FR-005

---

## Checklist por Grupo de Derivados

### Rastreabilidade
- [ ] Todos os derivados referenciam o Brief ID da peça-mãe
- [ ] Mapa de atomização documentado (master → derivados)
- [ ] Total de derivados ≥ 10 (ou ≥ 5 para posts simples)

### Claims (Consistência)
- [ ] Mesmos claim IDs usados em todos os derivados
- [ ] Nenhum derivado adiciona claims que não estão na peça-mãe
- [ ] Versão acessível e técnica dos claims usadas adequadamente por plataforma

### Mensagem-Core
- [ ] Mensagem principal é a mesma em todos os derivados
- [ ] Ângulo/perspectiva pode variar, mas o benefício central é consistente
- [ ] Produto referenciado é o mesmo

### Adaptação por Plataforma
- [ ] NENHUM derivado é cópia idêntica de outro (zero cross-post)
- [ ] Tom adaptado por plataforma:
  - LinkedIn: técnico (8/10)
  - Instagram Feed: visual/acessível (5/10)
  - Instagram Reels/Stories: dinâmico (3/10)
  - YouTube: educativo (4-7/10)
  - Facebook: conversacional (4/10)
- [ ] Char limits respeitados por plataforma
- [ ] Dimensões corretas por plataforma

### CTAs
- [ ] CTAs diferenciados por plataforma:
  - Instagram: "Link na bio" / "Salve"
  - LinkedIn: "Comente FICHA" / "Link no comentário"
  - YouTube: "Se inscreva" / "Link na descrição"
  - Facebook: "Compartilhe" / "Comente"
- [ ] Nenhum CTA repetido identicamente entre plataformas

### Hashtags
- [ ] Hashtags adequadas por plataforma (IG=11, LI=3-5)
- [ ] Hashtags do banco (`hashtag-bank.yaml`)
- [ ] Core hashtags da marca presentes em todos

### Cobertura
- [ ] Cada plataforma ativa da marca tem ≥ 1 derivado
- [ ] Mix de formatos presente (não todos iguais)
- [ ] Formatos prioritários priorizados (IG: Reels > Carousel > Post)

---

## Scoring

| Score | Decisão |
|:-----:|---------|
| Todos ✅ | Batch aprovado para review de compliance |
| 1-2 falhas não-críticas | Correção rápida e segue |
| Claim inconsistente | BLOQUEAR — corrigir antes de avançar |
| Cross-post detectado | BLOQUEAR — adaptar obrigatoriamente |
