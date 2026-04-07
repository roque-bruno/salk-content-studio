# Content Studio — Projeto de Producao de Conteudo para Redes Sociais

> **Manager Grupo** | Sao Jose dos Pinhais/PR
> Documento atualizado em: 2026-04-07

---

## 1. O Que e Este Projeto

O Content Studio e um sistema web completo para **producao em massa de conteudo profissional para redes sociais**, construido sob medida para o Manager Grupo — um grupo empresarial do setor de equipamentos medico-hospitalares.

O sistema permite que uma unica gestora de marketing planeje, produza, revise e publique dezenas de pecas de conteudo por semana, para 4 marcas e 6 plataformas, com qualidade consistente e compliance regulatorio — algo que normalmente exigiria uma equipe de 5-8 pessoas.

**Endereco em producao:** https://studio.salkmedical.com/

---

## 2. Por Que Este Projeto Existe

### O Problema

O Manager Grupo e dono de uma cadeia de valor verticalizada no setor de saude:

```
Dayho (fabrica pecas metalicas) → Mendel Medical (monta equipamentos medicos ANVISA) → Salk Medical (comercializa) → Hospitais
```

Apesar de ter produtos tecnicamente superiores em varias categorias (foco cirurgico LEV com Ra/R9=99 vs media de mercado 85-92, mesa KRATUS com menor preco da categoria EH), o grupo tinha **presenca digital quase inexistente**. Nenhum fabricante nacional de equipamentos medicos tem uma estrategia de conteudo sofisticada — existe um vazio digital enorme neste mercado.

### O Desafio

Produzir conteudo para equipamentos medicos nao e como produzir conteudo para varejo. Existem barreiras reais:

1. **Regulatorio:** ANVISA (RDC 96/2008, RDC 751/2022), CFM, CONAR — nao se pode prometer resultados clinicos, usar superlativos, ou inventar specs
2. **Tecnico:** O publico-alvo inclui engenheiros clinicos que verificam cada numero. Claims devem ser rastreaveis aos manuais oficiais
3. **Multi-marca:** 4 marcas com tons completamente diferentes — de consultivo (Salk) a industrial (Dayho)
4. **Multi-persona:** 4 buyer personas com linguagens e preocupacoes distintas — de cirurgioes a gestores de compras
5. **Multi-plataforma:** Instagram, LinkedIn, YouTube, Facebook, email, WhatsApp — cada um com seus limites e formatos
6. **Volume:** A meta de regime e ~48 pecas/semana para todas as marcas

### A Oportunidade

A pesquisa de mercado revelou que:

- **Nenhum concorrente nacional** tem estrategia de conteudo digital sofisticada
- O conteudo B2B healthcare no Brasil e dominado por posts genericos e sem dados
- Com IA generativa (imagens, video, copy), e possivel produzir conteudo de qualidade profissional a ~R$1 por peca completa
- A atomizacao (1 peca-mae = 5-8 derivados) multiplica o volume sem multiplicar o esforco

### A Decisao

Em vez de contratar uma agencia (que dificilmente dominaria o setor regulado de dispositivos medicos), o grupo decidiu construir **uma fabrica de conteudo propria**, automatizada por IA mas governada por regras de negocio rigidas.

---

## 3. O Que o Sistema Faz

O Content Studio e uma aplicacao web que cobre todo o ciclo de vida de uma peca de conteudo:

### 3.1 Planejamento (Calendario)

A gestora abre o calendario semanal e ve os slots de conteudo distribuidos por dia, plataforma e pilar de conteudo. O sistema sugere automaticamente a distribuicao ideal baseada nos pesos configurados (ex: Salk = 30% produto, 25% educacional, 20% cases...).

Para cada slot, o sistema pode **gerar um briefing automatico** usando IA (Atlas), que ja vem com:
- Objetivo especifico ao tema
- Mensagem-chave com diferencial tecnico real
- CTA consultivo
- Claims sugeridos do banco aprovado
- Instrucoes visuais para a imagem NB2

### 3.2 Producao de Copy

Com o briefing pronto, o sistema gera o texto (copy) usando **copywriters virtuais especializados por marca**:

- **Helena** (Salk) — tom consultivo, orientado a resultados
- **Roberto** (Mendel) — tecnico, preciso, autoritativo
- **Carolina** (Manager Grupo) — acolhedor, institucional
- **Marcos** (Dayho) — industrial, solido

Cada copywriter opera sob regras rigidas: NUNCA mencionar ETRUS, NUNCA usar superlativos, claims SOMENTE do banco aprovado, tom conforme brandbook. O copy e revisado por **persona clones** (Dr. Marcelo, Fernanda, Dra. Ana, Carlos) que simulam a reacao do publico-alvo real.

### 3.3 Producao Visual (Imagem)

O sistema gera imagens profissionais dos produtos usando **NB2 (Nano Banana 2)** via fal.ai:

1. A gestora seleciona o produto (LEV, KRATUS, OSTUS, KRONUS)
2. O sistema carrega a imagem PNG real do produto como referencia
3. Um **prompt de 8 dimensoes** e construido automaticamente (tecnica, iluminacao, cenario, composicao, atmosfera, detalhes tecnicos + regras do produto + negativos obrigatorios)
4. A IA renderiza o produto real DENTRO de um cenario profissional
5. O sistema verifica automaticamente 10 quality gates (texto na imagem? equipamento concorrente? distorcao do produto? direcao da luz LEV?)

**Importante:** O sistema NUNCA gera wallpaper + colagem. O produto real e integrado na cena pela IA. E NUNCA gera texto, logo ou pessoas — esses sao adicionados no Canva pela equipe de design.

### 3.4 Producao de Video

O sistema anima as imagens geradas em videos curtos usando:
- **Minimax/Hailuo** — video I2V (imagem para video), ~$0.12/video
- **Kling 3.0** — alternativa de alta qualidade
- **ElevenLabs** — narracao profissional por voz sintetica
- **FFmpeg** — montagem, legendas, transicoes

### 3.5 Atomizacao

Uma peca-mae (ex: carrossel para Instagram) e automaticamente **atomizada** em derivados para outras plataformas:

| Master | Derivados Automaticos |
|--------|----------------------|
| Carrossel | Story + Reel + LinkedIn Post + Email |
| Post Unico | Story + LinkedIn + WhatsApp |
| Video Longo | Reels + Story + LinkedIn |
| Artigo | LinkedIn + Instagram + Email + WhatsApp |

Cada derivado e adaptado: limite de caracteres, tom, hashtags, CTA — tudo conforme as specs da plataforma de destino.

### 3.6 Quality Gate (Compliance)

Antes de publicar, cada peca passa por verificacoes automaticas:

**Bloqueiam publicacao (severity: block):**
- Texto ou logo gerado por IA na imagem
- Equipamento medico concorrente visivel
- Rostos identificaveis (LGPD)
- Cenas clinicas graficas
- Luz do LEV dispersa (contradiz o produto)
- Produto distorcido

**Geram alerta (severity: warn):**
- Qualidade tecnica baixa (blur, artefatos)
- Composicao inadequada
- Cores fora da paleta da marca
- Cenario vazio/generico

### 3.7 Aprovacao e Publicacao

A gestora revisa as pecas no painel de aprovacao, podendo aprovar, rejeitar ou solicitar ajustes. Pecas aprovadas podem ser publicadas diretamente nas plataformas via API (Instagram, LinkedIn, Facebook, YouTube).

### 3.8 Configuracao Total pela Gestora

**Todo** dado estrategico do sistema e editavel pela interface web — nada esta fixo no codigo:

**Secao "Marca" (sidebar):**
- Brandbooks das 4 marcas (tom, cores, logo, produtos, personas)
- Buyer personas com linguagem e CTAs
- Termos proibidos (compliance ANVISA)
- Claims aprovados (banco de argumentos tecnicos)
- Hashtags curadas por marca e plataforma
- Diretrizes de marca e regra de logo
- Specs de plataforma (dimensoes, limites)
- Calendario editorial (template semanal e metas)

**Secao "Motor IA" (sidebar):**
- Copywriters (personalidade e prompt de cada redator virtual)
- Geracao de Imagem (dimensoes NB2, negativos, regras por produto)
- Estrategia de Conteudo (pesos de pilares, personas por pilar, tecnicas visuais)
- Atomizacao (formatos por plataforma, mapa de derivacoes)
- Quality Gate (checks, severidade, produtos especificos)
- Briefing Atlas (prompt do estrategista de conteudo)

---

## 4. Como o Sistema Funciona (Arquitetura)

### 4.1 Visao Geral

```
┌─────────────────────────────────────────────────────┐
│                 BROWSER (gestora)                     │
│            studio.salkmedical.com                     │
│        Alpine.js SPA + HTML/CSS/JS                    │
└──────────────────────┬──────────────────────────────┘
                       │ HTTPS
                       ▼
┌─────────────────────────────────────────────────────┐
│              VPS (162.240.13.51)                      │
│         Docker Container (Python 3.13)                │
│                                                       │
│  ┌─────────────────────────────────────────────────┐ │
│  │            FastAPI (90+ endpoints)                │ │
│  │  ┌──────────┐  ┌──────────┐  ┌───────────────┐  │ │
│  │  │ Services │  │   Auth   │  │ Settings Store│  │ │
│  │  └─────┬────┘  └──────────┘  └───────────────┘  │ │
│  │        │                                          │ │
│  │  ┌─────▼──────────────────────────────────────┐  │ │
│  │  │          Automation Modules                 │  │ │
│  │  │  AutoBriefing | BrandCopywriter | AutoPrompt│  │ │
│  │  │  ImageGenerator | VideoAnimator | Atomizer  │  │ │
│  │  │  DisasterCheck | WeekOrchestrator           │  │ │
│  │  └─────┬──────────────────────────────────────┘  │ │
│  │        │                                          │ │
│  │  ┌─────▼──────────────────────────────────────┐  │ │
│  │  │          YAML Data Files                    │  │ │
│  │  │  squads/content-production/data/            │  │ │
│  │  │  18 arquivos = fonte unica de verdade       │  │ │
│  │  └────────────────────────────────────────────┘  │ │
│  └──────────────────────────────────────────────────┘ │
│                                                       │
│  APIs Externas:                                       │
│  ├─ OpenRouter (LLM: Gemini Flash, Claude, GPT)      │
│  ├─ fal.ai (NB2/FLUX: geracao de imagens)             │
│  ├─ Minimax/Kling (geracao de video)                  │
│  ├─ ElevenLabs (narracao por voz)                     │
│  └─ Supabase (banco de dados)                         │
└─────────────────────────────────────────────────────┘
```

### 4.2 Stack Tecnologica

| Camada | Tecnologia |
|--------|-----------|
| **Frontend** | HTML + Alpine.js (SPA de arquivo unico, ~12.750 linhas) |
| **Backend** | Python 3.13 + FastAPI (90+ endpoints) |
| **Banco de Dados** | Supabase (PostgreSQL hospedado) + SQLite (fallback local) |
| **Autenticacao** | JWT com usuario/senha configuravel |
| **Config/Dados** | 18 arquivos YAML (editaveis pela UI) |
| **IA — Texto** | OpenRouter → Gemini Flash 2.0 ($0.04/peca) |
| **IA — Imagem** | fal.ai → FLUX/NB2 ($0.04-0.08/imagem) |
| **IA — Video** | Minimax ($0.12/video), Kling 3.0, Veo 3 |
| **IA — Voz** | ElevenLabs (voice Bill, multilingual_v2) |
| **Video Processing** | FFmpeg (montagem, legendas, transicoes) |
| **Hospedagem** | VPS cPanel (Docker, porta 8000, HTTPS via proxy) |
| **Deploy** | Git push → SSH → Docker rebuild |

### 4.3 Modulos do Sistema

O backend e organizado em 8 pacotes:

**`automation/`** — Cerebro do sistema (9 modulos)
| Modulo | Funcao |
|--------|--------|
| `auto_briefing.py` | Atlas — gera briefings automaticos por slot do calendario |
| `copywriter.py` | Helena/Roberto/Carolina/Marcos — copywriters por marca + persona clones |
| `auto_prompt.py` | Apex — constroi prompts NB2 de 8 dimensoes para imagens |
| `image_generator.py` | Gera imagens via fal.ai com FLUX/NB2 |
| `video_animator.py` | Anima imagens em video via Minimax/Kling |
| `keyframe_processor.py` | Extrai keyframes FFmpeg → altera via NB2 → remonta |
| `week_orchestrator.py` | Distribui pecas por pilar, produto, persona na semana |
| `atomizer.py` | Nova — atomiza 1 master em 5-8 derivados por plataforma |
| `disaster_check.py` | Shield — 10 quality gates antes de publicar |

**`web/`** — Interface e API (7 modulos)
| Modulo | Funcao |
|--------|--------|
| `app.py` | FastAPI com 90+ endpoints |
| `services.py` | Logica de negocio, cache, CRUD |
| `database_supabase.py` | Persistencia Supabase (PostgreSQL) |
| `database.py` | Persistencia SQLite (fallback) |
| `auth.py` | Autenticacao JWT |
| `settings_store.py` | Armazenamento seguro de API keys (XOR + base64) |
| `models.py` | Modelos de dados (pecas, reviews, settings) |

**`llm/`** — Inteligencia de linguagem (3 modulos)
| Modulo | Funcao |
|--------|--------|
| `openrouter.py` | Cliente OpenRouter com fallback entre modelos |
| `budget_tracker.py` | Controle de custo por peca/dia/mes |
| `journey_log.py` | Diario de bordo de cada peca (custos, modelos, tempos) |

**`nb2/`** — Visual intelligence (3 modulos)
| Modulo | Funcao |
|--------|--------|
| `engine.py` | Motor NB2 — envia prompt + imagem ref para fal.ai |
| `prompt_builder.py` | Construtor de prompt com 8 dimensoes |
| `vdp_loader.py` | Carrega VDPs (fichas visuais de produto) |

**`video/`** — Producao de video (5 modulos)
| Modulo | Funcao |
|--------|--------|
| `minimax_client.py` | Minimax/Hailuo I2V |
| `kling_client.py` | Kling 3.0 I2V |
| `veo3_client.py` | Google Veo 3 |
| `elevenlabs_tts.py` | Narracao por voz |
| `assembler.py` | FFmpeg — montagem final |

**`publishers/`** — Distribuicao (8 modulos)
| Modulo | Funcao |
|--------|--------|
| `instagram.py` | Publicacao no Instagram |
| `linkedin.py` | Publicacao no LinkedIn |
| `facebook.py` | Publicacao no Facebook |
| `youtube.py` | Publicacao no YouTube |
| `batch_approval.py` | Aprovacao em lote |
| `metrics_collector.py` | Coleta de metricas pos-publicacao |
| `feedback_loop.py` | Loop de feedback para melhorar producao |
| `report_pdf.py` | Relatorio semanal em PDF |

### 4.4 Fluxo de Dados

```
YAML Data Files (18 arquivos)
    │
    ▼
init_*_config(data_dir)  ←── chamado na startup
    │
    ▼
_load_*_config()  ←── cache em memoria (module-level)
    │
    ▼
get_*()  ←── acessores usados pelos modulos de automacao
    │
    ▼
Automacao executa com dados dinamicos
    │
    ▼
UI edita via formulario visual → PUT /api/data/{config}
    │
    ▼
services.save_*_config() → grava YAML + invalida cache
```

Quando a gestora edita qualquer configuracao pela UI, o sistema:
1. Recebe o JSON do formulario
2. Grava no arquivo YAML correspondente
3. Invalida o cache do modulo (service-level + module-level)
4. Na proxima geracao, os dados atualizados sao usados automaticamente

### 4.5 Custo por Peca

| Etapa | Custo Medio |
|-------|-------------|
| Briefing (Gemini Flash) | ~$0.01 |
| Copy (Gemini Flash) | ~$0.03 |
| Imagem NB2 (fal.ai FLUX) | ~$0.04-0.08 |
| Video (Minimax) | ~$0.12 |
| **Total por peca completa** | **~$0.20-0.24** |

Para a meta MVP de 5 masters + 25-40 derivados/semana: **~$5-10/semana** ou **~R$25-50/semana**.

---

## 5. Metodologia de Construcao

### 5.1 Pesquisa Fundamentada

Antes de escrever uma linha de codigo, foram realizadas **6 pesquisas profundas**:

1. **Marketing B2B Healthcare 2025-2026** — tendencias, benchmarks, melhores praticas
2. **Content Operations / Producao em Massa** — como escalar producao com qualidade
3. **IA Generativa Visual** — Imagen, Veo, NB2, FLUX — capacidades e limitacoes
4. **Copywriting para Dispositivos Medicos** — regulatorio ANVISA, CFM, linguagem segura
5. **Benchmarking Concorrentes** — o que Mindray, Trumpf, Steris fazem (e nao fazem)
6. **Algoritmos e Formatos por Plataforma** — Instagram, LinkedIn, YouTube, Facebook em 2026

Essas pesquisas geraram um **documento estrategico consolidado** de 1.361 linhas que fundamenta todas as decisoes do sistema.

### 5.2 Squad de Agentes IA

O sistema foi projetado como um **squad de 12 agentes especializados**, cada um com personalidade, regras e responsabilidades definidas:

| Agente | Persona | Responsabilidade |
|--------|---------|-----------------|
| Atlas | Estrategista | Briefings, calendario, distribuicao |
| Vigil | Inteligencia | Monitoramento de mercado e concorrencia |
| Helix | Copywriter | Copy especializado em dispositivos medicos |
| Apex | Visual Designer | Prompts NB2 e composicao visual |
| Flux | Video Producer | Video IA (Minimax, Kling, Veo) |
| Nova | Atomizer | Atomizacao 1→5-8 derivados |
| Shield | Compliance | Gate bloqueante ANVISA/CFM |
| Lens | Quality Editor | Controle de qualidade |
| Bridge | CRM | Integracao Bitrix24, UTM, leads |
| Tempo | Production Manager | Orquestracao do pipeline |
| Echo | Publisher | Publicacao em 6 plataformas |
| Pulse | Performance | Feedback loop e auto-aprendizado |

### 5.3 Pipeline Ciclico

O conteudo flui por um pipeline ciclico com feedback:

```
BRIEFING → COPY → DESIGN → VIDEO → ATOMIZAR → QUALITY → COMPLIANCE → PUBLICAR
    ↑                                                                      │
    └──────────────── PERFORMANCE FEEDBACK ←───────────────────────────────┘
```

As metricas de performance alimentam o proximo ciclo de briefing, criando um loop de melhoria continua.

### 5.4 3 Camadas de Execucao

| Camada | % | O Que Faz |
|--------|---|-----------|
| **Workers** | ~40% | Tarefas deterministicas (FFmpeg, UTM, resize, export) — custo zero de IA |
| **Agentes IA** | ~45% | Tarefas criativas (copy, prompts, briefings) — via OpenRouter/fal.ai |
| **Humanos** | ~15% | 3 gates de aprovacao (compliance alto risco, mudanca de estrategia, risco de marca) |

### 5.5 Evolucao do PRD

O projeto passou por iteracoes de aprendizado:

**PRD v1.0** (marco 2026): Meta ambiciosa de 227-265 pecas/mes. MVP W13 foi cancelado por qualidade insuficiente.

**PRD v2.0** (marco 2026): Incorporou 13 feedbacks reais + licoes do cancelamento:
- Volume MVP reduzido para 5 masters + 25-40 derivados/semana
- Atomizacao ajustada de 1:17-20 para 1:5-8
- ETRUS bloqueado ate lancamento oficial
- Regras de fidelidade visual (NB2 nunca wallpaper, LEV luz focada)
- Regra de logo Mendel=tecnico, Salk=comercial
- Review intermediario antes do design
- 42 claims rastreavies aos manuais ANVISA

---

## 6. O Que Torna Este Projeto Unico

### 6.1 Zero Invencao

Nenhum claim, spec ou argumento e inventado pelo sistema. Todos os 42 claims sao rastreavies a documentos oficiais (manuais ANVISA, registros, analises competitivas). Quando a IA gera copy, ela so pode usar argumentos do banco aprovado.

### 6.2 Compliance Nativo

O compliance nao e uma etapa posterior — esta embutido em cada modulo:
- Copywriters tem regras de termos proibidos no prompt
- Geracao de imagem tem negativos obrigatorios (nunca concorrente, nunca pessoas)
- Quality gate bloqueia automaticamente 6 tipos de violacao
- Termos proibidos sao verificados contra 5 categorias de risco

### 6.3 Multi-Marca com Identidade Preservada

Cada marca tem brandbook, tom, copywriter, paleta, regras visuais e personas proprias. O mesmo sistema produz conteudo tecnico para engenheiros (Mendel) e conteudo institucional acolhedor (Manager Grupo) sem confundir identidades.

### 6.4 Produto Real na Cena

A tecnica NB2 integra o produto real (foto PNG) dentro de cenarios gerados por IA. Nao e wallpaper com produto colado por cima. A IA renderiza o produto como parte da cena, mantendo fidelidade de cor e proporcao.

### 6.5 Autonomia Total da Gestora

Toda variavel estrategica e editavel pela interface web — desde o tom de voz de cada marca ate os negativos de prompt de imagem. A gestora de marketing pode ajustar qualquer parametro sem depender de desenvolvedor.

### 6.6 Custo Marginal Proximo de Zero

Apos o investimento inicial de construcao, cada peca de conteudo custa ~R$1. Para uma empresa que pagaria R$500-2.000/peca em agencia, isso representa uma reducao de custo de 99%.

---

## 7. Equipe e Papeis

| Pessoa | Papel no Projeto |
|--------|-----------------|
| **Gisele** | Diretora, Marketing, SGQI — define estrategia, aprova conteudo, feedback |
| **Bruno** | Inteligencia de Marketing — construiu o sistema, configura regras, opera |
| **Audrey** | Design Digital — composicao final no Canva (logo, texto, ajustes) |

O sistema foi projetado para que Bruno configure as regras e Gisele/Audrey operem o dia a dia sem precisar de conhecimento tecnico.

---

## 8. Estado Atual e Proximos Passos

### Entregue

- Sistema web completo e em producao (studio.salkmedical.com)
- 90+ endpoints API
- 18 arquivos YAML de configuracao editaveis pela UI
- Pipeline de geracao: briefing → copy → imagem → video → atomizacao
- Quality gate com 10 verificacoes automaticas
- 4 brandbooks, 42 claims, 4 buyer personas, banco de hashtags
- Specs de 6 plataformas, calendario editorial, UTM patterns
- Autenticacao JWT, banco Supabase, deploy Docker em VPS

### Em Andamento

- Calibracao de qualidade visual NB2 (prompts otimizados por produto)
- Batch de producao piloto (5 masters Salk)
- Publicacao automatica via APIs de plataformas

### Futuro

- Feedback loop automatico (metricas → ajuste de estrategia)
- Video Producer avancado (narracao + legendas + transicoes)
- Integracao CRM Bitrix24 (leads por UTM)
- Manager Grupo e Dayho (apos validacao Salk/Mendel)
- Relatorio semanal automatico em PDF

---

## 9. Resumo Executivo

O Content Studio transforma o Manager Grupo de uma empresa com presenca digital quase nula em uma **fabrica de conteudo profissional** capaz de produzir ~48 pecas/semana para 4 marcas e 6 plataformas.

O sistema combina:
- **IA generativa** (texto, imagem, video) para escala
- **Regras de negocio rigidas** (42 claims, 20+ termos proibidos, 10 quality gates) para compliance
- **Interface visual intuitiva** para que a gestora de marketing opere sem dependencia tecnica
- **Custo marginal de ~R$1/peca** vs R$500-2.000/peca em agencia

Tudo isso fundamentado em 6 pesquisas profundas de mercado e iterado com feedback real da equipe e da diretoria.

---

> **Fonte tecnica completa:** Ver `docs_user/REGRAS-DE-NEGOCIO-COMPLETAS.md` para todas as variaveis estrategicas do sistema.
