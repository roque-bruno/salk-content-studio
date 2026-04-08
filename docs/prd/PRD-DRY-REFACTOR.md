# PRD: DRY Refactor — Eliminacao de Duplicacoes no Content Studio

**Versao:** 1.0
**Data:** 2026-04-08
**Autor:** Orion (AIOX Master)
**Status:** Em Execucao

---

## 1. Problema

O Content Studio acumulou duplicacoes criticas ao longo do desenvolvimento rapido:
- **9 endpoints backend** fazendo a mesma operacao com configuracoes diferentes
- **26 hardcodes** de "salk", **15** de "instagram" espalhados pelo codigo
- **5 funcoes frontend** para gerar imagem, **3** para criar peca, **4** batch loops identicos
- **115 try-catch** com 3 padroes diferentes de tratamento de erro
- **Monolito app.py** com 3000+ linhas sem separacao de responsabilidades

**Impacto direto:** Bug no NB2 levou 5 deploys para corrigir porque a logica estava em 3 caminhos diferentes. Cada feature nova copia o padrao anterior ao inves de reusar.

## 2. Objetivo

Reduzir complexidade do codebase em ~30% eliminando duplicacoes, unificando caminhos e extraindo padroes reutilizaveis. **Zero mudanca de funcionalidade** — pure refactor.

## 3. Principios

| # | Principio | Descricao |
|---|-----------|-----------|
| P1 | **Menos e mais** | Uma funcao, um proposito, um caminho |
| P2 | **DRY absoluto** | Se aparece 2x, vira funcao/constante |
| P3 | **Zero regressao** | Todos endpoints devem retornar exatamente o mesmo resultado |
| P4 | **Incremental** | Cada story e deployavel independente |
| P5 | **Teste antes** | Capturar comportamento atual antes de refatorar |

## 4. Escopo

### IN SCOPE
- Extrair constantes e defaults compartilhados
- Unificar funcoes utilitarias (parse notes, notifications)
- Consolidar endpoints duplicados (imagem, briefing, prompt, copy)
- Unificar pipeline de producao (produce_single_piece + _produce_slot)
- Consolidar funcoes frontend (batch ops, wrappers, piece creation)
- Endpoint factory para 12 pares GET/PUT de dados
- Limpar imports duplicados

### OUT OF SCOPE
- Novas funcionalidades
- Mudancas de UI/UX
- Migracao de banco
- Separacao do monolito em modulos (epic futuro)

## 5. Metricas de Sucesso

| Metrica | Antes | Meta |
|---------|-------|------|
| Linhas app.py | ~3000 | < 2200 (-25%) |
| Linhas index.html JS | ~3500 | < 2800 (-20%) |
| Endpoints duplicados | 9 | 0 |
| Hardcodes "salk"/"instagram" | 41 | 0 (constantes) |
| Funcoes frontend duplicadas | 12+ | 0 |

## 6. Riscos

| Risco | Mitigacao |
|-------|----------|
| Regressao em endpoint existente | Snapshot de responses antes/depois |
| Frontend quebra | Teste manual de cada fluxo apos cada story |
| Deploy parcial inconsistente | Cada story e atomica e deployavel |

## 7. Epic e Stories

Ver: `docs/stories/epic-16-dry-refactor/`

## 8. Quality Gate

Checklist obrigatorio por story:
1. Nenhum endpoint mudou sua response shape
2. Todos botoes do frontend funcionam igual
3. `docker restart` apos deploy de Python
4. Teste do fluxo completo: criar peca → gerar copy → gerar prompt → gerar imagem
