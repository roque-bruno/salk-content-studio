# Relatorio: IA Generativa para Producao Visual e de Video
## Pesquisa Profunda — Marco 2026

**Contexto:** Fabricante de equipamentos medicos com ~340 imagens de produtos (PNG fundo transparente): focos cirurgicos, mesas cirurgicas, serras, suportes. Objetivo: criar posts profissionais, carousels, reels e stories em massa.

---

## Indice

1. [Google Imagen 3/4 e Nano Banana 2](#1-google-imagen-34-e-nano-banana-2)
2. [Google Veo 3 / Veo 3.1](#2-google-veo-3--veo-31)
3. [Tecnicas de Composicao com Product Shots](#3-tecnicas-de-composicao-com-product-shots)
4. [Workflows de Producao Visual com IA](#4-workflows-de-producao-visual-com-ia)
5. [Alternativas e Complementos](#5-alternativas-e-complementos)
6. [Geracao de Videos a partir de Imagens Estaticas](#6-geracao-de-videos-a-partir-de-imagens-estaticas)
7. [Templates de Design com IA](#7-templates-de-design-com-ia)
8. [Limitacoes e Cuidados — Dispositivos Medicos](#8-limitacoes-e-cuidados--dispositivos-medicos)
9. [MVP sem API](#9-mvp-sem-api)
10. [Escalabilidade via API](#10-escalabilidade-via-api)
11. [Recomendacoes Praticas](#11-recomendacoes-praticas)

---

## 1. Google Imagen 3/4 e Nano Banana 2

### Evolucao dos Modelos Google

| Modelo | Lancamento | Resolucao Max | Texto | Destaque |
|--------|-----------|---------------|-------|----------|
| Imagen 3 | 2024 | 1024x1024 | Basico | Fotorrealismo avancado |
| Imagen 4 Standard | Mai 2025 (I/O) | 2048x2048 | 95% precisao | Texturas, reflexos, tecidos |
| Imagen 4 Fast | Mai 2025 | 1408x768 | Bom | ~2.7s latencia |
| Imagen 4 Ultra | Mai 2025 | 2K+ | Excelente | Qualidade maxima |
| Nano Banana (original) | Ago 2025 | 1024x1024 | Bom | 13M usuarios em 4 dias |
| Nano Banana Pro | Nov 2025 | 2K | Excelente | Gemini 3 Pro Image |
| Nano Banana 2 | Fev 2026 | 1024x1024 | Muito bom | Velocidade + qualidade |

### O que e "Nano Banana"

Nano Banana e o codinome do modelo de geracao de imagens integrado ao Gemini (originalmente Gemini 2.5 Flash Image). O nome veio de apelidos da Product Manager Naina Raisinghani do Google DeepMind. Na pratica:

- **Nano Banana** = Gemini 2.5 Flash Image (rapido, gratuito)
- **Nano Banana Pro** = Gemini 3 Pro Image (qualidade superior, pago)
- **Nano Banana 2** = Gemini 3.1 Flash Image (equilibrio velocidade/qualidade)

### Capacidades para Marketing Profissional

**Pontos Fortes:**
- Fotorrealismo excepcional — dificil distinguir de fotos reais
- Personalizacao de marca: pode guiar o modelo para gerar imagens com estilo, logo e caracteristicas do produto
- Texto renderizado com ate 95% de precisao (Imagen 4)
- Resolucao ate 2K para materiais impressos e digitais
- Edicao por linguagem natural (alterar elementos especificos via prompt)

**Limitacoes:**
- Imagen 3 tinha texto distorcido (70% precisao) — superado pelo Imagen 4
- Modelos gratuitos tem limites diarios
- Sem controle fino de composicao (nao substitui Photoshop para layouts precisos)

### Acesso: Interface Web vs API

| Canal | Ferramenta | Custo | Limite |
|-------|-----------|-------|--------|
| Web (gratuito) | Google AI Studio | Gratis | ~500 imagens/dia |
| Web (Pro) | Gemini app (AI Pro) | US$19.99/mes | 1000 NB + 100 NB Pro/dia |
| Web (Ultra) | Gemini app (AI Ultra) | US$249.99/mes | Acesso "Highest" |
| API (gratis) | Gemini Developer API | Gratis | ~500 req/dia (varia) |
| API (pago) | Vertex AI | Pay-per-use | Imagen 4 Fast: $0.02/img |

### Precos API (Vertex AI, 2026)

| Modelo | Preco/Imagem |
|--------|-------------|
| Imagen 4 Fast | US$0.02 |
| Imagen 4 Standard | US$0.04 |
| Imagen 4 Ultra | US$0.06 |
| Nano Banana (Flash Image) | ~US$0.045 (512px) a ~US$0.15 (4K) |
| Nano Banana Pro (3 Pro Image) | ~US$0.134 (1K) a ~US$0.24 (4K) |

---

## 2. Google Veo 3 / Veo 3.1

### Capacidades Atuais

Veo 3 e o modelo de geracao de video do Google DeepMind, disponivel via Gemini e Google Flow.

**Recursos principais:**
- **Texto para video** com audio sincronizado nativamente
- **Imagem para video** — upload de foto do produto e descricao do movimento desejado
- **Reference Image Control** (Veo 3.1) — ate 3 imagens de referencia para manter consistencia
- **Scene Extension** — gerar clipes conectados para videos de ate 1 minuto+
- **Frame Transition** — criar transicoes suaves entre duas imagens (inicio e fim)
- **Video vertical** — upload de imagem vertical gera video vertical (ideal para Reels/Stories)
- **Audio integrado** — descricao de audio no prompt gera som sincronizado

### Aplicacao para Product Shots

Para focos cirurgicos e mesas cirurgicas em PNG transparente:
1. Gerar background com Imagen 4 / Nano Banana (sala cirurgica, showroom, etc.)
2. Compor produto + background em editor (Canva, Photoshop)
3. Usar imagem composta como input no Veo 3 para gerar video com movimento sutil
4. Transicoes entre angulos diferentes do mesmo produto via Frame Transition

### Google Flow (Plataforma Unificada)

Em marco 2026, Google unificou Whisk + ImageFX + Flow em uma unica plataforma:
- **Whisk** (mood boards e colagens visuais) agora esta dentro do Flow
- **ImageFX** (texto para imagem) integrado ao Flow
- **Nano Banana** integrado nativamente — criar imagem e animar sem sair do Flow
- **Ferramenta Lasso** — selecionar areas da imagem e editar via linguagem natural

**Fluxo ideal no Flow:**
1. Criar imagem do produto em cenario (Nano Banana/Imagen)
2. Editar detalhes com lasso tool
3. Animar com Veo 3.1
4. Exportar em formato vertical (Stories/Reels)

### Acesso

- **Gemini AI Pro** (US$19.99/mes): acesso ao Veo 3
- **Gemini AI Ultra** (US$249.99/mes): acesso completo Veo 3.1
- **API Vertex AI**: preco por segundo de video gerado
- **Google Flow**: interface web gratuita (com limites) ou via assinatura

---

## 3. Tecnicas de Composicao com Product Shots

### O Problema

Voce tem ~340 PNGs com fundo transparente. Precisa coloca-los em cenarios profissionais (salas cirurgicas, ambientes hospitalares, showrooms) mantendo o produto REAL e o cenario gerado por IA.

### Abordagem 1: Background Generation (Recomendada para MVP)

**Ferramentas especializadas:**

| Ferramenta | Especialidade | Batch? | API? | Preco |
|-----------|---------------|--------|------|-------|
| **Photoroom** | E-commerce, mobile-first | Sim | Sim | Freemium |
| **Claid AI** | Catalogo profissional, 4K | Sim | Sim | Pago |
| **Mokker AI** | Background realista, sombras | Sim | Sim | Pago |
| **Canva AI** | Templates + brand kit | Sim | Limitada | US$13/mes |
| **CreatorKit** | Product photography | Sim | Sim | Pago |

**Como funciona:**
1. Upload do PNG com fundo transparente
2. Descricao do cenario desejado (texto) OU selecao de template
3. IA identifica contorno do produto automaticamente
4. Gera cenario com sombras, iluminacao e reflexos realistas
5. Composicao automatica produto + cenario

### Abordagem 2: Inpainting/Outpainting Manual

**Ferramentas:** Photoshop (Generative Fill), Leonardo AI Canvas, GIMP + plugins
1. Colocar produto no canvas na posicao desejada
2. Selecionar area ao redor do produto
3. Usar inpainting/outpainting para gerar cenario ao redor
4. Ajustar iluminacao e sombras manualmente

### Abordagem 3: Composicao Hibrida (Maior Qualidade)

1. **Gerar cenario completo** com Imagen 4 / Midjourney (sala cirurgica vazia)
2. **Sobrepor produto** (PNG transparente) em editor (Photoshop/Canva)
3. **Ajustar iluminacao** — usar IA para harmonizar luz do produto com cenario
4. **Adicionar sombras** — drop shadow realista baseado na luz do cenario
5. **Refinar** — inpainting nas bordas para integrar naturalmente

### Dicas para Equipamentos Medicos

- Usar cenarios limpos e profissionais (salas brancas, backgrounds neutros)
- Evitar cenarios clinicos com pacientes (questao regulatoria)
- Manter cores reais do produto — NUNCA alterar via IA
- Adicionar elementos contextuais sutis (instrumentos, iluminacao hospitalar)
- Garantir que especificacoes tecnicas visiveis no produto nao sejam alteradas

---

## 4. Workflows de Producao Visual com IA

### Pipeline Completo: Briefing -> Publicacao

```
FASE 1: PLANEJAMENTO
  |-- Calendario editorial (mensal)
  |-- Selecao de produtos para destaque
  |-- Definicao de formatos (post, carousel, reel, story)
  |-- Briefing por peca (produto + mensagem + CTA)

FASE 2: GERACAO DE ASSETS
  |-- [IA] Gerar backgrounds/cenarios (Imagen 4 / Nano Banana)
  |-- [IA] Compor produto + cenario (Photoroom / Claid / Canva)
  |-- [IA] Gerar textos/copy (Gemini / ChatGPT)
  |-- [IA] Gerar variacoes (A/B testing visual)

FASE 3: MONTAGEM
  |-- Aplicar em templates pre-aprovados (Canva Brand Kit)
  |-- Adicionar textos, CTAs, logos
  |-- Gerar formatos (1080x1080, 1080x1350, 1080x1920)
  |-- [IA] Animar para Reels/Stories (Veo 3 / Runway)

FASE 4: REVISAO HUMANA (OBRIGATORIA)
  |-- Verificar fidelidade do produto
  |-- Conferir especificacoes tecnicas
  |-- Validar compliance regulatorio
  |-- Aprovar textos e claims
  |-- Checklist de qualidade

FASE 5: PUBLICACAO
  |-- Agendar em ferramenta de social media
  |-- Publicar em multiplas plataformas
  |-- Monitorar engajamento
  |-- Iterar baseado em dados
```

### Metricas de Eficiencia com IA (Benchmarks 2025-2026)

- Reducao de 60-80% no tempo de producao
- Aumento de 3-5x no volume de conteudo
- 79% dos profissionais de social media usam IA diariamente
- 88% dos marketers dependem de ferramentas de IA todos os dias

### Principio Fundamental: Human-in-the-Loop

**Toda peca gerada por IA DEVE passar por revisao humana antes da publicacao.**
Isso e especialmente critico para marketing de dispositivos medicos.

---

## 5. Alternativas e Complementos

### Comparativo Geral para Marketing B2B Profissional

| Ferramenta | Forca Principal | Texto em Imagem | API | Preco Base | Ideal Para |
|-----------|----------------|-----------------|-----|-----------|-----------|
| **Imagen 4** | Fotorrealismo, velocidade | 95% | Sim (Vertex) | $0.02/img | Backgrounds, composicoes |
| **Nano Banana 2** | Velocidade + integracao Gemini | Bom | Sim (Gemini API) | Gratis (limites) | Prototipagem rapida |
| **Midjourney** | Estetica artistica, coerencia | Medio | Nao (Discord) | $10/mes | Branding, lifestyle |
| **DALL-E 3 / GPT Image** | Texto preciso, ChatGPT | Excelente | Sim (OpenAI) | $0.005-0.08/img | Textos em imagens, social |
| **Stable Diffusion** | Open-source, customizacao | Variavel | Local/API | Gratis (local) | Fine-tuning marca |
| **Leonardo AI** | Fine-tuning, Canvas Editor | Bom (Phoenix) | Sim | $12/mes | Product mockups |
| **Canva AI** | Templates + Brand Kit | N/A (texto separado) | Limitada | $13/mes | Producao em massa |
| **Adobe Firefly** | Comercialmente seguro, integrado | Bom | Sim | Incluso Creative Cloud | Composicao profissional |

### Para Geracao de Video

| Ferramenta | Forca | Imagem->Video | Duracao Max | Preco |
|-----------|-------|---------------|-------------|-------|
| **Veo 3.1** | Audio nativo, qualidade | Sim (ate 3 refs) | 60s+ | Gemini Pro |
| **Runway Gen-4.5** | Cinematico, controle camera | Sim | 10s | $12/mes |
| **Kling AI** | Motion Brush, fisica | Sim | 120s | Freemium |
| **Pika** | Rapido, acessivel, keyframes | Sim | 10s | $8/mes |
| **Luma Dream Machine** | Textura realista | Sim | 5s | Freemium |
| **Adobe Firefly Video** | Comercialmente seguro | Sim | Variavel | Creative Cloud |

### Recomendacao por Caso de Uso

| Caso de Uso | Ferramenta Primaria | Alternativa |
|------------|-------------------|-------------|
| Background para product shot | Imagen 4 + Photoroom | Canva AI + Claid |
| Post com texto integrado | DALL-E 3 / Nano Banana Pro | Canva AI |
| Carousel educativo | Canva AI + Brand Kit | Leonardo AI |
| Reel de produto (15-30s) | Veo 3.1 (Flow) | Runway Gen-4.5 |
| Story com animacao sutil | Kling AI | Pika |
| Mockup de produto em cenario | Leonardo AI | Imagen 4 + Photoshop |
| Producao em massa (batch) | Canva AI + Photoroom | Claid API |

---

## 6. Geracao de Videos a partir de Imagens Estaticas

### Tecnicas Principais

#### 6.1. Image-to-Video Direto
- Upload da imagem do produto composta (com background)
- Prompt descrevendo o movimento desejado
- IA gera video de 5-60 segundos
- **Ferramentas:** Veo 3.1, Runway, Kling AI

#### 6.2. Frame Transition (Duas Imagens)
- Imagem inicial (ex: produto desligado)
- Imagem final (ex: produto em uso/aceso)
- IA gera transicao cinematica entre as duas
- **Ferramenta ideal:** Veo 3.1

#### 6.3. Motion Brush (Animacao Seletiva)
- Upload da imagem
- Selecao manual da area a animar (ex: luzes do foco cirurgico)
- Definicao do tipo de movimento
- Restante da imagem permanece estatico
- **Ferramenta ideal:** Kling AI

#### 6.4. Camera Motion (Ken Burns Avancado)
- Aplicar movimento de camera sobre imagem estatica
- Zoom, pan, orbita, tilt
- Adiciona profundidade e dinamismo
- **Ferramentas:** Runway, Veo 3, qualquer editor de video

#### 6.5. Composicao Multi-Shot
- Gerar multiplos angulos/variacoes do produto
- Montar sequencia com transicoes
- Adicionar texto/overlay em editor
- **Pipeline:** Imagen/Nano Banana -> Canva/Premiere -> Publicacao

### Workflow para Reel de Produto (Recomendado)

```
1. Selecionar 3-5 imagens do produto (diferentes angulos)
2. Gerar backgrounds com Imagen 4 (cenario hospitalar clean)
3. Compor produto + background (Photoroom ou Canva)
4. Gerar transicoes entre imagens (Veo 3.1 Frame Transition)
5. Adicionar texto overlay com specs do produto
6. Adicionar musica/audio ambiente
7. Exportar em 1080x1920 (9:16) para Reels/Stories
8. REVISAO HUMANA antes de publicar
```

---

## 7. Templates de Design com IA

### Sistema de Templates com Identidade Visual

#### Principios
1. **Elementos fixos (locked):** Logo, paleta de cores, tipografia, safe zones
2. **Elementos variaveis (IA):** Background, cenario, iluminacao, composicao
3. **Regras de marca:** Definidas em Brand Kit (Canva) ou guia de estilo

#### Implementacao com Canva AI

**Canva Brand Kit (Pro/Teams):**
- Upload de logos, cores oficiais (hex), fontes aprovadas
- Templates pre-aprovados com areas editaveis
- Magic Design gera variacoes on-brand automaticamente
- Bulk Create: gerar dezenas de variacoes a partir de planilha

**Workflow:**
1. Criar 5-10 templates master por formato (post, carousel, story, reel)
2. Definir areas fixas (logo, barra de cor, tipografia)
3. Definir areas variaveis (imagem do produto, background, texto)
4. Usar Canva Sheets para gerar variacoes em massa
5. Uma planilha com: produto, texto, CTA -> dezenas de pecas prontas

#### Implementacao com Ferramentas Dedicadas

**Typeface:** Plataforma de IA que gera conteudo on-brand automaticamente
**Frontify:** Hub de marca com IA que valida compliance visual
**Lucidpress:** Templates com elementos locked + campos customizaveis

#### Fine-Tuning para Consistencia

**Leonardo AI** permite treinar modelos customizados:
1. Upload de 10-20 imagens de referencia (identidade visual existente)
2. Treinar modelo personalizado
3. Todas as geracoes futuras seguem o estilo da marca
4. Especialmente util para manter consistencia visual em campanhas longas

### Template System para Equipamentos Medicos

```
TEMPLATE: Post de Produto
├── Header: Logo + tagline (FIXO)
├── Imagem: Produto em cenario (VARIAVEL - IA gera cenario)
├── Badge: Certificacoes (FIXO - ANVISA, ISO, etc.)
├── Texto: Nome do produto + destaque (VARIAVEL)
├── CTA: Botao/link (SEMI-FIXO - texto varia)
└── Footer: Contato + redes sociais (FIXO)
```

---

## 8. Limitacoes e Cuidados — Dispositivos Medicos

### O que IA Generativa NAO DEVE fazer em marketing de dispositivos medicos

#### Proibicoes Absolutas

1. **NAO inventar especificacoes tecnicas** — Toda spec deve vir da documentacao oficial do fabricante
2. **NAO criar cenas clinicas falsas** — Imagens de pacientes, procedimentos cirurgicos ou cenarios clinicos com pessoas sao PROIBIDOS se gerados por IA
3. **NAO alterar a aparencia real do produto** — Cor, formato, tamanho, rotulos e marcacoes devem corresponder ao produto real
4. **NAO gerar claims de eficacia** — Textos sobre desempenho devem ser baseados em dados reais e aprovados
5. **NAO simular resultados clinicos** — Antes/depois, dados de pacientes, ou resultados de tratamento
6. **NAO criar imagens de uso em pacientes reais** — IA pode "alucinar" detalhes anatomicos incorretos

#### Cuidados Regulatorios

**ANVISA (Brasil):**
- Marketing de dispositivos medicos deve seguir RDC 96/2008 e normas especificas
- Informacoes tecnicas devem corresponder ao registro do produto
- Imagens promocionais nao devem induzir a erro sobre capacidades do produto

**FDA (EUA) — Referencia:**
- 65% dos profissionais de pharma NAO confiam em IA para compliance
- Principais preocupacoes: alucinacoes (40%), falta de rastreabilidade (20%), falta de transparencia (12.5%)
- Toda imagem gerada por IA deve ter revisao humana qualificada

#### Boas Praticas

| Pratica | Detalhes |
|---------|---------|
| **Produto sempre real** | Usar SEMPRE a foto real do produto (PNG original) |
| **Cenario pode ser IA** | Backgrounds neutros, showrooms, ambientes limpos |
| **Texto verificado** | Todo texto/claim verificado por equipe regulatoria |
| **Sem pessoas IA** | Nao gerar profissionais de saude ou pacientes com IA |
| **Watermark interno** | Documentar internamente quais imagens usaram IA |
| **Arquivo de prompts** | Manter registro dos prompts usados para cada peca |
| **Checklist pre-publicacao** | Validacao obrigatoria antes de qualquer publicacao |
| **Disclaimer quando necessario** | "Imagem ilustrativa do ambiente" quando aplicavel |

#### Checklist de Compliance para Cada Peca

```
[ ] Produto na imagem e a foto REAL (nao gerada por IA)?
[ ] Especificacoes tecnicas conferem com documentacao oficial?
[ ] Cenario nao sugere procedimento clinico com paciente?
[ ] Nao ha pessoas geradas por IA na imagem?
[ ] Claims de marketing aprovados pela equipe regulatoria?
[ ] Cores e aparencia do produto correspondem ao real?
[ ] Certificacoes exibidas sao validas e atuais?
[ ] Imagem nao induz a interpretacao errada sobre o produto?
```

---

## 9. MVP sem API — Estrategia de Prototipagem Rapida

### Ferramentas Web para Comecar Imediatamente

#### Stack Recomendado para MVP (Custo Minimo)

| Ferramenta | Funcao | Custo | Capacidade |
|-----------|--------|-------|-----------|
| **Google AI Studio** (gratis) | Gerar backgrounds/cenarios | Gratis | ~500 imgs/dia |
| **Gemini AI Pro** | Nano Banana + Veo 3 | US$19.99/mes | 1000 imgs + videos |
| **Canva Pro** | Templates + composicao + brand kit | US$13/mes | Ilimitado |
| **Photoroom** (gratis) | Composicao produto + background | Gratis (limites) | ~10/dia free |
| **Google Flow** | Video a partir de imagens | Incluso Gemini | Com limites |

**Custo MVP Total: ~US$33/mes** (Gemini Pro + Canva Pro)

#### Workflow MVP (100% Interface Web)

```
PASSO 1: Gerar Cenarios (Google AI Studio / Gemini)
  Prompt: "Professional medical showroom, white clean background,
           soft LED lighting, modern hospital environment,
           no people, empty room, photorealistic, 4K"
  -> Gerar 10-20 variacoes de cenario

PASSO 2: Compor Produto + Cenario (Canva / Photoroom)
  - Upload PNG do produto (fundo transparente)
  - Upload cenario gerado
  - Posicionar produto no cenario
  - Ajustar sombras e proporcoes

PASSO 3: Aplicar Template (Canva)
  - Usar Brand Kit com cores e fontes da empresa
  - Aplicar template pre-definido
  - Adicionar texto, CTA, logo, certificacoes
  - Exportar em multiplos formatos

PASSO 4: Criar Video (Google Flow / Veo 3)
  - Upload da composicao final
  - Prompt de animacao sutil
  - Exportar em formato vertical

PASSO 5: Revisao e Publicacao
  - Checklist de compliance
  - Aprovacao humana
  - Agendar publicacao
```

#### Capacidade de Producao MVP (Estimativa)

Com uma pessoa dedicada, usando stack acima:
- **Posts estaticos:** 15-25/dia (incluindo revisao)
- **Carousels:** 5-8/dia
- **Stories/Reels simples:** 3-5/dia
- **Total semanal:** 100-150 pecas

#### Google AI Pro — O que voce ganha por US$19.99/mes

- Ate 100 prompts/dia com modelos Thinking e Pro
- 1000 imagens/dia com Nano Banana
- 100 imagens/dia com Nano Banana Pro
- Acesso ao Veo 3 para geracao de video
- 20 relatorios Deep Research por dia
- 1 milhao de tokens de contexto
- Acesso ao Google Flow para edicao integrada

---

## 10. Escalabilidade via API

### Quando Migrar de Interface Web para API

#### Sinais de que Precisa de API

| Sinal | Detalhes |
|-------|---------|
| Volume > 50 pecas/dia | Interface web se torna gargalo |
| Repeticao manual excessiva | Mesmos passos para cada produto |
| Necessidade de variacao sistematica | Mesmo produto, 10 cenarios diferentes |
| Integracao com sistemas internos | ERP, PIM, DAM |
| Equipe nao-tecnica precisa produzir | Self-service via formularios |
| Consistencia critica | Padronizacao automatizada |

#### Arquitetura API Recomendada

```
ENTRADA (Dados do Produto)
  |-- Nome do produto
  |-- Imagem PNG (fundo transparente)
  |-- Categoria (foco, mesa, serra, suporte)
  |-- Especificacoes tecnicas
  |-- Formato desejado (post, carousel, reel, story)
       |
       v
PROCESSAMENTO (Pipeline Automatizado)
  |-- [API] Imagen 4 Fast -> Gerar 3-5 backgrounds ($0.02/img)
  |-- [API] Photoroom/Claid -> Compor produto + background
  |-- [API] Gemini -> Gerar copy/texto para a peca
  |-- [API] Canva -> Aplicar template + brand kit
  |-- [API] Veo 3 -> Gerar video se formato = reel/story
       |
       v
SAIDA (Assets Prontos)
  |-- Imagens em multiplos formatos
  |-- Videos em 9:16 e 1:1
  |-- Textos/captions
  |-- Queue para revisao humana
       |
       v
REVISAO HUMANA (Dashboard)
  |-- Aprovar / Rejeitar / Editar
  |-- Compliance check
  |-- Agendar publicacao
```

#### Custos Estimados em Escala

**Cenario: 340 produtos x 5 variacoes = 1.700 imagens/mes**

| Componente | Custo Unitario | Quantidade | Custo Mensal |
|-----------|---------------|-----------|-------------|
| Imagen 4 Fast (backgrounds) | $0.02 | 1.700 | US$34 |
| Composicao (Photoroom API) | ~$0.05 | 1.700 | US$85 |
| Copy (Gemini API) | ~$0.01 | 1.700 | US$17 |
| Videos (Veo 3 API) | ~$0.10/s x 10s | 500 | US$500 |
| **TOTAL Estimado** | | | **~US$636/mes** |

**Comparacao com producao tradicional:**
- Fotografo + estudio + pos-producao: R$5.000-15.000/mes para volume equivalente
- Agencia de marketing: R$8.000-25.000/mes
- **Pipeline IA: ~R$3.500/mes** (taxa de cambio ~5.5)

#### APIs Disponiveis (Marco 2026)

| Servico | API | Documentacao |
|---------|-----|-------------|
| Google Imagen 4 | Vertex AI | cloud.google.com/vertex-ai |
| Google Veo 3 | Vertex AI | cloud.google.com/vertex-ai |
| Gemini (texto + imagem) | Gemini Developer API | ai.google.dev |
| Nano Banana | Gemini Developer API | ai.google.dev |
| OpenAI DALL-E / GPT Image | OpenAI API | platform.openai.com |
| Leonardo AI | Leonardo API | docs.leonardo.ai |
| Runway | Runway API | docs.runwayml.com |
| Photoroom | Photoroom API | photoroom.com/api |
| Claid | Claid API | claid.ai/api |
| Canva | Canva Connect API | canva.dev |

#### Resiliencia do Pipeline

Praticas recomendadas para producao em massa:
- **Exponential backoff** para erros de rate limit
- **Circuit breaker** com fallback para provider secundario
- **Logging estruturado** de todas as chamadas API
- **Cache** de backgrounds gerados para reutilizacao
- **Queue system** (ex: Bull, RabbitMQ) para processar em lotes
- **Monitoramento** de custos e qualidade

---

## 11. Recomendacoes Praticas

### Fase 1: MVP Imediato (Semanas 1-4)

**Objetivo:** Validar conceito, criar primeiras 50-100 pecas, estabelecer workflow.

**Stack:**
- Google Gemini AI Pro (US$19.99/mes)
- Canva Pro (US$13/mes)
- Photoroom Free

**Acoes:**
1. Configurar Brand Kit no Canva (logo, cores, fontes)
2. Criar 5 templates master (post, carousel, story, reel cover, banner)
3. Selecionar 20 produtos prioritarios
4. Gerar cenarios com Nano Banana / Google AI Studio
5. Compor 100 pecas piloto
6. Testar publicacao e medir engajamento
7. Documentar workflow e tempos

**Custo: ~US$33/mes (~R$180/mes)**

### Fase 2: Producao Regular (Meses 2-3)

**Objetivo:** Escalar para toda a linha de produtos, estabelecer cadencia de publicacao.

**Stack adicional:**
- Photoroom Pro ou Claid (para batch processing)
- Google Flow (para videos)

**Acoes:**
1. Processar todos os 340 produtos em batch
2. Gerar 3-5 variacoes por produto
3. Criar biblioteca de cenarios reutilizaveis
4. Estabelecer calendario editorial semanal
5. Treinar equipe no workflow
6. Implementar checklist de compliance

**Custo: ~US$80-120/mes (~R$500-650/mes)**

### Fase 3: Automacao via API (Meses 4-6)

**Objetivo:** Pipeline automatizado, self-service para equipe comercial.

**Stack:**
- Vertex AI (Imagen 4 + Veo 3 API)
- Gemini Developer API
- Photoroom/Claid API
- Dashboard customizado (Next.js ou similar)

**Acoes:**
1. Desenvolver pipeline automatizado
2. Interface web interna para solicitar pecas
3. Sistema de aprovacao com workflow
4. Integracao com calendario de publicacao
5. Metricas de producao e custo por peca
6. A/B testing automatizado

**Custo: US$500-800/mes infra + desenvolvimento inicial**

### Resumo de Decisao

| Criterio | Recomendacao |
|---------|-------------|
| **Melhor para backgrounds** | Imagen 4 (via Gemini/Vertex AI) |
| **Melhor para composicao rapida** | Photoroom + Canva |
| **Melhor para videos** | Veo 3.1 (via Google Flow) |
| **Melhor custo-beneficio MVP** | Gemini Pro + Canva Pro |
| **Melhor para producao em massa** | Pipeline API (Vertex AI + Photoroom API) |
| **Melhor para brand consistency** | Canva Brand Kit + Templates locked |
| **Melhor para texto em imagem** | DALL-E 3 / Imagen 4 |
| **NUNCA usar** | IA para gerar specs, pacientes, cenas clinicas |

---

## Sources

- [Google Imagen 3 — Vertex AI Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/3-0-generate)
- [Imagen 4 vs Imagen 3 Comparison](https://medium.com/@luxurymen2t/imagen-4-vs-imagen-3-which-ai-image-generator-should-you-use-in-2025-b8108eb03e4d)
- [5 Key Differences Between Google Imagen 3 and Imagen 4](https://timeboostermarketing.com/differences-google-imagen-3-and-imagen-4/)
- [Imagen 4 Family Generally Available in Gemini API](https://developers.googleblog.com/announcing-imagen-4-fast-and-imagen-4-family-generally-available-in-the-gemini-api/)
- [What Is Imagen 4 Ultra — MindStudio](https://www.mindstudio.ai/blog/what-is-imagen-4-ultra-google)
- [Nano Banana 2 — Google Blog](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/)
- [Nano Banana Pro — Google DeepMind](https://blog.google/technology/ai/nano-banana-pro/)
- [Nano Banana 2 Explained](https://www.eesel.ai/blog/nano-banana-2)
- [Veo 3 — Google DeepMind](https://deepmind.google/models/veo/)
- [Veo 3.1 and New Creative Capabilities](https://developers.googleblog.com/introducing-veo-3-1-and-new-creative-capabilities-in-the-gemini-api/)
- [Google Adds Image-to-Video to Veo 3 — TechCrunch](https://techcrunch.com/2025/07/10/google-adds-image-to-video-generation-capability-to-veo-3/)
- [Veo 3 Fast on Vertex AI](https://cloud.google.com/blog/products/ai-machine-learning/veo-3-fast-available-for-everyone-on-vertex-ai)
- [Google Flow March 2026 Redesign](https://bonega.ai/en/blog/google-flow-march-2026-unified-ai-video-workspace)
- [Google Flow Updates February 2026](https://blog.google/innovation-and-ai/models-and-research/google-labs/flow-updates-february-2026/)
- [Gemini AI Video Generation](https://gemini.google/overview/video-generation/)
- [Google AI Pro & Ultra Features — 9to5Google](https://9to5google.com/2026/02/21/google-ai-pro-ultra-features/)
- [Gemini Developer API Pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Vertex AI Pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing)
- [AI Image Pricing 2026: Google vs OpenAI](https://intuitionlabs.com/articles/ai-image-generation-pricing-google-openai)
- [Gemini Image Generation Free Tier Guide 2026](https://www.aifreeapi.com/en/posts/gemini-image-generation-free-api)
- [AI Video Tools Comparison 2025 — Sora vs Runway vs Pika](https://www.aivideodetector.org/blog/ai-video-generation-tools-comparison-2025)
- [Top 5 AI Video Generators 2026](https://bestphoto.ai/blog/top-5-ai-video-generators-2026)
- [Ultimate AI Video Generation Models Guide 2025](https://ulazai.com/ai-video-models-guide-2025/)
- [Midjourney vs DALL-E 3 vs Stable Diffusion 2025](https://vertu.com/lifestyle/midjourney-vs-dall-e-3-vs-stable-diffusion-2025-ai-image-generation/)
- [Best AI Image Generation Tools 2025 — Brand Vision](https://www.brandvm.com/post/best-image-generation-ai-tools-2025)
- [Leonardo AI Review 2026](https://techtip.blog/leonardo-ai-review-2026/)
- [Leonardo AI Product Mockups — AI Flow Review](https://aiflowreview.com/leonardo-ai-product-mockups/)
- [Canva Magic Design](https://www.canva.com/magic-design/)
- [Canva Brand Kit](https://www.canva.com/pro/brand-kit/)
- [AI Brand Management — Typeface](https://www.typeface.ai/blog/ai-brand-management-how-to-maintain-brand-consistency-with-ai-image-generators)
- [AI Tools for Brand Management 2025 — Frontify](https://www.frontify.com/en/guide/ai-tools-for-brand-management)
- [Claid AI — Product Photography](https://claid.ai/)
- [Photoroom — AI Product Photography](https://www.photoroom.com/)
- [Mokker AI — Background Replacement](https://mokker.ai/)
- [AI Product Photography Tools 2026 — Claid Blog](https://claid.ai/blog/article/ai-product-photo-tools)
- [AI-Driven Social Media Workflow 2025 — Mixpost](https://mixpost.app/blog/how-ai-is-redefining-social-media-workflow-in-2025)
- [2026 State of Content Workflows — Averi](https://www.averi.ai/guides/2026-state-content-workflows)
- [FDA AI Medical Device Regulation 2025](https://www.complizen.ai/post/fda-ai-medical-device-regulation-2025)
- [AI Image Generation API Comparison 2026](https://blog.laozhang.ai/en/posts/ai-image-generation-api-comparison-2026)
- [Imagen 4 Pricing and API Access 2026](https://magichour.ai/blog/imagen-4-pricing-and-api-access)
