# Guia de Execucao NB2 — Calibracao Hero Shots

**Data:** 2026-03-25
**Story:** 1.3 — Calibrar NB2 com hero shots individuais

---

## Passo a Passo para Cada Hero Shot

### 1. Abrir Google AI Studio
- Acessar aistudio.google.com
- Selecionar modelo Gemini (mais recente disponivel)

### 2. Upload do PNG de Referencia
- **LEV 4LEV:** `docs_user/imagem_produtos/Foco de Teto e Parede/Simplex_4LEV.png`
- **KRATUS:** `docs_user/imagem_produtos/Mesa Cirurgica/KRATUS-EH-460K-ML-clean01.png`
- **LEV Duplex:** `docs_user/imagem_produtos/Foco de Teto e Parede/Duplex_3LEV_4LEV.png`
- Fazer upload ANTES de colar o prompt

### 3. Colar o Prompt
- Copiar prompt completo do VDP correspondente
- Colar no chat do AI Studio
- Enviar

### 4. Avaliar Resultado
**Checklist rapido:**
- Produto fiel ao original? (forma, cor, proporcoes)
- Reflexo/superficie visivel?
- Iluminacao premium?
- Sem equipamento concorrente?
- Sem texto/logo gerado?
- "Pararia meu scroll?" → SIM = aprovado

### 5. Se Reprovado — Iterar
- Identificar problema especifico
- Ajustar prompt (V2, V3...)
- Possibilidades de ajuste:
  - Produto distorcido → adicionar "preserve exact product shape"
  - Cenario muito complexo → simplificar descricao do ambiente
  - Iluminacao errada → ajustar descricao de lighting
  - Reflexo demais/de menos → ajustar opacidade descrita
- NUNCA abandonar NB2, NUNCA sugerir colagem no Canva

### 6. Pos-Aprovacao
- Salvar imagem em alta resolucao
- Remover marca d'agua do Google (se houver)
- Aplicar composicao Canva conforme VDP
- Documentar prompt vencedor

---

## Ordem de Execucao

| # | VDP | Arquivo | Prioridade |
|---|-----|---------|:----------:|
| 1 | Hero LEV 4LEV | `calibracao/hero-lev-v1.md` | PRIMEIRO |
| 2 | Hero KRATUS | `calibracao/hero-kratus-v1.md` | SEGUNDO |
| 3 | Hero LEV Duplex | `calibracao/hero-lev-duplex-v1.md` | TERCEIRO |

**Regra:** Aprovar LEV primeiro. Se funcionar, seguir para KRATUS. Se ambos aprovados, tentar o Duplex como bonus.

---

## Resumo dos Conceitos Criativos

| Produto | Conceito | Tecnica | Background |
|---------|----------|---------|------------|
| LEV 4LEV | "Dramatic Studio — Precisao sob Controle" | Dramatic Studio + piso reflexivo preto | Preto puro |
| KRATUS | "Engineering Monolith — Solidez que Inspira" | Industrial luxury + concreto polido | Charcoal escuro |
| LEV Duplex | "Dual Precision — Configuracao sob medida" | Premium tech reveal + metal escovado | Navy-black |

---

**Guia gerado 2026-03-25 — Apex (visual-designer)**
