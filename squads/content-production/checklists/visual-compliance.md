# Checklist: Compliance Visual

**Agente:** Shield (compliance-guardian) + Lens (quality-editor)
**Uso:** Verificar cada composição visual antes da publicação
**PRD:** FR-003, CON-003, CON-004

---

## Checklist por Peça Visual

### Produto (CRÍTICO)
- [ ] Imagem do produto é foto REAL (PNG original, NÃO gerada por IA)
- [ ] Cores e aparência do produto correspondem ao real
- [ ] Produto não foi alterado por IA (tamanho, formato, cor)
- [ ] Produto está em escala realista no cenário

### Cenário
- [ ] Cenário NÃO sugere procedimento clínico com paciente
- [ ] Sem pessoas geradas por IA na composição
- [ ] Sem pacientes (reais ou IA) na imagem
- [ ] Cenário adequado ao contexto (showroom, hospital clean, fábrica)

### Marca
- [ ] Logo posicionado corretamente (conforme `brand-guidelines.yaml`)
- [ ] Cores HEX da marca corretas
- [ ] Tipografia correta
- [ ] Badge de certificação presente (ANVISA, se aplicável)

### Formato Técnico
- [ ] Dimensões corretas para a plataforma (conforme `platform-specs.yaml`)
- [ ] Safe zones respeitadas (Reels: 1080x1440 central)
- [ ] Texto legível em mobile (fontes ≥ 24pt)
- [ ] Contraste adequado (texto sobre imagem)
- [ ] Formato de arquivo correto (JPG/PNG)

### Texto Overlay
- [ ] Claims no overlay são do banco pré-aprovado
- [ ] Specs técnicos conferem com manuais
- [ ] Sem erros ortográficos no overlay
- [ ] CTA visível e claro

### Vídeo (se aplicável)
- [ ] Legendas incluídas
- [ ] Hook visual nos primeiros 3 segundos
- [ ] Thumbnail adequada (não clickbait de saúde)
- [ ] Duração dentro dos limites da plataforma

### Regulatório
- [ ] Certificações exibidas são válidas e atuais
- [ ] Disclaimers presentes onde necessário
- [ ] Sem emojis que banalizam saúde (caveiras, seringas, rostos doentes)
- [ ] Sem promessas visuais de resultado clínico

---

## Vereditos

| Resultado | Critério |
|-----------|----------|
| **APROVADO** | Todos os itens críticos ✅ |
| **APROVADO COM NOTA** | Ajuste menor de formato/posição |
| **BLOQUEADO** | Violação de produto IA, cenário clínico, ou claim visual inválido |
| **REJEITADO** | Múltiplas violações críticas |
