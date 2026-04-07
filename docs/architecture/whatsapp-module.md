# Arquitetura — Modulo WhatsApp Business

**Story:** 15.1 — Epic 15 (Novos Canais + CRM)
**Autor:** @architect (Aria)
**Data:** 2026-04-07
**Status:** Arquitetura definida — implementacao pendente (15.2)

---

## 1. Overview

O WhatsApp foi validado pela IC como **canal #1** para conversao B2B healthcare (Score 95/100). O sistema atual dedica apenas 2% do esforco ao canal, enquanto deveria ser o canal primario de nurturing. Este modulo integra WhatsApp Business API ao Content Studio para nurturing direto, catalogo de produtos e sequencias automatizadas por fase da jornada de compra.

### Por que WhatsApp para B2B healthcare

- **Penetracao:** 99% dos profissionais de saude brasileiros usam WhatsApp diariamente
- **Contexto:** Decisoes de compra de dispositivos medicos envolvem 4+ stakeholders — WhatsApp conecta todos
- **Ciclo longo:** Jornada de compra de 3-18 meses exige nurturing persistente, nao apenas posts em feed
- **Urgencia:** Engenheiros clinicos respondem WhatsApp em minutos vs. e-mail em dias
- **Confianca:** Canal percebido como direto e pessoal — ideal para B2B de alto valor

### Principios

- **Nurturing > Broadcasting** — sequencias personalizadas por persona e fase, nao spam
- **Conteudo tecnico** — engenheiro clinico recebe specs, compras recebe TCO
- **Compliance** — CONAR (sem citar concorrentes), LGPD (opt-in obrigatorio), Meta policies
- **Rastreabilidade** — toda mensagem gera UTM para tracking no CRM

### Posicionamento no Content Studio

O modulo WhatsApp nao e um sistema standalone. Ele e um **canal de distribuicao** que recebe conteudo atomizado do pipeline existente (SemanticAtomizer) e o formata para entrega via WhatsApp Business API.

```
Pipeline de Conteudo
       |
  SemanticAtomizer
       |
  +----+----+
  |    |    |
Feed  Blog  WhatsApp  <-- ESTE MODULO
              |
        Meta Business API
              |
        Contatos segmentados
```

---

## 2. Fluxos de Nurturing por Jornada

### 2.1 Mapa da Jornada B2B Healthcare

A jornada de compra de dispositivos medicos possui 7 fases distintas. Cada fase tem objetivos de comunicacao diferentes.

| # | Fase | Duracao Tipica | Objetivo da Comunicacao |
|---|------|---------------|------------------------|
| 1 | Identificacao | 1-4 semanas | Conscientizar sobre o problema/necessidade |
| 2 | Planejamento | 2-6 semanas | Apresentar solucoes possiveis |
| 3 | Especificacao | 2-8 semanas | Fornecer dados tecnicos detalhados |
| 4 | Cotacao | 1-3 semanas | Facilitar comparacao e proposta |
| 5 | Avaliacao | 2-6 semanas | Resolver objecoes, fornecer evidencias |
| 6 | Decisao | 1-2 semanas | Criar urgencia, confirmar escolha |
| 7 | Pos-compra | Ongoing | Fidelizar, gerar indicacoes, upsell |

### 2.2 Personas (4 decisores)

| ID | Persona | Papel na Decisao | Conteudo Preferido |
|----|---------|------------------|--------------------|
| `eng_clinica` | Engenheiro Clinico | Especificador tecnico | Datasheets, normas, comparativos tecnicos |
| `compras` | Setor de Compras | Decisor financeiro | ROI, TCO, condicoes comerciais |
| `equipe_medica` | Corpo Medico | Influenciador clinico | Casos clinicos, ergonomia, workflow |
| `admin` | Diretoria/Administracao | Aprovador final | Business case, compliance, referencias |

### 2.3 Matriz 28 Fluxos (7 fases x 4 personas)

Cada celula representa uma sequencia de nurturing com 3-7 mensagens espacadas ao longo da fase.

| Fase | Persona: Eng. Clinica | Compras | Equipe Medica | Admin |
|------|----------------------|---------|---------------|-------|
| 1. Identificacao | Specs comparativas | Custo total propriedade | Cases clinicos impacto | Dados mercado modernizacao |
| 2. Planejamento | Fichas tecnicas PDF | TCO inicial, financiamento | Videos demo workflow | Overview portfolio |
| 3. Especificacao | Claims detalhados, demos | Condicoes garantia | Agendamento demonstracao | Certificacoes ISO/ANVISA |
| 4. Cotacao | Docs licitacao | Proposta, margem 20% | Parecer pos-demo | ROI projetado |
| 5. Avaliacao | Comparativo "vs mercado" | Cases + social proof | Depoimentos medicos | Cases ROI |
| 6. Decisao | Suporte tecnico | Documentacao pregao | Parecer clinico | Analise TCO final |
| 7. Pos-compra | Tutoriais, manutencao | Fidelidade, recompra | Guia operacao | NPS, case sucesso |

#### Fase 1 — Identificacao (detalhada)

| Persona | Sequencia | Msgs | Gatilho |
|---------|-----------|------|---------|
| eng_clinica | `SEQ-ALL-ENG-F1` | 4 | Lead capturado via formulario tecnico |
| compras | `SEQ-ALL-COMP-F1` | 3 | Lead capturado via solicitacao de orcamento |
| equipe_medica | `SEQ-ALL-MED-F1` | 4 | Lead capturado via conteudo clinico |
| admin | `SEQ-ALL-ADM-F1` | 3 | Lead capturado via evento/indicacao |

**Conteudo tipico fase 1:**
- eng_clinica: "Voce sabia que 73% dos centros cirurgicos operam com iluminacao abaixo da norma?" + link artigo
- compras: Infografico de custo total de propriedade vs. manutencao corretiva
- equipe_medica: Case clinico anonimizado sobre impacto da iluminacao na ergonomia
- admin: Dado de mercado sobre modernizacao hospitalar no Brasil

#### Fase 2 — Planejamento (detalhada)

| Persona | Sequencia | Msgs | Gatilho |
|---------|-----------|------|---------|
| eng_clinica | `SEQ-{prod}-ENG-F2` | 5 | Abriu conteudo tecnico ou respondeu msg fase 1 |
| compras | `SEQ-{prod}-COMP-F2` | 4 | Solicitou informacao de preco |
| equipe_medica | `SEQ-{prod}-MED-F2` | 4 | Engajou com caso clinico |
| admin | `SEQ-{prod}-ADM-F2` | 3 | Solicitou apresentacao institucional |

**Exemplo: Sequencia Fase 2 — Eng. Clinica + LEV**

```
Dia 0: "Ola {nome}, vi que esta especificando focos cirurgicos. Preparei a ficha tecnica do LEV 4."
       -> Anexo: PDF ficha tecnica LEV
Dia 2: "Sabe por que Ra=99 faz diferenca na distincao de tecidos? Assista em 2 min."
       -> Link: YouTube Short — Ra=99 explicado
Dia 5: "Comparativo tecnico: nosso foco vs media de mercado em 5 specs que importam."
       -> Anexo: PDF comparativo (sem citar concorrentes)
Dia 7: "Quer agendar uma demonstracao tecnica presencial? Nosso consultor pode ir ate o hospital."
       -> CTA: Responda SIM
```

#### Fase 3 — Especificacao

| Persona | Sequencia | Msgs | Gatilho |
|---------|-----------|------|---------|
| eng_clinica | `SEQ-{prod}-ENG-F3` | 7 | Solicitou datasheet ou especificacao |
| compras | `SEQ-{prod}-COMP-F3` | 4 | Pediu proposta formal |
| equipe_medica | `SEQ-{prod}-MED-F3` | 5 | Pediu demo ou avaliacao |
| admin | `SEQ-{prod}-ADM-F3` | 3 | Solicitou referencias de clientes |

#### Fase 4 — Cotacao

| Persona | Sequencia | Msgs | Gatilho |
|---------|-----------|------|---------|
| eng_clinica | `SEQ-{prod}-ENG-F4` | 3 | Especificacao concluida |
| compras | `SEQ-{prod}-COMP-F4` | 5 | Proposta enviada |
| equipe_medica | `SEQ-{prod}-MED-F4` | 2 | Demo realizada |
| admin | `SEQ-{prod}-ADM-F4` | 3 | Proposta em avaliacao |

#### Fase 5 — Avaliacao

| Persona | Sequencia | Msgs | Gatilho |
|---------|-----------|------|---------|
| eng_clinica | `SEQ-{prod}-ENG-F5` | 5 | Proposta em analise interna |
| compras | `SEQ-{prod}-COMP-F5` | 5 | Comparando fornecedores |
| equipe_medica | `SEQ-{prod}-MED-F5` | 4 | Avaliando experiencia de uso |
| admin | `SEQ-{prod}-ADM-F5` | 4 | Avaliando business case |

**Conteudo tipico fase 5:**
- eng_clinica: Respostas tecnicas personalizadas, teste em campo se aplicavel
- compras: Contrapropostas, flexibilidade de pagamento, SLA de assistencia
- equipe_medica: Depoimentos de medicos em hospitais similares
- admin: ROI projetado com dados reais do hospital

#### Fase 6 — Decisao

| Persona | Sequencia | Msgs | Gatilho |
|---------|-----------|------|---------|
| eng_clinica | `SEQ-{prod}-ENG-F6` | 3 | Aprovacao tecnica emitida |
| compras | `SEQ-{prod}-COMP-F6` | 4 | Negociacao final |
| equipe_medica | `SEQ-{prod}-MED-F6` | 2 | Parecer clinico positivo |
| admin | `SEQ-{prod}-ADM-F6` | 3 | Decisao de investimento pendente |

#### Fase 7 — Pos-compra

| Persona | Sequencia | Msgs | Gatilho |
|---------|-----------|------|---------|
| eng_clinica | `SEQ-{prod}-ENG-F7` | 5 | Equipamento entregue/instalado |
| compras | `SEQ-{prod}-COMP-F7` | 3 | Faturamento concluido |
| equipe_medica | `SEQ-{prod}-MED-F7` | 4 | Equipamento em uso clinico |
| admin | `SEQ-{prod}-ADM-F7` | 3 | Projeto concluido |

**Conteudo tipico fase 7:**
- eng_clinica: Guias de manutencao preventiva, atualizacoes de firmware, treinamento avancado
- compras: Programas de fidelidade, condicoes especiais para proximas compras
- equipe_medica: Dicas de uso otimizado, novos acessorios, feedback collection
- admin: Relatorio de impacto pos-implantacao, convite para case de sucesso

---

## 3. Templates HSM (Header-Structured Messages)

Templates precisam de aprovacao previa da Meta. Categorias:

### 3.1 Categorias Meta

| Categoria | Uso | Custo | Aprovacao |
|-----------|-----|-------|-----------|
| **Utilidade** | Atualizacoes de pedido, confirmacoes, alertas | ~R$ 0.15 | Rapida (horas) |
| **Marketing** | Promocoes, conteudo, nurturing | ~R$ 0.30 | Moderada (1-3 dias) |
| **Autenticacao** | OTP, verificacao de identidade | ~R$ 0.10 | Rapida (horas) |

### 3.2 Estrutura de um Template HSM

```
+---------------------------+
| HEADER                    |  <-- Texto, imagem, video ou documento
|---------------------------|
| BODY                      |  <-- Texto principal (max 1024 chars)
| Suporta variaveis {{1}}   |
|---------------------------|
| FOOTER                    |  <-- Texto secundario (max 60 chars)
|---------------------------|
| [Botao 1] [Botao 2]      |  <-- Ate 3 botoes (URL, telefone, resposta rapida)
+---------------------------+
```

### 3.3 Templates Utilidade (utility)

| Template ID | Nome | Produto | Uso |
|-------------|------|---------|-----|
| UTL-001 | confirmacao_demo | Todos | Confirmacao de agendamento de demo |
| UTL-002 | envio_ficha_tecnica | Todos | Envio de ficha tecnica solicitada |
| UTL-003 | status_proposta | Todos | Atualizacao de status de proposta/licitacao |
| UTL-004 | pos_venda_checklist | LEV, KRATUS | Checklist pos-instalacao |
| UTL-005 | manutencao_preventiva | LEV | Lembrete de manutencao preventiva agendada |
| UTL-006 | cotacao_atualizada | Todos | Notificacao de proposta atualizada |

### 3.4 Templates Marketing (marketing)

| Template ID | Nome | Produto | Uso |
|-------------|------|---------|-----|
| MKT-001 | nurturing_specs | LEV | Sequencia specs (Fase 2-3) |
| MKT-002 | nurturing_tco | KRATUS | Sequencia TCO/ROI (Fase 4-6) |
| MKT-003 | nurturing_portfolio | Todos | Portfolio completo CC |
| MKT-004 | evento_hospitalar | Todos | Convite para feira/evento |
| MKT-005 | caso_sucesso | Todos | Case de cliente |
| MKT-006 | newsletter_semanal | Todos | Compilado semanal de conteudo |
| MKT-007 | nurturing_seguranca | OSTUS | Sequencia seguranca paciente |
| MKT-008 | nurturing_integracao | KRONUS | Sequencia integracao centro cirurgico |

### 3.5 Templates Autenticacao (authentication)

| Template ID | Nome | Uso |
|-------------|------|-----|
| AUTH-001 | opt_in_confirmacao | Confirmacao de opt-in LGPD |

### 3.6 Exemplos Concretos por Produto

#### LEV (Foco Cirurgico LED)

```yaml
template:
  id: "MKT-001"
  name: "nurturing_specs_lev"
  category: "marketing"
  language: "pt_BR"
  header:
    type: "document"
    example: "ficha-tecnica-lev.pdf"
  body: |
    Ola {{1}}, tudo bem?

    Preparamos a ficha tecnica completa do foco cirurgico LEV com todas as especificacoes:
    - Ra = 99 (fidelidade de cor maxima)
    - Profundidade de 1.930mm
    - 5 articulacoes independentes
    - Recarga em 2-4,5h

    {{2}}
  footer: "Salk Medical — Equipamento Medico Nacional"
  buttons:
    - type: "quick_reply"
      text: "Quero agendar demo"
    - type: "quick_reply"
      text: "Enviar para colega"
    - type: "url"
      text: "Ver no site"
      url: "https://salkmedical.com.br/lev?utm_source=whatsapp&utm_medium=social&utm_campaign={{3}}"
```

**Nota LEV:** Luz sempre CONCENTRADA no campo. Nunca pedir glow, dispersao ou raios laterais — contradiz o produto.

#### KRATUS (Mesa Cirurgica)

```yaml
template:
  id: "MKT-002"
  name: "nurturing_tco_kratus"
  category: "marketing"
  language: "pt_BR"
  header:
    type: "document"
    example: "tco-kratus-analise.pdf"
  body: |
    {{1}}, sua equipe cirurgica trabalha com a mesa certa para cada procedimento?

    O KRATUS oferece:
    - Posicionamento multiarticulado para todas especialidades
    - TCO 40% menor que solucoes importadas
    - Margem de preferencia 20% em licitacoes

    Calculamos o ROI especifico para o perfil do {{2}}.

    {{3}}
  footer: "Salk Medical — Equipamento Medico Nacional"
  buttons:
    - type: "quick_reply"
      text: "Ver proposta completa"
    - type: "quick_reply"
      text: "Agendar visita tecnica"
```

#### OSTUS (Cama Hospitalar)

```yaml
template:
  id: "MKT-007"
  name: "nurturing_seguranca_ostus"
  category: "marketing"
  language: "pt_BR"
  header:
    type: "image"
    example: "ostus-seguranca-paciente.jpg"
  body: |
    {{1}}, quedas de leito representam um dos eventos adversos mais frequentes.

    O OSTUS foi projetado para prevencao ativa:
    - Grades laterais com trava de seguranca
    - Freio centralizado em todas as rodas
    - Posicao Trendelenburg para emergencias

    Veja como a UTI do Hospital {{2}} otimizou o workflow de enfermagem.
  footer: "Salk Medical — Equipamento Medico Nacional"
  buttons:
    - type: "quick_reply"
      text: "Ver caso completo"
    - type: "url"
      text: "Catalogo OSTUS"
      url: "https://salkmedical.com.br/ostus?utm_source=whatsapp&utm_medium=social&utm_campaign={{3}}"
```

#### KRONUS (Pendente Cirurgico)

```yaml
template:
  id: "MKT-008"
  name: "nurturing_integracao_kronus"
  category: "marketing"
  language: "pt_BR"
  header:
    type: "image"
    example: "kronus-centro-cirurgico.jpg"
  body: |
    {{1}}, seu pendente cirurgico integra gases, eletrica e dados em um unico ponto?

    O KRONUS centraliza toda a infraestrutura do centro cirurgico:
    - Gases medicinais (O2, N2O, ar comprimido, vacuo)
    - Tomadas eletricas e de rede
    - Bracos articulados para monitores

    Configuracao customizada para {{2}} salas.
  footer: "Salk Medical — Equipamento Medico Nacional"
  buttons:
    - type: "quick_reply"
      text: "Solicitar projeto"
    - type: "quick_reply"
      text: "Falar com engenheiro"
```

### 3.7 Templates Institucionais (cross-product)

| Template ID | Categoria | Uso |
|-------------|-----------|-----|
| `inst_boas_vindas` | marketing | Primeiro contato com lead qualificado |
| `inst_agendamento_demo` | utilidade | Confirmacao de demonstracao agendada |
| `inst_pos_evento` | marketing | Follow-up apos eventos (FEMIPA, HOSPITALAR) |
| `inst_pesquisa_satisfacao` | utilidade | NPS pos-venda (30/90/180 dias) |
| `inst_aniversario_compra` | marketing | Aniversario da compra — oportunidade de upsell |

---

## 4. API Endpoints

### 4.1 Envio de Mensagens

| Metodo | Endpoint | Descricao |
|--------|----------|-----------|
| POST | `/api/whatsapp/send` | Enviar mensagem individual (template ou session) |
| POST | `/api/whatsapp/broadcast` | Broadcast segmentado para lista de contatos |
| POST | `/api/whatsapp/sequence/start` | Iniciar sequencia de nurturing para contato |
| PUT | `/api/whatsapp/sequence/{id}/pause` | Pausar sequencia ativa |
| PUT | `/api/whatsapp/sequence/{id}/resume` | Retomar sequencia pausada |
| DELETE | `/api/whatsapp/sequence/{id}` | Cancelar sequencia |

#### POST `/api/whatsapp/send` — Request

```json
{
  "contact_id": "uuid",
  "template_id": "MKT-001",
  "parameters": {
    "header": { "document_url": "https://cdn.salkmedical.com.br/datasheets/lev-v4.pdf" },
    "body": ["Dr. Silva", "LEV-500"]
  },
  "schedule_at": "2026-04-08T10:00:00-03:00"
}
```

#### POST `/api/whatsapp/send` — Response

```json
{
  "message_id": "uuid",
  "meta_message_id": "wamid.HBgNNTU...",
  "status": "sent",
  "timestamp": "2026-04-07T14:30:00Z"
}
```

### 4.2 Webhooks (recebimento)

| Metodo | Endpoint | Descricao |
|--------|----------|-----------|
| POST | `/api/whatsapp/webhook` | Callback da Meta (mensagens, status, leitura) |
| GET | `/api/whatsapp/webhook` | Verificacao de webhook (challenge) |

#### Eventos recebidos via webhook

| Evento | Campo `statuses[].status` | Acao |
|--------|--------------------------|------|
| `sent` | Mensagem enviada ao servidor Meta | Atualizar status |
| `delivered` | Entregue ao dispositivo | Atualizar status |
| `read` | Lida pelo destinatario | Atualizar status + abrir janela 24h |
| `failed` | Falha no envio | Logar erro, retry se aplicavel |
| `message` | Resposta do contato | Processar resposta, notificar equipe |

#### Webhook payload (status update)

```json
{
  "object": "whatsapp_business_account",
  "entry": [{
    "id": "BUSINESS_ACCOUNT_ID",
    "changes": [{
      "value": {
        "messaging_product": "whatsapp",
        "metadata": { "phone_number_id": "PHONE_ID" },
        "statuses": [{
          "id": "wamid.HBgNNTU...",
          "status": "read",
          "timestamp": "1712505600",
          "recipient_id": "5541999999999"
        }]
      }
    }]
  }]
}
```

### 4.3 Status e Metricas

| Metodo | Endpoint | Descricao |
|--------|----------|-----------|
| GET | `/api/whatsapp/messages/{id}/status` | Status de mensagem individual |
| GET | `/api/whatsapp/metrics/sequence/{id}` | Metricas de sequencia |
| GET | `/api/whatsapp/metrics/template/{id}` | Metricas de template |
| GET | `/api/whatsapp/metrics/overview` | Dashboard geral |
| GET | `/api/whatsapp/metrics/personas` | Metricas agrupadas por persona |
| GET | `/api/whatsapp/metrics/journey-phases` | Metricas agrupadas por fase da jornada |
| GET | `/api/whatsapp/metrics/products/{slug}` | Metricas agrupadas por produto |
| GET | `/api/whatsapp/metrics/cost` | Custo total e por categoria de template |

#### GET `/api/whatsapp/metrics/overview` — Response

```json
{
  "period": { "start": "2026-04-01", "end": "2026-04-07" },
  "totals": {
    "sent": 1250,
    "delivered": 1198,
    "read": 847,
    "replied": 234,
    "converted": 18
  },
  "rates": {
    "delivery_rate": 0.958,
    "read_rate": 0.707,
    "reply_rate": 0.195,
    "conversion_rate": 0.015
  },
  "cost": {
    "total_brl": 287.50,
    "by_category": {
      "marketing": 210.00,
      "utilidade": 67.50,
      "autenticacao": 10.00
    }
  }
}
```

### 4.4 Gerenciamento

| Metodo | Endpoint | Descricao |
|--------|----------|-----------|
| GET | `/api/whatsapp/templates` | Listar templates aprovados |
| POST | `/api/whatsapp/templates` | Submeter template para aprovacao |
| GET | `/api/whatsapp/contacts` | Listar contatos segmentados |
| POST | `/api/whatsapp/contacts/import` | Importar contatos do CRM |
| GET | `/api/whatsapp/sequences` | Listar sequencias configuradas |
| POST | `/api/whatsapp/sequences` | Criar nova sequencia |
| PUT | `/api/whatsapp/sequences/{id}` | Atualizar sequencia existente |
| POST | `/api/whatsapp/sequences/{id}/clone` | Clonar sequencia como base para nova |

---

## 5. Modelo de Dados

Ver `whatsapp-data-model.yaml` para estrutura completa.

### 5.1 Entidades Principais

```
sequences ──< steps
    |
    +──< sequence_enrollments ──< messages
                                     |
contacts ──< sequence_enrollments    |
    |                                |
    +───────────────────────> messages
                                     |
templates ──────────────────> messages
                                     |
metrics (agregado por sequencia/template/periodo)
```

### 5.2 Resumo das Entidades

| Entidade | Descricao | Volume Estimado |
|----------|-----------|----------------|
| `sequences` | Fluxo de nurturing (28 base + customizados) | ~50-100 |
| `steps` | Passos dentro de uma sequencia | ~300-500 |
| `templates` | Templates HSM aprovados pela Meta | ~50-80 |
| `contacts` | Leads e clientes no WhatsApp | ~2.000-10.000 |
| `messages` | Mensagens enviadas/recebidas | ~50.000/mes |
| `metrics` | Agregacoes de performance | ~500/mes |
| `sequence_enrollments` | Contato inscrito em sequencia | ~5.000-20.000 |
| `broadcasts` | Envios em massa segmentados | ~20-50/mes |

---

## 6. Integracao com Pipeline de Atomizacao

### 6.1 Como o WhatsApp recebe conteudo

O SemanticAtomizer do pipeline de conteudo ja transforma pecas grandes em atomos reutilizaveis. O modulo WhatsApp consome esses atomos:

```
Master Content (Atlas)
  -> SemanticAtomizer
    -> whatsapp_nurturing format (max 1000 chars, conversacional)
    -> whatsapp_catalog format (max 500 chars, specs resumidas)
    -> whatsapp_broadcast format (max 1000 chars)
  -> WhatsApp Module
    -> Template matching (content -> template HSM mais adequado)
    -> Scheduling (horarios otimos por persona)
    -> Envio via Meta API
```

### 6.2 Mapeamento Atomo -> Template

| Tipo de Atomo | Uso no WhatsApp | Exemplo |
|---------------|-----------------|---------|
| `claim` | Body do template marketing | "LEV entrega 160.000 lux de iluminacao concentrada" |
| `hook` | Primeira linha do body (abertura) | "Sua equipe cirurgica merece melhor visibilidade?" |
| `cta` | Botao de acao do template | "Solicitar demonstracao" |
| `statistic` | Body de template de nurturing | "73% dos centros cirurgicos operam abaixo da norma" |
| `visual` | Header do template (imagem/video) | Foto do produto em ambiente hospitalar |
| `case_study` | Template de avaliacao | Case completo formatado para WhatsApp |

### 6.3 Regras de Adaptacao

1. **Tamanho:** Body max 1024 caracteres — atomos devem ser concisos
2. **Variaveis:** Atomos com placeholders `{{persona}}` sao interpolados no envio
3. **Midia:** Imagens otimizadas para mobile (max 5MB, formato JPEG/PNG)
4. **Videos:** Max 16MB, formato MP4, duracao max 30 segundos para nurturing
5. **Documentos:** PDFs de datasheets e catalogos (max 100MB)

### 6.4 Fluxo de Criacao de Template a partir de Atomo

1. Helix (copywriter) gera conteudo atomizado
2. SemanticAtomizer classifica e armazena atomos
3. Operador seleciona atomos na UI do Content Studio
4. Sistema monta template HSM com atomos selecionados
5. Template e submetido para aprovacao da Meta
6. Apos aprovado, template fica disponivel para sequencias

---

## 7. Restricoes e Limites da Meta API

### 7.1 Janela de 24 Horas

A Meta impoe uma regra fundamental: mensagens de texto livre (session messages) so podem ser enviadas dentro de uma janela de 24h apos a ultima mensagem RECEBIDA do contato.

| Cenario | Permitido | Tipo |
|---------|-----------|------|
| Contato enviou msg ha 2h | Texto livre + templates | Session |
| Contato enviou msg ha 20h | Texto livre + templates | Session |
| Contato nao responde ha 25h | Apenas templates HSM | Template |
| Primeiro contato (nunca interagiu) | Apenas templates HSM | Template |

### 7.2 Rate Limits

| Tier | Mensagens/dia | Requisito |
|------|--------------|-----------|
| Tier 1 (inicio) | 1.000 | Numero verificado |
| Tier 2 | 10.000 | Qualidade boa por 7 dias |
| Tier 3 | 100.000 | Qualidade boa por 7 dias em Tier 2 |
| Tier 4 | Ilimitado | Qualidade boa por 7 dias em Tier 3 |

**Nota:** Para o volume estimado do projeto (~2.000-5.000 msgs/mes), Tier 2 e suficiente.

### 7.3 Qualidade da Conta

A Meta monitora a qualidade da conta baseada em:

| Metrica | Verde | Amarelo | Vermelho |
|---------|-------|---------|----------|
| Taxa de bloqueio | < 2% | 2-5% | > 5% |
| Taxa de report | < 0.1% | 0.1-0.5% | > 0.5% |

**Consequencias de vermelho:** Tier rebaixado, possivel suspensao.

**Mitigacao:**
- Opt-in explicito antes de qualquer envio
- Opcao de opt-out em toda mensagem de marketing
- Frequencia maxima: 2 mensagens de marketing/semana por contato
- Horario de envio: seg-sex 8h-18h, sabado 9h-12h

### 7.4 Aprovacao de Templates

| Aspecto | Regra |
|---------|-------|
| Tempo de aprovacao | 1-24 horas (tipicamente 2-4h) |
| Rejeicoes comuns | Conteudo enganoso, falta de opt-out, variaveis genericas |
| Idioma | Template deve declarar idioma (pt_BR) |
| Variaveis | Devem ter exemplos concretos no envio para aprovacao |
| Alteracao | Template aprovado nao pode ser editado — nova versao necessaria |

### 7.5 Limites Tecnicos

| Recurso | Limite |
|---------|--------|
| Body text | 1024 caracteres |
| Header text | 60 caracteres |
| Footer text | 60 caracteres |
| Botoes | Max 3 (URL, telefone, ou resposta rapida) |
| Variaveis no body | Max 10 |
| Imagem header | Max 5MB (JPEG, PNG) |
| Video header | Max 16MB (MP4) |
| Documento header | Max 100MB (PDF) |
| Mensagens por segundo | 80 msg/s (Tier 1), 1000 msg/s (Tier 4) |

---

## 8. Estimativa de Custos

### 8.1 Precificacao Meta (Brasil, abril 2026)

| Tipo | Custo por Mensagem (BRL) |
|------|--------------------------|
| Template Marketing | ~R$ 0.30 |
| Template Utilidade | ~R$ 0.15 |
| Template Autenticacao | ~R$ 0.10 |
| Session Message (dentro da janela 24h) | Gratis |

### 8.2 Projecao Mensal — Cenario Conservador (500 contatos)

| Item | Quantidade/mes | Custo Unitario | Total |
|------|---------------|----------------|-------|
| Templates Marketing (nurturing) | 500 | R$ 0.30 | R$ 150.00 |
| Templates Utilidade (datasheets, confirmacoes) | 200 | R$ 0.15 | R$ 30.00 |
| Templates Autenticacao | 20 | R$ 0.10 | R$ 2.00 |
| Session Messages (respostas) | 300 | Gratis | R$ 0.00 |
| **Total conservador** | **1.020** | — | **~R$ 182/mes** |

### 8.3 Projecao Mensal — Cenario Escalado (2.000 contatos)

| Item | Quantidade/mes | Custo Unitario | Total |
|------|---------------|----------------|-------|
| Templates Marketing (nurturing) | 3.000 | R$ 0.30 | R$ 900.00 |
| Templates Utilidade (datasheets, confirmacoes) | 1.500 | R$ 0.15 | R$ 225.00 |
| Templates Autenticacao | 100 | R$ 0.10 | R$ 10.00 |
| Session Messages (respostas) | 2.000 | Gratis | R$ 0.00 |
| **Total escalado** | **6.600** | — | **~R$ 1.135/mes** |

### 8.4 Otimizacao de Custo

- **Maximizar janela 24h:** Quando contato responde, aproveitar para enviar conteudo adicional gratis
- **Horarios estrategicos:** Enviar marketing quando probabilidade de resposta e maior (abre janela)
- **Consolidar templates:** Um template versatil com variaveis e mais barato que varios especificos
- **Monitorar ROI:** Custo por lead convertido deve justificar o investimento
- **Meta Business API direta** (Cloud API) em vez de BSP terceirizado — menor custo, controle total

---

## 9. Segmentacao por Persona

### 9.1 Criterios de Classificacao

| Criterio | Como Identificar | Fonte |
|----------|-----------------|-------|
| Cargo/funcao | Campo no cadastro ou CRM | Bitrix24 |
| Departamento | Inferido do cargo | Cadastro |
| Conteudo consumido | Tipo de material baixado/acessado | Pipeline analytics |
| Perguntas feitas | NLP na resposta recebida via WhatsApp | Webhook + classificacao |
| Evento de origem | Qual evento/formulario gerou o lead | Tag de origem |

### 9.2 Fluxos Diferenciados por Persona

#### eng_clinica (Engenheiro Clinico)
- **Tom:** Tecnico, direto, baseado em dados
- **Frequencia:** Ate 3 msgs/semana (alta tolerancia a conteudo tecnico)
- **Conteudo:** Datasheets, normas, comparativos, testes
- **CTA preferido:** "Baixar especificacao completa", "Solicitar demonstracao tecnica"
- **Horario otimo:** Ter-Qui 10h-12h
- **% do volume:** 40%

#### compras (Setor de Compras)
- **Tom:** Objetivo, focado em valor e condicoes
- **Frequencia:** Max 2 msgs/semana (baixa tolerancia a "spam")
- **Conteudo:** ROI, TCO, condicoes comerciais, cases financeiros
- **CTA preferido:** "Solicitar proposta", "Comparar condicoes"
- **Horario otimo:** Seg-Qua 14h-16h
- **% do volume:** 30%

#### equipe_medica (Corpo Medico)
- **Tom:** Clinico, empatico, focado no paciente
- **Frequencia:** Max 1-2 msgs/semana (muito ocupados)
- **Conteudo:** Cases clinicos, ergonomia, workflow, videos curtos
- **CTA preferido:** "Agendar demonstracao", "Ver caso clinico"
- **Horario otimo:** Seg/Qua 7h-8h (antes do expediente clinico)
- **% do volume:** 20%

#### admin (Diretoria/Administracao)
- **Tom:** Executivo, focado em resultados e compliance
- **Frequencia:** Max 1 msg/semana (extremamente seletivos)
- **Conteudo:** Business cases, ROI, compliance, referencias
- **CTA preferido:** "Agendar reuniao", "Ver referencia"
- **Horario otimo:** Seg 9h-10h
- **% do volume:** 10%

### 9.3 Regras de Transicao de Persona

Um contato pode ser reclassificado quando:
- Responde indicando outro decisor: "Vou passar para o engenheiro clinico avaliar"
- CRM atualiza o cargo/funcao
- Padrao de consumo de conteudo muda (ex: admin comeca a baixar datasheets)

---

## 10. Compliance CONAR e Regulatorio

### 10.1 CONAR — Regra Fundamental

**NUNCA citar concorrentes direta ou indiretamente.** Isso vale para:

- Templates HSM
- Mensagens de texto livre
- Respostas automaticas
- Comparativos (sempre "solucoes tradicionais" ou "media de mercado", nunca marcas)

### 10.2 ANVISA

- Dispositivos medicos classe I-IV: comunicacao deve respeitar classificacao regulatoria
- Claims devem ser comprovanveis e alinhados com registro ANVISA
- Nao fazer promessas terapeuticas absolutas

### 10.3 LGPD

- **Opt-in explicito** obrigatorio antes de enviar mensagens marketing
- Template AUTH-001 confirma consentimento
- **Opt-out facil** em toda mensagem ("Responda SAIR para cancelar")
- **Retencao de dados:** Mensagens armazenadas por max 2 anos
- **Portabilidade:** Contato pode solicitar exportacao dos seus dados
- **Base legal:** Consentimento (marketing) ou execucao contratual (utilidade)

### 10.4 Politicas Meta

- Sem conteudo enganoso ou spam
- Templates revisados antes de submissao
- Respeitar horario comercial (8h-18h seg-sex)
- Nao enviar mensagens entre 20h e 8h (exceto utilidade urgente)
- Manter taxa de bloqueio abaixo de 2%

---

## Pre-requisitos para Implementacao (Story 15.2)

1. [ ] Conta Meta Business verificada
2. [ ] Numero WhatsApp Business dedicado
3. [ ] API direta (Cloud API) configurada
4. [ ] Templates HSM submetidos e aprovados pela Meta
5. [ ] Webhook endpoint publico (HTTPS) configurado
6. [ ] Integracao com CRM Bitrix24 (Story 15.5)

---

## Apendice A: Glossario

| Termo | Definicao |
|-------|-----------|
| HSM | Header-Structured Message — template pre-aprovado pela Meta |
| Session Message | Mensagem livre dentro da janela de 24h |
| WAMID | WhatsApp Message ID — identificador unico da mensagem na Meta |
| BSP | Business Solution Provider — intermediario certificado pela Meta |
| Sequence | Fluxo automatizado de N mensagens com delays definidos |
| Enrollment | Inscricao de um contato em uma sequencia |
| Atom | Unidade minima de conteudo gerada pelo SemanticAtomizer |

## Apendice B: Decisoes Arquiteturais

| Decisao | Escolha | Justificativa |
|---------|---------|---------------|
| API direta vs BSP | API direta (Cloud API) | Controle total, sem intermediario, menor custo |
| Storage de mensagens | PostgreSQL | Ja usado no Content Studio, consistencia transacional |
| Fila de envio | Redis + Bull | Ja disponivel na infra, controle de rate limit |
| Webhook processing | Async worker | Desacoplar recebimento de processamento |
| Template versioning | Versionamento imutavel | Templates aprovados nunca sao editados, apenas nova versao |

---

*Arquitetura definida por @architect (Aria) — Story 15.1 — Epic 15*
*Fonte: Auditoria IC — WhatsApp Score 95/100, Canal #1 validado*
