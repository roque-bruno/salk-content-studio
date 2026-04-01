# PRD v1.0 — Content Studio: Features Locais (Sem API Keys)

**Projeto:** Manager Grupo — Content Studio
**Versao:** 1.0
**Status:** Aprovado
**Data:** 2026-04-01
**Autor:** @pm (Morgan)
**Contexto:** Plataforma em preview mode enquanto cartao corporativo nao libera API keys. Todas as features abaixo funcionam com dados locais (YAML, SQLite, uploads).

---

## 1. OBJETIVO

Tornar o Content Studio **utilizavel pela gestora de marketing HOJE**, mesmo sem API keys. A gestora deve conseguir planejar conteudo, criar pecas manualmente, organizar o calendario editorial, verificar compliance, aprovar pecas e gerar relatorios — tudo via browser.

## 2. PRINCIPIO

> **Util sem IA > Bonito sem funcao. Cada tela deve entregar valor real com dados locais.**

## 3. EPICOS

### Epic 8 — Dashboard Inteligente
**Objetivo:** Dashboard com KPIs reais do banco local, metricas de producao, resumo de integracoes.
**Valor:** Gestora ve o estado real da producao ao abrir o sistema.

### Epic 9 — Calendario Editorial Funcional
**Objetivo:** Planejamento semanal/mensal de conteudo baseado nos templates YAML.
**Valor:** Gestora planeja a semana inteira de conteudo sem sair do browser.

### Epic 10 — Pipeline de Producao Manual
**Objetivo:** Fluxo completo de criacao manual de pecas (sem IA): upload imagem, escrever copy, selecionar plataforma, mover pelo pipeline.
**Valor:** Producao funciona mesmo sem API keys — gestora cria pecas manualmente.

### Epic 11 — Compliance & Brand Check
**Objetivo:** Validacao real de copy contra prohibited terms, claims bank e brand guidelines.
**Valor:** Zero violacoes ANVISA/CFM publicadas.

### Epic 12 — Relatorios & Analytics
**Objetivo:** Relatorio semanal com dados locais, exportacao PDF, dashboard executivo.
**Valor:** Diretoria recebe visao executiva da producao.

### Epic 13 — Gestao de Assets
**Objetivo:** Biblioteca visual organizada com upload, tagueamento e busca.
**Valor:** Todos os assets visuais centralizados e acessiveis.

---

## 4. FORA DE ESCOPO

- Geracao de conteudo por IA (depende de API keys)
- Publicacao real em redes sociais (depende de tokens)
- Integracao com Supabase (SQLite local suficiente)
- Video pipeline (depende de Kling/Veo3 APIs)

## 5. DADOS LOCAIS DISPONIVEIS

| Arquivo | Conteudo | Uso |
|---------|----------|-----|
| platform-specs.yaml | Limites de copy, dimensoes, frequencia | Calendario, validacao |
| buyer-personas.yaml | 5+ personas por marca | Copy direcionado |
| hashtag-bank.yaml | Hashtags por marca/produto | Sugestao automatica |
| claims-bank.yaml | Claims aprovados por produto | Compliance check |
| prohibited-terms.yaml | Termos bloqueados ANVISA/CFM | Compliance gate |
| brand-guidelines.yaml | Paleta, logo, tom de voz | Brand check |
| editorial-calendar-template.yaml | Frequencias, temas, formatos | Geracao de calendario |
| 4x brandbook YAMLs | Diretrizes detalhadas por marca | Referencia |

## 6. METRICAS DE SUCESSO

| Metrica | Antes | Depois |
|---------|-------|--------|
| Telas funcionais (com dados reais) | 3/21 | 15/21 |
| Pecas criaveis sem API | 0 | ilimitado |
| Compliance check funcional | Nao | Sim |
| Relatorio semanal exportavel | Nao | Sim (PDF) |
| Assets organizados | Nao | Sim (tags + busca) |

---

*@pm (Morgan) — 2026-04-01*
