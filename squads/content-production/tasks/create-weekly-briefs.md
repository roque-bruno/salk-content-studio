# Task: Gerar Batch de Content Briefs

**Agent:** Atlas (content-strategist)
**Command:** `*create-weekly-briefs`
**Type:** recurring (semanal)
**PRD:** FR-001, FR-008
**Depends on:** `create-editorial-calendar.md`

---

## Objetivo

Gerar briefs estruturados para todos os slots do calendário editorial semanal aprovado. Cada brief contém informações suficientes para Helix (copy) e Apex (visual) trabalharem de forma autônoma.

## Pre-Conditions

- [ ] Calendário editorial da semana aprovado
- [ ] `data/claims-bank.yaml` disponível
- [ ] `data/buyer-personas.yaml` disponível
- [ ] `data/brand-guidelines.yaml` disponível
- [ ] `templates/content-brief.md` disponível

## Inputs

| Input | Fonte | Obrigatório |
|-------|-------|:-----------:|
| Calendário aprovado | Output de `create-editorial-calendar` | Sim |
| Claims bank | `data/claims-bank.yaml` | Sim |
| Buyer personas | `data/buyer-personas.yaml` | Sim |
| Brand guidelines | `data/brand-guidelines.yaml` | Sim |

## Steps

1. **Para cada slot do calendário:**

   a. **Definir mensagem principal** — 1 frase clara baseada no pilar + produto

   b. **Selecionar claims** — Escolher 2-4 claims do banco (`claims-bank.yaml`) relevantes para o produto e pilar. Registrar IDs (LEV-01, KR-03, etc.)

   c. **Escolher framework de copy** — Baseado no formato:
      - Post de produto → PAS ou AIDA
      - Case de instalação → BAB
      - Thought leadership → SPIN adaptado
      - Carousel educativo → AIDA

   d. **Definir buyer persona alvo** — Escolher da `buyer-personas.yaml`

   e. **Selecionar CTA** — Baseado na etapa do funil e plataforma

   f. **Selecionar hashtags** — Do `data/hashtag-bank.yaml`

   g. **Preencher template de brief** — Formato do `templates/content-brief.md`

2. **Validar batch completo:**
   - [ ] Todos os briefs têm claims válidos (IDs existem no banco)?
   - [ ] Tom de voz correto por marca?
   - [ ] CTA adequado por plataforma?
   - [ ] Specs técnicos corretos por plataforma (dimensões, char limit)?
   - [ ] Nenhum brief com claim inventado (Article IV)?

3. **Apresentar batch para aprovação**

## Output

Conjunto de briefs no formato:

```
=== CONTENT BRIEF ===
ID: SALK-2026-W16-001
Marca: Salk Medical
Produto: LEV 4LEV
Plataforma: Instagram Feed
Formato: Carousel 4:5 (10 slides)
Pilar: Produto em Destaque
Objetivo: Consideração
Mensagem principal: "Iluminação cirúrgica com fidelidade cromática máxima"
Framework: PAS
Tom: Consultivo
Persona alvo: Engenharia Clínica
Claims: [LEV-01, LEV-05, LEV-07, CMP-01]
CTA: "Solicite a ficha técnica completa — link na bio"
Hashtags: #SalkMedical #LEV #FocoCirurgico #CentroCirurgico #EngenhariaClinica ...
Dimensões: 1080x1350 px (4:5)
Nível de revisão: Camadas 1+2+3
```

## Post-Conditions

- Batch de briefs aprovado pelo usuário
- Briefs prontos para `*write-batch-copy` (Helix)
- Claims rastreáveis ao banco

## Error Handling

- Se claim necessário não existe no banco → NÃO inventar. Escalar para Shield para validação de novo claim
- Se slot requer produto sem claims cadastrados → Usar claims genéricos (INST-XX) ou institucional
