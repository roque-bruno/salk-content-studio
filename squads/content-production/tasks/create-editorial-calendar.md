# Task: Criar Calendário Editorial Semanal

**Agent:** Atlas (content-strategist)
**Command:** `*create-editorial-calendar`
**Type:** recurring (semanal)
**PRD:** FR-008

---

## Objetivo

Criar calendário editorial semanal para uma ou mais marcas, distribuindo conteúdo nos pilares corretos, plataformas adequadas e frequências definidas.

## Pre-Conditions

- [ ] `data/editorial-calendar-template.yaml` disponível
- [ ] `data/brand-guidelines.yaml` disponível (pilares por marca)
- [ ] `data/platform-specs.yaml` disponível (frequências)
- [ ] Semana-alvo definida (ex: 2026-W16)
- [ ] Marca(s) definida(s)

## Inputs

| Input | Fonte | Obrigatório |
|-------|-------|:-----------:|
| Semana-alvo | Usuário | Sim |
| Marca(s) | Usuário (default: Salk Medical) | Sim |
| Datas sazonais | `data/editorial-calendar-template.yaml` | Não |
| Feedback de performance | Pulse (se disponível) | Não |

## Steps

1. **Carregar dados de referência:**
   - Ler `data/brand-guidelines.yaml` → pilares e % por marca
   - Ler `data/platform-specs.yaml` → frequências e formatos
   - Ler `data/editorial-calendar-template.yaml` → slots e targets
   - Verificar datas sazonais na semana-alvo

2. **Distribuir conteúdo nos slots:**
   - Preencher slots diários respeitando:
     - Frequência por plataforma (Salk: 5x/semana IG, 5x LI, 3x YT, 3x FB)
     - Proporção de pilares (Produto 30%, Educacional 25%, Cases 20%, etc.)
     - Rotação de produtos (LEV, KRATUS, OSTUS, KRONUS, COMMAND)
     - Horários ideais por plataforma

3. **Gerar brief IDs:**
   - Formato: `{MARCA}-{ANO}-W{SEMANA}-{NUMERO}`
   - Ex: SALK-2026-W16-001

4. **Validar calendário:**
   - [ ] Todos os slots preenchidos?
   - [ ] Proporção de pilares respeitada (~±5%)?
   - [ ] Sem produto repetido em dias consecutivos?
   - [ ] Datas sazonais aproveitadas?
   - [ ] Mix de formatos adequado (Reels > Carousel > Post)?

5. **Apresentar para aprovação do usuário**

## Output

Calendário semanal preenchido no formato:

```
## Calendário Editorial — {Marca} — {Semana}

### Segunda (Copy Day)
| # | Plataforma | Formato | Pilar | Produto | Brief ID | Horário |
|---|-----------|---------|-------|---------|----------|---------|
| 1 | Instagram Feed | Carousel 4:5 | Educacional | LEV | SALK-2026-W16-001 | 11h |
...

### Terça (Visual Day)
...
```

## Post-Conditions

- Calendário aprovado pelo usuário
- Brief IDs gerados e prontos para `*create-weekly-briefs`
- Nenhum slot vazio na semana

## Error Handling

- Se feedback de Pulse indica pilar com baixo engagement → Reduzir proporção, aumentar pilar de melhor performance
- Se data sazonal cai na semana → Substituir 1 slot por conteúdo sazonal
