# PRD — Sistema de Producao de Conteudo para Redes Sociais

**Projeto:** Manager Grupo — Producao Profissional de Conteudo B2B Healthcare
**Versao:** 2.0
**Status:** Aprovado
**Data:** 2026-03-25
**Autor:** @pm (Morgan) / Orion (aiox-master)
**Revisao:** Incorpora todas as licoes aprendidas do Epico 0, batch W13 (cancelado), sessoes de calibracao NB2, e 13 feedbacks validados
**Fonte:** docs/ESTRATEGIA-PRODUCAO-CONTEUDO.md, docs/MAPEAMENTO_ORGANIZACIONAL.md, 5 relatorios de pesquisa, 21 memorias de feedback

---

## 1. Background

O Manager Grupo e um conglomerado B2B do setor de saude com sede em Sao Jose dos Pinhais/PR, composto por 4 empresas ativas (Dayho fabrica pecas, Mendel Medical monta equipamentos medicos com registro ANVISA, Salk Medical comercializa, Manager Grupo coordena). O projeto consiste na producao profissional de conteudo para redes sociais das 4 marcas, operando em 4 plataformas (Instagram, LinkedIn, YouTube, Facebook), totalizando 16 canais ativos.

**Fonte:** docs/MAPEAMENTO_ORGANIZACIONAL.md (linhas 1-57)

### Oportunidade de Mercado

Nenhum fabricante nacional de equipamentos medicos possui presenca digital consistente e profissional em redes sociais. Concorrentes diretos (KSS, OQTIS, MEDLIGHT, MEDPEJ, BARRFAB) tem presenca minima ou amadora — oportunidade de first-mover advantage.

**Fonte:** docs/ESTRATEGIA-PRODUCAO-CONTEUDO.md (linhas 30-46)

### Marcas e Prioridades

| Prioridade | Marca | Foco | Pecas/Semana (MVP) | Pecas/Mes (Regime) |
|:----------:|-------|------|:------------------:|:------------------:|
| 1 | Salk Medical | Comercial / Vendas | 3-4 | 120-160 |
| 2 | Mendel Medical | Autoridade / Fabricante | 2-3 | 80-100 |
| 3 | Manager Grupo | Institucional / Employer Branding | 1 | 20-30 |
| 4 | Dayho | Autoridade Industrial | 0-1 | 10-15 |
| **TOTAL** | | | **6-9** | **230-305** |

> **REVISAO v2.0:** Metas de regime (230-305/mes) mantidas como norte estrategico. MVP opera com metas semanais realisticas (5 masters + derivados). Escalar baseado em dados reais, nao projecoes.

**Fonte:** docs/ESTRATEGIA-PRODUCAO-CONTEUDO.md (linhas 19-27), Reuniao Squad 2026-03-17

### Cadeia de Valor

```
Dayho (fabrica pecas) → Mendel Medical (monta + ANVISA) → Salk Medical (comercializa) → Hospitais
```

### Produtos Publicaveis (MVP)

| Produto | Marca Comercial | Marca Tecnica | Status | Claims Aprovados |
|---------|----------------|---------------|--------|:----------------:|
| **LEV** (Foco Cirurgico) | Salk Medical | Mendel Medical | PUBLICAVEL | 13 |
| **KRATUS** (Mesa Cirurgica) | Salk Medical | Mendel Medical | PUBLICAVEL | 10+ |
| **OSTUS** (Serra Cirurgica) | Salk Medical | Mendel Medical | PUBLICAVEL | 3 |
| **KRONUS** (Suporte) | Salk Medical | Mendel Medical | PUBLICAVEL | 3 |
| ~~ETRUS~~ | — | — | **BLOQUEADO** | — |
| ~~COMMAND~~ | — | — | **RESTRITO** | 2 |

> **REGRA INEGOCIAVEL:** ETRUS NAO foi lancado. PROIBIDO publicar qualquer conteudo sobre ele. COMMAND e integrado ao ETRUS — verificar se pode ser divulgado independentemente antes de incluir.

**Fonte:** Feedback diretora 2026-03-17

---

## 2. Goals

### 2.1 Objetivo Principal

Produzir conteudo de qualidade profissional de advertising para 16 canais (4 marcas x 4 plataformas), com compliance ANVISA total, escalando volume progressivamente baseado em dados de performance reais.

### 2.2 Principio Fundamental: Qualidade > Volume

> **30 pecas a score 9.0 > 60 pecas a score 6.0**

O sistema prioriza qualidade de advertising real sobre volume. Cada peca deve competir por atencao em feed de redes sociais — nao e panfleto tecnico. E conteudo que precisa ter conceito, impacto visual, storytelling de marca.

**Fonte:** Reuniao Squad 2026-03-17, Feedback MVP cancelado W13

### 2.3 Objetivos Secundarios

- Preencher vazio digital identificado no setor de equipamentos medicos nacionais
- Posicionar produtos como referencia em qualidade e inovacao
- Gerar leads qualificados via funil social → CRM (Bitrix24)
- Estabelecer thought leadership no segmento B2B healthcare
- Construir biblioteca de assets visuais reutilizaveis (NB2 hero shots)

---

## 3. Functional Requirements

### FR-001: Volume de Producao Progressivo
**Descricao:** Producao escala progressivamente: Semana 1-2 = calibracao (5 masters + 15-40 derivados). Semana 3+ = escalar baseado em metricas reais. Meta de regime = 227-265 pecas/mes.
**Detalhamento:** Salk Medical (prioridade maxima), Mendel Medical (alta), Manager Grupo (baixa), Dayho (minima).
**Fonte:** Reuniao Squad 2026-03-17

### FR-002: Copy Baseado em Claims Pre-Aprovados
**Descricao:** Todo conteudo tecnico deve usar EXCLUSIVAMENTE claims do banco pre-aprovado (IDs: LEV-XX, KR-XX, OS-XX, KN-XX, CMP-XX).
**Detalhamento:** Claims derivam de manuais tecnicos oficiais registrados na ANVISA. Nenhum claim inventado e permitido (Constitution Article IV).
**Fonte:** docs/ESTRATEGIA-PRODUCAO-CONTEUDO.md (linhas 387-430)

### FR-003: Visual com Product-in-Scene (NB2)
**Descricao:** Producao visual usa tecnica NB2 (Nano Banana 2): upload da imagem REAL do produto como referencia no AI Studio, IA renderiza o produto DENTRO do cenario/conceito com iluminacao, reflexos e sombras coerentes.
**Detalhamento:**
- Produto SEMPRE real (PNG original uploadado como referencia)
- IA renderiza o produto INTEGRADO na cena (NAO e wallpaper + colagem)
- Descrever APENAS o cenario/ambiente no prompt — NUNCA descrever o produto
- Sem pessoas geradas por IA. Sem cenas clinicas com IA
- Pensar como ADVERTISING: qual conceito/ideia/historia valoriza o produto?
**Fonte:** Sessoes NB2 2026-03-17/18, Feedback validado

### FR-004: Gate de Compliance Bloqueante
**Descricao:** Shield (compliance-guardian) opera gate BLOQUEANTE — nenhuma peca e publicada sem aprovacao nas 4 camadas de QC.
**Detalhamento:** Camada 1 (automatizada), Camada 2 (editorial/Lens), Camada 3 (tecnica/medica/Shield), Camada 4 (legal/compliance/Shield).
**Fonte:** docs/ESTRATEGIA-PRODUCAO-CONTEUDO.md (linhas 759-800)

### FR-005: Atomizacao Cross-Platform Realista
**Descricao:** Cada master piece atomizada em 5-8 derivados cross-platform (NAO 17-20). Carousel e PDF sao conteudo ORIGINAL, nao derivados.
**Detalhamento:** Nunca cross-post identico. Cada derivado adapta copy, formato, tom, dimensao e CTA para a plataforma destino. Ratio realista: 1:5-8.
**Fonte:** Reuniao Squad 2026-03-17

### FR-006: Feedback Loop Semanal
**Descricao:** Pulse (performance-analyst) analisa metricas pos-publicacao e alimenta Atlas (content-strategist) com insights para otimizacao continua.
**Detalhamento:** Ciclo fecha semanalmente: publicacao → metricas → insights → ajuste de calendario/briefing.
**Fonte:** docs/ESTRATEGIA-PRODUCAO-CONTEUDO.md (linhas 1125-1172)

### FR-007: Pipeline em Batch Semanal com Review Intermediario
**Descricao:** Producao segue ciclo semanal com review intermediario OBRIGATORIO apos copy:
1. Segunda: Planejamento + Calendarios (Atlas)
2. Terca: Copywriting (Helix) + **Review Intermediario (Lens)**
3. Quarta: Visual Production (Apex)
4. Quinta: Atomizacao (Nova) + Review Final (Lens + Shield)
5. Sexta: Ajustes + Agendamento (Usuario)
**Fonte:** Pipeline v2.0, Reuniao Squad 2026-03-17

### FR-008: Calendario Editorial por Marca
**Descricao:** Atlas gera calendario editorial semanal por marca, cruzando pilares x formatos x plataformas.
**Detalhamento:** Frequencia MVP: Salk (3-4x/semana), Mendel (2-3x/semana), Manager (1x/semana), Dayho (0-1x/semana).
**Fonte:** docs/ESTRATEGIA-PRODUCAO-CONTEUDO.md (linhas 142-181)

### FR-009: Tom de Voz por Marca
**Descricao:** Cada marca tem tom de voz distinto que deve ser respeitado em todo conteudo.
**Detalhamento:** Salk (consultivo), Mendel (tecnico), Manager (acolhedor), Dayho (industrial).
**Fonte:** docs/ESTRATEGIA-PRODUCAO-CONTEUDO.md (linhas 328-336)

### FR-010: Copy por Buyer Persona
**Descricao:** Copy deve ser adaptado por buyer persona: Compras/Suprimentos, Engenharia Clinica, Equipe Medica, Administradores Hospitalares.
**Fonte:** docs/ESTRATEGIA-PRODUCAO-CONTEUDO.md (linhas 337-371)

### FR-011: Frameworks de Copy
**Descricao:** Usar frameworks de copy adequados por formato: PAS, AIDA, BAB, StoryBrand, SPIN adaptado.
**Fonte:** docs/ESTRATEGIA-PRODUCAO-CONTEUDO.md (linhas 275-326)

### FR-012: Hashtags Estrategicas
**Descricao:** Aplicar estrategia escada de hashtags por marca/plataforma (core + produto + nicho).
**Fonte:** docs/ESTRATEGIA-PRODUCAO-CONTEUDO.md (linhas 1210-1249)

### FR-013: Visual Delivery Pack (VDP) Completo [NOVO v2.0]
**Descricao:** Cada imagem entregue DEVE conter pack completo de instrucoes:
1. Prompt NB2 otimizado (arquitetura 8 dimensoes)
2. Task padrao: remover marca d'agua do Google
3. Instrucao de composicao Canva completa:
   - Texto exato, localizacao, fonte, tamanho, alinhamento, cor HEX
   - Logo: qual, onde, tamanho, efeitos
   - Efeitos: quais, onde, parametros
   - TUDO especificado — nada subjetivo
**Fonte:** Feedback Padroes de Qualidade 2026-03-16

### FR-014: Regra de Logo por Tipo de Conteudo [NOVO v2.0]
**Descricao:** Logo no conteudo depende do TIPO, nao da campanha:
- **Mendel Medical** → conteudo tecnico, specs, fabricacao, engenharia, Ra/R9, normas, bastidores
- **Salk Medical** → conteudo comercial, vendas, preco, atendimento, cases, licitacoes
**Regra pratica:** se tem numero tecnico (Ra, kg, mm, horas, lux) → Mendel. Se tem CTA de venda → Salk.
**Fonte:** Feedback diretora 2026-03-17

---

## 4. Non-Functional Requirements

### NFR-001: Velocidade de Producao
**Descricao:** Pipeline semanal completo em 5 dias uteis. Tempo medio por peca master < 2.5h.
**Fonte:** docs/ESTRATEGIA-PRODUCAO-CONTEUDO.md (linhas 849-861)

### NFR-002: Aprovacao First-Pass
**Descricao:** >= 70% das pecas aprovadas sem retrabalho na primeira passagem (meta MVP). Meta de regime: >= 85%.
**Fonte:** Reuniao Squad 2026-03-17 (meta ajustada para MVP)

### NFR-003: Zero Violacoes de Compliance
**Descricao:** 100% das pecas publicadas em conformidade com ANVISA/CFM. Zero violacoes. Inegociavel.
**Fonte:** docs/ESTRATEGIA-PRODUCAO-CONTEUDO.md (linha 859)

### NFR-004: Brand Consistency
**Descricao:** Score de brand consistency > 90% em auditoria periodica.
**Fonte:** docs/ESTRATEGIA-PRODUCAO-CONTEUDO.md (linha 860)

### NFR-005: Engagement Targets (Regime)
**Descricao:** Instagram > 4.0%, LinkedIn > 3.5%, Facebook > 2.0%, YouTube > 4% completion rate.
**Meta MVP:** Instagram > 2%, LinkedIn > 1.5% (baseline para calibracao).
**Fonte:** docs/ESTRATEGIA-PRODUCAO-CONTEUDO.md (linhas 821-828)

### NFR-006: Qualidade Visual NB2
**Descricao:** Imagens NB2 devem atingir qualidade de advertising profissional. Testes de qualidade visual devem passar pela aprovacao do usuario ANTES de escalar para batch.
**Criterio:** Hero shot aprovado = referencia para o produto. Se reprovado, iterar prompt (V2, V3...) ate acertar.
**Fonte:** Feedback MVP cancelado W13

---

## 5. Constraints

### CON-001: Custo Operacional Minimo (MVP)
**Descricao:** MVP opera com Claude Code + Google AI Studio (Gemini) + Canva Pro. Total: ~R$180/mes.
**Fonte:** docs/ESTRATEGIA-PRODUCAO-CONTEUDO.md (linhas 489-498)

### CON-002: Operador Unico
**Descricao:** Sistema operado por uma unica pessoa (o usuario), com assistencia de agentes IA. Sem equipe de marketing dedicada.
**Fonte:** Contexto do projeto

### CON-003: Regulamentacao ANVISA
**Descricao:** Todo conteudo sobre dispositivos medicos deve estar em conformidade com RDC 96/2008, RDC 751/2022, RDC 848/2024. CFM Resolucao 2.336/2023.
**Fonte:** docs/ESTRATEGIA-PRODUCAO-CONTEUDO.md (linhas 451-482)

### CON-004: Produto Real em Imagens
**Descricao:** Produto na imagem SEMPRE deve ser a foto real (PNG uploadado como referencia). IA renderiza o produto INTEGRADO no cenario. NUNCA gerar wallpaper + colar PNG no Canva (PROIBIDO). Sem pessoas geradas por IA. Sem cenas clinicas com IA.
**Fonte:** Feedback NB2 2026-03-17/18

### CON-005: Semi-Manual no MVP
**Descricao:** No MVP, publicacao e manual (Meta Business Suite, LinkedIn, YT Studio). Automacao via API vem na Fase 3.
**Fonte:** docs/ESTRATEGIA-PRODUCAO-CONTEUDO.md (linhas 970-998)

### CON-006: Claims Verificaveis
**Descricao:** Nenhum dado tecnico pode ser inventado. Tudo deve ser rastreavel a manuais oficiais, fichas tecnicas registradas na ANVISA, ou documentacao institucional.
**Fonte:** Constitution Article IV (No Invention)

### CON-007: API Limits
**Descricao:** Google AI Studio: limites do plano. Canva Pro: uso individual.
**Fonte:** docs/ESTRATEGIA-PRODUCAO-CONTEUDO.md (linhas 489-498)

### CON-008: ETRUS Bloqueado [NOVO v2.0]
**Descricao:** ETRUS NAO foi lancado. PROIBIDO publicar qualquer conteudo sobre ele. COMMAND e integrado ao ETRUS — verificar independencia antes de incluir. Foco EXCLUSIVO em LEV, KRATUS, OSTUS, KRONUS e conteudo institucional.
**Fonte:** Feedback diretora 2026-03-17

### CON-009: Sem Scripts Locais em Producao [NOVO v2.0]
**Descricao:** Workers/automacoes NAO podem depender de maquina local. Infraestrutura: GitHub Actions, VPS da empresa, APIs nativas (Meta, Google, LinkedIn), Bitrix24.
**Fonte:** Feedback infraestrutura 2026-03-16

---

## 6. Regras de Producao Visual — NB2 [NOVO v2.0]

Esta secao codifica TODAS as regras validadas para producao visual com NB2 (Nano Banana 2).

### 6.1 Arquitetura de Prompt — 8 Dimensoes

Todo prompt NB2 DEVE seguir a arquitetura de 8 dimensoes do Apex:

| # | Dimensao | Descricao | Exemplo |
|---|----------|-----------|---------|
| 1 | **Subject** | Produto uploadado como referencia | "Place this EXACT uploaded product in the scene" |
| 2 | **Action** | O que o produto esta fazendo na cena | "Positioned on a dark reflective surface" |
| 3 | **Setting** | Ambiente/cenario ao redor | "Professional photo studio with dark background" |
| 4 | **Lighting** | Esquema de iluminacao detalhado | "Three-point lighting: key light 45deg..." |
| 5 | **Camera** | Camera e lente especificas | "Hasselblad X2D, 80mm f/2.8 macro" |
| 6 | **Style** | Estilo fotografico/artistico | "Commercial product photography, editorial" |
| 7 | **Mood** | Atmosfera e sentimento | "Premium, authoritative, clinical precision" |
| 8 | **Technical** | Specs de output | "Aspect ratio 4:5, 1080x1350, no text no logos" |

### 6.2 Tecnica Validada — Dramatic Studio (LEV)

Para hero shots de LEV (foco cirurgico):
- Fundo escuro + piso reflexivo com reflexo do produto
- Rim light azul sutil nas bordas do housing branco (separa do fundo)
- Three-point lighting descrito em detalhe (key, fill, rim)
- Camera e lente reais nomeadas
- Produto como 60-70% do frame

### 6.3 Regras Inegociaveis de NB2

| Regra | Descricao | Consequencia |
|-------|-----------|--------------|
| **Nunca descrever o produto** | Descrever APENAS cenario/ambiente | Produto distorce se descrito |
| **Nunca wallpaper+colagem** | Produto INTEGRADO na cena via upload | Colagem = amadorismo = PROIBIDO |
| **Nunca equipamento concorrente** | Negative prompt obrigatorio | Produto generico = concorrente no material |
| **Nunca luz dispersa (LEV)** | Luz FOCADA para baixo, concentrada | Raios laterais = luz desperdicada = contradiz produto |
| **Nunca glow/rays (LEV)** | Sem "dramatic glow", "light spreading" | Luz lateral = falha optica para o publico-alvo |
| **Nunca cenario vazio** | Produto JA integrado na cena | Cenario vazio = Anti-Pattern 1 do Apex |
| **Nunca texto/logo via IA** | Adicionar no Canva depois | IA gera texto ilegivel |
| **Nunca pessoas via IA** | Sem rostos, maos, corpos gerados | Uncanny valley em healthcare = risco |

### 6.4 Negative Prompt Obrigatorio

Todo prompt NB2 DEVE incluir:
```
no text, no logos, no watermarks, no brand names, no people, no hands, no faces,
surgical lights, ceiling lights, overhead lamps, medical lamps, other medical devices,
competitor products, ceiling mounted equipment
```

### 6.5 Preservacao de Fidelidade do Produto

- Instruir explicitamente: "Place this EXACT uploaded product in the scene. Do NOT modify the product design, shape, materials, colors, or proportions"
- Manter prompt de ambiente simples — complexidade excessiva = Gemini toma liberdade com o produto
- Se resultado distorcer, ITERAR prompt (V2, V3...) — NUNCA abandonar NB2

### 6.6 Composicao Canva — Regras Validadas

| Elemento | Especificacao |
|----------|--------------|
| **Margens** | 60px (5.5% da largura) |
| **Logo** | 180-200px largura minima |
| **Headline** | 36pt bold, alinhado a esquerda, topo |
| **Spec line** | 18-20pt light, branco 70% opacidade, tracking +80-100, centralizado rodape |
| **ANVISA badge** | 12-14pt, branco 50% opacidade, canto inferior direito |
| **Gradientes** | Preto→transparente: topo (40-60%), rodape (50-70%) |
| **Zona protegida** | NUNCA texto sobre produto ou reflexo |

---

## 7. Pipeline de Producao v2.0

### 7.1 Fluxo com Review Intermediario

```
Atlas (Briefing) → Helix (Copy) → Lens (Review Intermediario) → Apex (Visual/NB2)
     → Nova (Atomizacao) → Lens (Review Final) → Shield (Compliance BLOQUEANTE)
     → Usuario (Publicacao Manual)
```

### 7.2 Stages Detalhados

| Stage | Agente | Input | Output | Gate |
|-------|--------|-------|--------|------|
| 1. Briefing | Atlas | Calendario + Claims | Briefs estruturados | — |
| 2. Copywriting | Helix | Briefs + Claims Bank | Copy sets por formato | — |
| 3. **Review Intermediario** | Lens | Copy sets | Copy aprovado/revisado | Soft gate |
| 4. Visual Design | Apex | Copy aprovado + PNGs | Visual Delivery Packs | — |
| 5. Atomizacao | Nova | Masters + Copy | 5-8 derivados/master | — |
| 6. Review Final | Lens | Pacote completo | QC layers 1-2 | Soft gate |
| 7. Compliance | Shield | Pacote revisado | Aprovacao/Rejeicao | **BLOCKING** |
| 8. Publicacao | Usuario | Pecas aprovadas | Posts publicados | Human gate |

### 7.3 Ciclo Semanal

| Dia | Atividade | Agentes |
|-----|-----------|---------|
| Segunda | Planejamento + Calendario Editorial | Atlas |
| Terca | Copywriting + Review Intermediario | Helix → Lens |
| Quarta | Producao Visual NB2 | Apex |
| Quinta | Atomizacao + Review Final + Compliance | Nova → Lens → Shield |
| Sexta | Ajustes Finais + Agendamento | Usuario |

---

## 8. Squad de Producao v2.0

### 8.1 Agentes MVP (8 Core)

| Tier | Persona | ID | Papel | Status |
|:----:|---------|-----|-------|--------|
| 1 | **Atlas** | content-strategist | Chief Content Strategist & Pipeline Orchestrator | ATIVO |
| 2 | **Helix** | medical-copywriter | Specialized Medical Device Copywriter | ATIVO |
| 2 | **Apex** | visual-designer | Elite Visual Designer — NB2 & Advertising Creative | ATIVO |
| 2 | **Nova** | content-atomizer | Content Atomization & Cross-Platform | ATIVO |
| 3 | **Shield** | compliance-guardian | Regulatory Compliance Guardian (ANVISA/CFM) | ATIVO |
| 3 | **Lens** | quality-editor | Chief Editor & Quality Control | ATIVO |
| 4 | **Tempo** | production-manager | Production Manager & Pipeline Controller | ATIVO |
| 4 | **Pulse** | performance-analyst | Performance Analyst & Feedback Loop | ATIVO |

### 8.2 Agentes Diferidos (Mes 2+)

| Persona | ID | Motivo Diferimento |
|---------|-----|-------------------|
| Vigil | market-intelligence | Atlas absorve via docs existentes |
| Flux | video-producer | MVP focado em imagem estatica |
| Bridge | crm-integration | UTMs manuais + CTA guidelines |
| Echo | platform-publisher | Publicacao manual no MVP |

---

## 9. Ativos Disponiveis

### 9.1 Biblioteca de Imagens

| Categoria | Quantidade | Path |
|-----------|:----------:|------|
| LEV (Foco Cirurgico) | 164 | docs_user/imagem_produtos/ |
| KRATUS (Mesa) | 60 | docs_user/imagem_produtos/ |
| OSTUS (Serra) | 32 | docs_user/imagem_produtos/ |
| KRONUS (Suporte) | 27 | docs_user/imagem_produtos/ |
| Command | 15 | docs_user/imagem_produtos/ |
| Outros | 42 | docs_user/imagem_produtos/ |
| **TOTAL** | **340** | |

### 9.2 Logos

| Marca | Quantidade | Formatos |
|-------|:----------:|----------|
| Mendel Medical | 13 | AI, EPS, CDR, PNG |
| Salk Medical | 7 | PNG |
| Manager Grupo | 5 | PNG |
| Dayho | 2 | PNG |

### 9.3 Documentacao Tecnica

- 5 manuais PDF de produtos
- 2 portfolios comerciais
- 7 analises competitivas detalhadas
- 7.266 linhas de pesquisa estrategica

### 9.4 Data Files (Squad)

| Arquivo | Conteudo | Path |
|---------|----------|------|
| claims-bank.yaml | 40+ claims pre-aprovados por produto | squads/content-production/data/ |
| brand-guidelines.yaml | Tom de voz, identidade visual, 4 marcas | squads/content-production/data/ |
| buyer-personas.yaml | 4 personas com pain points e CTAs | squads/content-production/data/ |
| platform-specs.yaml | Dimensoes e specs por plataforma | squads/content-production/data/ |
| hashtag-bank.yaml | Estrategia escada por marca | squads/content-production/data/ |
| utm-patterns.yaml | Templates UTM + CTA por funil | squads/content-production/data/ |
| prohibited-terms.yaml | Termos proibidos ANVISA/CFM | squads/content-production/data/ |
| editorial-calendar-template.yaml | Template de calendario semanal | squads/content-production/data/ |

---

## 10. Epic Roadmap

| Epico | Nome | Objetivo | Semanas | Status |
|:-----:|------|----------|:-------:|--------|
| 0 | Fundacao & Governanca | PRD + data files + tasks + validacao | 1 | **COMPLETO** |
| 1 | Calibracao & Primeiro Batch — Salk/Mendel | Calibrar qualidade, 20-40 pecas reais | 2-4 | **PROXIMO** |
| 2 | Escala + Marcas Adicionais | Atingir 50% volume, adicionar Manager/Dayho | 5-7 | Planejado |
| 3 | Video + Volume Total | Ativar Flux, 100% volume | 8-10 | Planejado |
| 4 | Automacao & Feedback Loop | Workers, APIs, Pulse em operacao plena | 11-13 | Planejado |

### 10.1 Epico 1 — Detalhamento

**Fase 1: Calibracao (Semanas 2-3)**
- Provar qualidade NB2 em 2-3 pecas individuais (hero shots LEV + KRATUS)
- Validar pipeline completo end-to-end com 1 peca
- Calibrar baseline de qualidade e tempo
- Aprovacao do usuario em cada peca antes de escalar

**Fase 2: Primeiro Batch (Semanas 3-4)**
- Batch semanal: 5 masters + 25-40 derivados
- Salk Medical (3 masters) + Mendel Medical (2 masters)
- Pipeline completo: brief → copy → review → visual → atomize → QC → compliance
- Publicacao real e coleta de metricas

**Fase 3: Otimizacao (Semana 4+)**
- Pulse analisa metricas de engajamento
- Ajustar calendario, pilares e formatos baseado em dados
- Definir metas de escala para Epico 2

---

## 11. Success Metrics — Epico 1

### 11.1 Fase Calibracao

| Metrica | Target |
|---------|--------|
| Hero shots NB2 aprovados | >= 2 (LEV + KRATUS) |
| Pipeline end-to-end validado | 1 peca completa |
| Qualidade visual (aprovacao usuario) | 100% |
| Zero violacoes compliance | 0 |

### 11.2 Fase Primeiro Batch

| Metrica | Target |
|---------|--------|
| Pecas master produzidas | >= 5/semana |
| Derivados por master | 5-8 |
| Pipeline completo | <= 5 dias uteis |
| Aprovacao first-pass (Shield) | >= 70% |
| Violacoes compliance | 0 |
| Engagement 7d (IG) | > 2% |
| Engagement 7d (LI) | > 1.5% |
| Tempo medio/peca master | < 3h end-to-end |

---

## 12. Out of Scope (MVP)

- Video production (diferido para Epico 3)
- Market intelligence automatizada (Atlas absorve com docs existentes)
- CRM integration automatizada (UTMs manuais, CTA guidelines em data file)
- Publicacao automatizada (manual via Meta Business Suite)
- Automacao via API (Fase 3)
- Conteudo sobre ETRUS (produto nao lancado)
- Conteudo sobre COMMAND (vinculado ao ETRUS — verificar independencia)
- Scripts/workers em maquina local (usar GitHub Actions, VPS, APIs)

---

## 13. Risks & Mitigations

| Risco | Probabilidade | Mitigacao |
|-------|:------------:|-----------|
| NB2 gera produto distorcido | Media | Iterar prompt (V2, V3...), arquitetura 8 dimensoes, nunca descrever produto |
| Compliance ANVISA violada | Baixa | Gate bloqueante Shield + claims pre-aprovados + prohibited-terms.yaml |
| Volume insustentavel para operador unico | Media | Atomizacao 1:5-8 + batch production + templates Canva + escala progressiva |
| Qualidade inconsistente entre marcas | Media | Brand guidelines + Lens review intermediario + checklists |
| Claims desatualizados | Baixa | Banco versionado + revisao periodica Shield |
| Equipamento concorrente em imagens NB2 | Media | Negative prompt obrigatorio + cenarios controlados (studio, clean bg) |
| Engagement abaixo do benchmark | Media | Feedback loop Pulse → Atlas + calibracao nas semanas 1-2 |
| ETRUS publicado acidentalmente | Baixa | Regra bloqueante em Shield + exclusao de claims-bank MVP |

---

## 14. Pre-Requisitos Bloqueantes (Epico 1)

Antes de iniciar producao real, confirmar:

- [ ] Product PNGs recortados (LEV, KRATUS) disponiveis com fundo transparente
- [ ] Teste NB2 end-to-end com 1 produto real aprovado pelo usuario
- [ ] Templates Canva base criados (feed 1080x1350, stories 1080x1920)
- [ ] Paleta de cores HEX definida por marca (verificar brand-guidelines.yaml)
- [ ] claims-bank.yaml atualizado (sem ETRUS, sem claims inconsistentes)
- [ ] Pipeline testado end-to-end com 1 peca completa

---

**Documento gerado a partir de fontes verificadas (Article IV — No Invention)**
**PRD v2.0 — 2026-03-25**
**Incorpora 13 feedbacks validados + licoes aprendidas Epico 0 + Reuniao Squad 2026-03-17**
