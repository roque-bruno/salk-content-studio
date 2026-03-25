# PRD v3.0 — Synkra Content Studio (AIOX-Powered)

**Projeto:** Manager Grupo — Maquina Automatica de Producao de Conteudo B2B Healthcare
**Versao:** 3.0
**Status:** Draft
**Data:** 2026-03-25
**Autor:** Orion (aiox-master) com inputs de Aria (architect)
**Supersede:** PRD v2.0 (PRD-content-production.md)
**Fonte primaria:** Analise arquitetural Aria, Budget AI (docs/BUDGET-GERACAO-AI-IMAGEM-VIDEO.md), 6 data files YAML do squad, infraestrutura servidor (docs_user/Servidor e paginas/), 10 conceitos AIOX do NotebookLM

---

## 1. VISAO DO PRODUTO

### 1.1 Declaracao de Visao

O Content Studio e uma maquina automatica de producao de conteudo que transforma o setor de marketing do Manager Grupo de **produtor** em **curador**. O sistema planeja, cria, verifica, atomiza e publica 197 pecas de conteudo por mes para 4 marcas em 4 plataformas — com intervencao humana minima de ~30 minutos semanais.

### 1.2 Problema

| Dimensao | Situacao Atual | Situacao Desejada |
|----------|---------------|-------------------|
| Volume | Producao manual, ~5 pecas/semana | 197 pecas/mes automatizadas |
| Qualidade | Inconsistente, sem compliance | 4 quality gates automaticos |
| Custo | Equipe grande ou agencia cara | R$ 1.804/mes teto (geracao AI) |
| Velocidade | Dias por peca | Batch semanal overnight |
| Conformidade | Verificacao manual ANVISA/CFM | Shield automatico + Disaster Check |
| Presenca | Irregular, sem estrategia | Calendario editorial automatico |

### 1.3 Usuarios

| Usuario | Perfil | Interacao com o Sistema |
|---------|--------|------------------------|
| **Gestora de Marketing** | Nao tecnica, estrategica | Acessa studio.salk.com, aprova/rejeita, publica |
| **Diretoria** | Decisor, visao executiva | Recebe relatorio semanal PDF automatico |
| **AIOX (Backend)** | Sistema autonomo | Executa pipeline, gera, verifica, atomiza |

### 1.4 Metricas de Sucesso

| Metrica | Baseline (hoje) | Meta Mes 3 | Meta Mes 6 |
|---------|:---------------:|:----------:|:----------:|
| Publicacoes/mes | ~20 | 100 | 197 |
| Tempo gestora/semana | N/A | 60 min | 30 min |
| Taxa acerto imagem NB2 | 30% | 50% | 65% |
| Taxa acerto video Kling | 25% | 40% | 50% |
| Custo geracao/mes | N/A | R$ 1.804 | R$ 750 |
| Violacoes compliance publicadas | desconhecido | 0 | 0 |

---

## 2. ARQUITETURA DO SISTEMA

### 2.1 Principio Fundamental: IA vs Worker vs Gate

| Tipo | Quando Usar | Erro Possivel | Exemplo |
|------|------------|:-------------:|---------|
| **Agente (IA)** | Tarefa criativa ou de raciocinio | Alucinacao controlada | Escrever copy, criar prompt NB2, avaliar persona |
| **Worker (Script)** | Tarefa deterministica, "apertar botao" | Zero | Chamar API Gemini, FFmpeg, publicar post |
| **Quality Gate** | Validacao binaria: passa ou nao passa | Zero | Shield ANVISA, Disaster Check, Brand Check |

**Regra de ouro:** Se a tarefa tem resposta certa e errada → Worker ou Gate. Se precisa de julgamento → Agente.

### 2.2 Stack Tecnico

| Camada | Tecnologia | Deploy |
|--------|-----------|--------|
| Frontend | HTML/CSS/JS estatico (Alpine.js) | cPanel → studio.salk.com |
| Backend API | FastAPI + Python | Render free tier / VPS leve |
| Banco de Dados | SQLite embarcado | Junto com API |
| Geracao Imagem | Gemini 3.1 Flash (NB2) — $0.05/img | API direta |
| Geracao Video | Kling 3.0 Pro — $0.14/s | API direta |
| Narracao | ElevenLabs (voz Bill) — multilingual_v2 | API direta |
| Montagem Video | FFmpeg (serverless) | Worker Python |
| Automacao | GitHub Actions (CRON semanal) | GitHub |
| Roteamento LLM | OpenRouter | Otimizacao de custo |
| CI/CD | GitHub Actions | GitHub |

### 2.3 Diagrama de Arquitetura

```
┌──────────────────────────────────────────────────┐
│          studio.salk.com (Frontend)               │
│          HTML/CSS/JS estatico no cPanel            │
│          Gestora acessa via browser                │
└────────────────────┬─────────────────────────────┘
                     │ HTTPS API calls
┌────────────────────▼─────────────────────────────┐
│          Backend API (FastAPI)                     │
│          Render / VPS / GitHub Actions             │
│          SQLite + Business Logic                   │
└────┬──────────┬──────────┬──────────┬────────────┘
     │          │          │          │
┌────▼────┐┌───▼────┐┌────▼────┐┌────▼─────┐
│ Gemini  ││ Kling  ││Eleven   ││OpenRouter│
│ NB2 API ││ 3.0 Pro││Labs API ││ LLM Hub  │
│$0.05/img││$0.14/s ││ TTS     ││ Routing  │
└─────────┘└────────┘└─────────┘└──────────┘
     │          │          │
┌────▼──────────▼──────────▼───────────────────────┐
│         GitHub Actions (CRON Semanal)              │
│  Domingo 22h: pipeline completo automatizado       │
│  Diario: coleta metricas, verifica publicacoes     │
└──────────────────────────────────────────────────┘
```

### 2.4 Separacao Frontend / Backend

| Componente | Responsabilidade | Hospedagem |
|-----------|-----------------|-----------|
| **Frontend** | UI pura — dashboard, kanban, formularios, review | cPanel salk.com (estatico) |
| **Backend** | Logica de negocio, APIs, orquestracao, geracao | Render/VPS (sempre ativo) |
| **CRON** | Pipeline automatizado (batch semanal) | GitHub Actions |

O frontend chama a API backend via HTTPS. O backend faz todo o trabalho pesado. A gestora NUNCA precisa rodar nada na maquina pessoal.

---

## 3. SQUAD DE AGENTES AIOX

### 3.1 Agentes Criativos (IA)

| Agente | Funcao | LLM (via OpenRouter) | Knowledge Base |
|--------|--------|---------------------|----------------|
| **Atlas** | Planejamento editorial, briefings | Flash/Haiku ($) | editorial-calendar-template.yaml |
| **Helix-Salk** | Copywriter Salk Medical (tom comercial) | Sonnet ($$) | brand-guidelines.yaml (salk) |
| **Helix-Mendel** | Copywriter Mendel Medical (tom tecnico) | Sonnet ($$) | brand-guidelines.yaml (mendel) |
| **Helix-Manager** | Copywriter Manager Grupo (tom institucional) | Sonnet ($$) | brand-guidelines.yaml (manager) |
| **Helix-Dayho** | Copywriter Dayho (tom industrial) | Sonnet ($$) | brand-guidelines.yaml (dayho) |
| **Apex** | Prompt Designer NB2 (8 dimensoes) | Sonnet ($$) | presets, regras NB2 |
| **Nova** | Atomizador semantico (master → derivados) | Flash ($) | platform-specs.yaml |
| **Pulse** | Analista de performance (feedback loop) | Flash ($) | metricas, Journey Log |

### 3.2 Agentes de Validacao (IA + Regras)

| Agente | Funcao | Modo | LLM |
|--------|--------|------|-----|
| **Shield** | Compliance ANVISA/CFM (textual) | Deterministico + IA | Sonnet ($$) |
| **Disaster Check** | Validacao visual pos-geracao | IA Vision | Flash Vision ($) |
| **Persona Clone: Eng. Clinica** | Simula reacao da persona | IA | Flash ($) |
| **Persona Clone: Compras** | Simula reacao da persona | IA | Flash ($) |
| **Persona Clone: Eq. Medica** | Simula reacao da persona | IA | Flash ($) |
| **Persona Clone: Admin** | Simula reacao da persona | IA | Flash ($) |

### 3.3 Workers (Scripts Deterministicos)

| Worker | Funcao | Tecnologia | Taxa Acerto |
|--------|--------|-----------|:-----------:|
| **Gemini Worker** | Chamar API NB2, upload PNG, extrair imagem | Python + google-generativeai | 100% |
| **Kling Worker** | Chamar API Kling 3.0 Pro (I2V) | Python + httpx | 100% |
| **ElevenLabs Worker** | Gerar narracao TTS (voz Bill) | Python + elevenlabs SDK | 100% |
| **FFmpeg Worker** | Montar video (clip + audio + legendas) | Python + ffmpeg-python | 100% |
| **Publisher Worker** | Publicar via APIs Instagram/LinkedIn/YouTube/FB | Python + APIs oficiais | 100% |
| **Metrics Worker** | Coletar metricas pos-publicacao | Python + APIs oficiais | 100% |
| **cPanel Worker** | Upload de arquivos para salk.com | Python + cPanel UAPI | 100% |

### 3.4 Quality Gates (Deterministicos)

| Gate | Ponto no Pipeline | Criterio | Acao se Falhar |
|------|-------------------|----------|----------------|
| **Gate 1: Shield** | Apos copy gerado | Termos proibidos, ETRUS, superlativos, promessas | Devolve ao copywriter |
| **Gate 2: Disaster Check** | Apos imagem/video gerado | Texto alucinado, anatomia bizarra, produto distorcido | Regenera (max 3x) |
| **Gate 3: Brand Check** | Apos composicao | Logo correto, cores, tipografia, posicao | Recompoe |
| **Gate 4: Human Approval** | Board da gestora | Aprovacao humana | Gestora rejeita com comentario |

---

## 4. KNOWLEDGE BASES (Fontes da Verdade)

| Arquivo | Conteudo | Owner | Usado por |
|---------|---------|-------|-----------|
| `claims-bank.yaml` | 45 claims regulatorios aprovados com fonte | Shield, Helix-* | Copy, compliance |
| `brand-guidelines.yaml` | Regras visuais e tom de cada marca | Helix-*, Brand Check | Copy, composicao |
| `prohibited-terms.yaml` | 7 categorias de termos proibidos | Shield | Compliance |
| `platform-specs.yaml` | Dimensoes, formatos, limites por plataforma | Nova, Workers | Atomizacao, export |
| `buyer-personas.yaml` | 4 personas com dores, keywords, claims | Atlas, Persona Clones | Briefing, copy |
| `hashtag-bank.yaml` | Hashtags curadas por marca e plataforma | Helix-* | Copy final |
| `editorial-calendar-template.yaml` | Template semanal com frequencia e pilares | Atlas | Planejamento |

### 4.1 Design System como Cabresto

Cada marca tem um brandbook YAML que atua como regra inviolavel para a IA:

```yaml
# Exemplo: salk-brandbook.yaml
brand: salk
tagline: "Sala Cirurgica Inteligente"
tone: consultivo, confiante, orientado a resultados
logo_rule: "Salk = conteudo comercial/vendas"
pillars:
  produto: 30%
  educacional: 25%
  cases: 20%
  command: 15%
  licitacoes: 10%
visual_rules:
  - SEMPRE foto real do produto (PNG upload como referencia)
  - NUNCA pessoas geradas por IA
  - NUNCA cenas clinicas geradas por IA
  - NUNCA texto ou logo na imagem IA
  - NUNCA equipamentos concorrentes no cenario
  - LEV: luz FOCADA para baixo, NUNCA dispersa
colors:
  primary: "#1e3a5f"
  accent: "#60a5fa"
canva:
  margins: 60px
  logo_min_width: 180px
  headline: 36pt bold, left-aligned, top
  spec_line: 18pt light, white 70%, centered bottom
  anvisa_badge: 12pt, white 50%, bottom-right
```

---

## 5. PIPELINE SEMANAL AUTOMATIZADO

### 5.1 Fluxo Completo

```
DOMINGO 22h (CRON GitHub Actions)
│
├─ FASE 1: PLANEJAMENTO (Atlas)
│  ├─ Carregar template editorial da semana
│  ├─ Rotacao de pilares (produto 30%, edu 25%, cases 20%, etc.)
│  ├─ Selecionar produtos e personas por slot
│  └─ Gerar ~30 briefings → LLM: Flash ($)
│
├─ FASE 2: COPY (Helix-{marca})
│  ├─ Briefing + claims + brandbook + persona → copy
│  ├─ Headline, CTA, hashtags auto-selecionadas
│  └─ Limites de caracteres por plataforma → LLM: Sonnet ($$)
│
├─ FASE 3: TESTE DE PERSONA (Persona Clones)
│  ├─ Copy → clone da persona-alvo avalia
│  ├─ "Eng. Clinico virtual" da feedback
│  └─ Copywriter refina se necessario → LLM: Flash ($)
│
├─ GATE 1: COMPLIANCE (Shield)
│  ├─ Verificar termos proibidos (deterministico)
│  ├─ Verificar ETRUS (deterministico)
│  ├─ Verificar claims validos (deterministico + IA)
│  ├─ APROVADO → avanca
│  └─ REJEITADO → volta ao copywriter (loop max 3x)
│
├─ FASE 4: VISUAL (Apex)
│  ├─ Conceito + produto → prompt NB2 8 dimensoes
│  └─ Formato + dimensoes por plataforma → LLM: Sonnet ($$)
│
├─ FASE 5: GERACAO IMAGEM (Gemini Worker)
│  ├─ Prompt + PNG referencia → API Gemini NB2
│  ├─ $0.05 por imagem
│  └─ Worker deterministico (100% acerto na chamada)
│
├─ GATE 2: DISASTER CHECK
│  ├─ Imagem gerada → analise visual
│  ├─ Texto alucinado? Anatomia bizarra? Produto distorcido?
│  ├─ APROVADO → avanca
│  └─ REJEITADO → regenera (max 3x) → LLM: Flash Vision ($)
│
├─ FASE 6: GERACAO VIDEO (Kling Worker)
│  ├─ Imagem NB2 aprovada → API Kling 3.0 Pro (I2V)
│  ├─ 4K @ 60fps, fisica realista
│  ├─ $0.14 por segundo
│  └─ Worker deterministico
│
├─ FASE 7: MONTAGEM (FFmpeg Worker)
│  ├─ Video AI + narracao ElevenLabs + musica + legendas
│  ├─ Script deterministico, 100% acerto
│  └─ Exporta nos formatos corretos por plataforma
│
├─ FASE 8: ATOMIZACAO (Nova)
│  ├─ Master → derivados semanticos (nao apenas recorte)
│  ├─ 1 conceito → 5-8 pecas por plataforma
│  ├─ Copy adaptado, dimensoes corretas, hashtags ajustadas
│  └─ LLM: Flash ($) + Workers FFmpeg
│
├─ GATE 3: BRAND CHECK
│  ├─ Logo correto (Mendel tecnico / Salk comercial)
│  ├─ Cores, tipografia, posicao ANVISA badge
│  └─ Deterministico (regras do cabresto)
│
└─ FASE 9: KANBAN
   ├─ Todas as pecas → status "AGUARDANDO REVIEW"
   └─ Alimenta studio.salk.com via API

SEGUNDA 9h (Gestora — ~30 min)
├─ Abre studio.salk.com
├─ Revisa board da semana
├─ Aprova / Rejeita com comentario
└─ Clica "Publicar Semana"

AUTOMATICO (Publisher Worker)
├─ Publica nos horarios otimizados por plataforma
├─ Salk: IG 11-13h, LI 8-10h, FB 12-15h
└─ Agendamento respeitando frequencia por marca

+48h (Metrics Worker + Pulse)
├─ Coleta metricas via APIs das plataformas
├─ Journey Log registra performance por combinacao
├─ Pulse analisa e ajusta parametros
└─ Feedback loop → proximo domingo mais preciso
```

### 5.2 Roteamento de Custos (OpenRouter)

| Tarefa | Modelo via OpenRouter | Custo Relativo | Justificativa |
|--------|----------------------|:-:|---|
| Briefing/ideacao | Gemini Flash / Haiku | $ | Rapido, criativo |
| Copy final | Claude Sonnet | $$ | Tom preciso, claims corretos |
| Shield compliance | Claude Sonnet | $$ | Raciocinio robusto para edge cases |
| Disaster check visual | Gemini Flash Vision | $ | Analise pass/fail rapida |
| Teste de persona | Gemini Flash | $ | Simulacao rapida |
| Prompt NB2 | Claude Sonnet | $$ | Criatividade + precisao |
| Atomizacao | Gemini Flash | $ | Decisoes de corte simples |
| Analise de metricas | Gemini Flash | $ | Dados estruturados |

**Estimativa custo LLM:** ~$15-25/mes (alem do budget de geracao imagem/video)

### 5.3 Memory Layer — Journey Log

| Evento | O que Registra | Usado Para |
|--------|---------------|-----------|
| Peca gerada | Prompt, modelo, tempo, custo | Otimizacao de prompts |
| Shield rejeita | Termo violado, motivo, copy original | Self-learning (evitar no futuro) |
| Disaster Check rejeita | Tipo de falha visual | Ajustar prompts NB2 |
| Gestora rejeita | Motivo do comentario | Refinar briefings futuros |
| Metrica coletada | Engajamento, alcance, impressoes | Feedback loop por pilar/persona |
| Prompt que acertou | Prompt exato + resultado aprovado | Banco de prompts validados |

**Self-learning:** O Analyst (Pulse) revisa o Journey Log semanalmente e ajusta:
- Pilares com melhor performance → mais frequencia
- Prompts com alta taxa de acerto → reutilizar
- Combinacoes produto+persona com mais engajamento → priorizar
- Claims mais eficazes → sugerir primeiro nos briefings

---

## 6. BUDGET CONSOLIDADO

### 6.1 Custos de Geracao AI (Mensal)

| Componente | Volume | Custo Unitario | Total/Mes |
|-----------|:------:|:-:|:-:|
| Imagens NB2 (Gemini) | 396 geracoes | $0.05 | $19.80 |
| Videos Kling 3.0 Pro | 1.928 segundos | $0.14 | $269.92 |
| Buffer seguranca 10% | — | — | $28.97 |
| **Subtotal Geracao** | | | **$318.69** |

### 6.2 Custos de LLM (Mensal)

| Componente | Estimativa |
|-----------|:-:|
| OpenRouter (mix Flash/Sonnet) | $15-25 |
| ElevenLabs (narracao) | $5-15 |
| **Subtotal LLM** | **$20-40** |

### 6.3 Custos de Infraestrutura (Mensal)

| Componente | Custo |
|-----------|:-:|
| cPanel (ja existente) | $0 |
| Render free tier (API) | $0 |
| GitHub Actions (2000 min gratis) | $0 |
| Dominio salk.com (ja existente) | $0 |
| **Subtotal Infra** | **$0** |

### 6.4 Budget Total

| | USD/mes | BRL/mes |
|---|:-:|:-:|
| Geracao AI | $319 | R$ 1.804 |
| LLM/OpenRouter | $30 | R$ 170 |
| Infra | $0 | R$ 0 |
| **TETO MENSAL** | **$349** | **R$ 1.974** |

**Evolucao com maturidade:**

| Fase | Mes | Budget Estimado |
|------|:---:|:-:|
| Calibrando | 1-2 | R$ 1.974 |
| Estavel | 3-5 | R$ 1.200 |
| Otimizado | 6+ | R$ 800 |

---

## 7. INTERFACE WEB — studio.salk.com

### 7.1 Secoes do Sistema

| # | Secao | Funcao Principal | Status Atual |
|:-:|-------|-----------------|:------------:|
| 1 | Dashboard | Visao geral, stats, acoes rapidas | Esqueleto v2.0 |
| 2 | Production Board | Kanban 6 estagios (briefing→published) | Esqueleto v2.0 |
| 3 | Calendario Editorial | Planejamento semanal por marca | Esqueleto v2.0 |
| 4 | Copy Editor | Editor com claims, compliance inline | Esqueleto v2.0 |
| 5 | VDP Creator | Criacao completa de VDPs | Esqueleto v2.0 |
| 6 | NB2 Studio | Prompt builder 8 dimensoes | Esqueleto v2.0 |
| 7 | Video Studio | Pipeline I2V, preview, galeria | **NAO EXISTE** |
| 8 | Compliance | Shield checker, glossario seguro | Esqueleto v2.0 |
| 9 | Review Queue | Fila com aprovar/rejeitar | Esqueleto v2.0 |
| 10 | Asset Library | Thumbnails produtos + logos | Esqueleto v2.0 |
| 11 | Claims Bank | Tabela filtravel com 45 claims | Esqueleto v2.0 |
| 12 | Hashtag Bank | Chips selecionaveis por marca | Esqueleto v2.0 |
| 13 | Buyer Personas | Cards com 4 personas detalhadas | Esqueleto v2.0 |
| 14 | Performance | Metricas, dashboard, historico | Esqueleto v2.0 |
| 15 | Budget Tracker | Gastos API em tempo real | **NAO EXISTE** |
| 16 | Journey Log | Historico de decisoes e aprendizados | **NAO EXISTE** |

### 7.2 Interacao Humana Minima

A gestora interage com o sistema em 3 momentos:

| Momento | Frequencia | Duracao | Acao |
|---------|-----------|---------|------|
| **Review semanal** | 1x/semana (segunda) | ~30 min | Revisar board, aprovar/rejeitar batch |
| **Ajuste mensal** | 1x/mes | ~15 min | Revisar performance, ajustar prioridades |
| **Excepcoes** | Quando necessario | ~5 min | Criar peca especial, campanha sazonal |

---

## 8. EPICOS DE IMPLEMENTACAO

### Epico 2 — Fundacao e Deploy (Semanas 1-2)

| Story | Titulo | Descricao | Agente |
|:-----:|--------|-----------|--------|
| 2.1 | Separar frontend do backend | Frontend estatico puro, API independente, CORS | @dev |
| 2.2 | Deploy frontend no cPanel | Subir HTML/CSS/JS em studio.salk.com | @devops |
| 2.3 | Deploy API no Render | FastAPI no Render free tier com auto-deploy | @devops |
| 2.4 | Migrar persistencia para SQLite | Substituir JSON files por SQLite | @dev |
| 2.5 | Autenticacao basica | Login simples para gestora (JWT ou session) | @dev |
| 2.6 | Brandbooks YAML por marca | Criar 4 brandbook configs como knowledge base | @dev |
| 2.7 | Design System como cabresto | Implementar validacao de marca em todos os gates | @dev |
| 2.8 | Setup GitHub Actions basico | CI/CD para deploy automatico | @devops |

### Epico 3 — Video Pipeline + Geracao (Semanas 3-5)

| Story | Titulo | Descricao | Agente |
|:-----:|--------|-----------|--------|
| 3.1 | Kling 3.0 Pro API client | Cliente Python com retry, I2V, extracao video | @dev |
| 3.2 | Pipeline Image-to-Video | NB2 hero → Kling anima → output video | @dev |
| 3.3 | ElevenLabs TTS integration | Narracao com voz Bill, multilingual_v2 | @dev |
| 3.4 | FFmpeg video assembly | Worker: clip + narracao + musica + legendas | @dev |
| 3.5 | Video Studio na UI | Secao de video no frontend: I2V, preview, galeria | @dev |
| 3.6 | OpenRouter integration | Roteamento inteligente de LLMs por tarefa | @dev |
| 3.7 | Budget tracker | Dashboard de gastos API em tempo real | @dev |
| 3.8 | Journey Log v1 | Registro de todas as decisoes e resultados | @dev |

### Epico 4 — Automacao + Inteligencia (Semanas 6-8)

| Story | Titulo | Descricao | Agente |
|:-----:|--------|-----------|--------|
| 4.1 | Auto-briefing (Atlas) | Gerar briefing automatico por slot do calendario | @dev |
| 4.2 | Squad copywriters por marca | 4 agentes com brandbook individual | @dev |
| 4.3 | Persona clones | Simulacao de 4 personas para testar copy | @dev |
| 4.4 | Auto-prompt NB2 (Apex) | Gerar prompt 8 dimensoes automaticamente | @dev |
| 4.5 | Disaster Check visual | Verificar imagem/video pos-geracao | @dev |
| 4.6 | Atomizacao semantica (Nova) | Master → derivados com sentido logico | @dev |
| 4.7 | CRON semanal completo | GitHub Actions: pipeline domingo 22h | @devops |
| 4.8 | Self-learning via Journey Log | Pulse analisa e ajusta parametros | @dev |

### Epico 5 — Escala + Publicacao (Semanas 9-12)

| Story | Titulo | Descricao | Agente |
|:-----:|--------|-----------|--------|
| 5.1 | Publisher Worker Instagram | API Instagram Graph para publicacao | @dev |
| 5.2 | Publisher Worker LinkedIn | API LinkedIn para publicacao | @dev |
| 5.3 | Publisher Worker YouTube | API YouTube Data v3 para Shorts | @dev |
| 5.4 | Publisher Worker Facebook | API Facebook Graph para publicacao | @dev |
| 5.5 | Metrics Collector automatico | Coletar engajamento 48h pos-publicacao | @dev |
| 5.6 | Feedback loop completo | Performance informa briefings futuros | @dev |
| 5.7 | Relatorio semanal PDF | Gerar e enviar relatorio automatico | @dev |
| 5.8 | Batch approval workflow | Gestora aprova semana inteira de uma vez | @dev |

---

## 9. RESTRICOES E REGRAS INEGOCIAVEIS

### 9.1 Produto

| Regra | Severidade |
|-------|:----------:|
| ETRUS PROIBIDO — nunca publicar | BLOQUEANTE |
| COMMAND — verificar independencia do ETRUS | ALTA |
| Claims apenas de claims-bank.yaml com fonte | BLOQUEANTE |
| Sem superlativos ("o melhor", "o unico") | BLOQUEANTE |
| Sem promessas ("garante", "cura", "100% seguro") | BLOQUEANTE |
| Badge ANVISA obrigatorio em toda peca | ALTA |

### 9.2 Visual

| Regra | Severidade |
|-------|:----------:|
| NUNCA pessoas geradas por IA | BLOQUEANTE |
| NUNCA cenas clinicas geradas por IA | BLOQUEANTE |
| NUNCA texto ou logo na imagem IA (adicionar no Canva) | BLOQUEANTE |
| NUNCA equipamentos concorrentes no cenario | BLOQUEANTE |
| NUNCA wallpaper + colagem (= PROIBIDO) | BLOQUEANTE |
| LEV: luz FOCADA para baixo, NUNCA dispersa | ALTA |
| Cores/aparencia devem corresponder ao produto real | ALTA |
| Mendel = tecnico | Salk = comercial (regra da diretora) | ALTA |

### 9.3 Infraestrutura

| Regra | Severidade |
|-------|:----------:|
| Sistema NAO pode depender de maquina pessoal | BLOQUEANTE |
| Gestora acessa via browser (studio.salk.com) | BLOQUEANTE |
| SSH bloqueado no servidor — usar cPanel UAPI | ALTA |
| Budget mensal maximo: R$ 2.000 | ALTA |

---

## 10. GLOSSARIO

| Termo | Definicao |
|-------|-----------|
| **NB2** | Nano Banana 2 — tecnica de upload do produto real como referencia + IA renderiza ele no cenario |
| **I2V** | Image-to-Video — imagem estatica como input para gerar video animado |
| **VDP** | Visual Design Pack — arquivo markdown com prompt NB2 + checklist + composicao Canva + claims |
| **Atomizacao** | Processo de transformar 1 master em 5-8 derivados por plataforma |
| **Shield** | Quality gate de compliance textual (ANVISA/CFM) |
| **Disaster Check** | Quality gate de validacao visual pos-geracao |
| **Journey Log** | Registro historico de todas as decisoes, rejeicoes e metricas do pipeline |
| **Cabresto** | Regras inviolaveis do Design System que limitam a IA |
| **Worker** | Script deterministico que executa tarefa sem IA (100% acerto) |
| **Quality Gate** | Ponto de validacao binaria: passa ou nao passa |
| **OpenRouter** | Hub de roteamento entre diferentes LLMs para otimizar custo |

---

*PRD v3.0 — Synkra Content Studio AIOX-Powered*
*Gerado por Orion (aiox-master) com inputs arquiteturais de Aria (architect)*
*Data: 2026-03-25*
