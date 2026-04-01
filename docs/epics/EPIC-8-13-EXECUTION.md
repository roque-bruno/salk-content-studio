# Epicos 8-13 — Features Locais (Sem API Keys)

**PRD:** PRD-studio-local-features.md
**Status:** Done (implementacao YOLO mode)
**Inicio:** 2026-03-31
**Owner:** @pm (Morgan) — orquestracao / @dev (Dex) — execucao

---

## Epic 8 — Dashboard Inteligente

**Status:** Done

### Implementacao
- **Backend (services.py):** `get_dashboard_stats()` expandido com 20+ KPIs:
  - `pieces_this_week` — producao dos ultimos 7 dias
  - `stage_breakdown` — distribuicao por estagio
  - `brand_breakdown` — distribuicao por marca
  - `platform_breakdown` — distribuicao por plataforma
  - `calendar_weeks`, `calendar_total_slots`, `calendar_filled_slots`
  - `compliance_rules_active` — total de regras de compliance ativas
  - `reviews_pending`, `reviews_approved`, `reviews_rejected`
  - `pieces_approved`, `pieces_published`, `pieces_total`

- **Frontend (index.html):** Segunda linha de KPIs adicionada:
  - Pecas esta Semana | Semanas Planejadas | Regras Compliance | Reviews Pendentes | Assets Visuais
  - Quick Actions expandidas: +Verificar Compliance, +Gerenciar Assets

---

## Epic 9 — Calendario Editorial Funcional

**Status:** Ja funcional (pre-existente)

Calendario com 7 endpoints, geracao de slots via template YAML, edicao de slots, producao de semana. Sem alteracoes necessarias — ja atendia os requisitos do PRD.

---

## Epic 10 — Pipeline de Producao Manual

**Status:** Ja funcional (pre-existente)

Criacao manual de pecas com formulario completo (titulo, marca, produto, plataforma, formato, pilar, persona, notas). Kanban com drag-and-drop entre 6 estagios. 8 templates rapidos. Sem alteracoes necessarias.

---

## Epic 11 — Compliance & Brand Check

**Status:** Done (BUG CRITICO CORRIGIDO)

### Bug Corrigido
`check_compliance()` em services.py nao iterava os termos proibidos do YAML. O codigo procurava chaves `categories`/`prohibitions` que nao existiam — a YAML usa chaves top-level como `produtos_bloqueados`, `superlativos`, `promessas`, etc.

### Implementacao
- **services.py `check_compliance()`** — reescrito para iterar todas as chaves top-level do YAML
  - Agora processa: `produtos_bloqueados`, `superlativos`, `promessas`, `comparativos`, `urgencia_falsa`, `visual_prohibitions`, `alem_registro`
  - Suporta tanto `terms` (lista de dicts) quanto `items` (lista de strings)
  - Deduplicacao inteligente de violacoes ETRUS

- **services.py `_validate_claims()`** — NOVO metodo
  - Valida especificacoes tecnicas contra claims-bank.yaml
  - Detecta specs numericas (lux, kg, Ra, IP, Kelvin) nao encontradas no banco
  - Retorna `approved_used` (claims aprovados encontrados) e `unapproved` (specs sem cobertura)

- **Frontend** — Claims validation display adicionado ao resultado do compliance check
  - Badge OK/ATENCAO para validacao de claims
  - Lista de claims aprovados encontrados (badge verde)
  - Lista de specs nao encontradas no banco (warning)
  - Contadores: total de claims aprovados e regras de compliance ativas

---

## Epic 12 — Relatorios & Analytics

**Status:** Done

### Implementacao
- **app.py** — Novo endpoint `GET /api/report/weekly/download`
  - Retorna HTML com CSS otimizado para impressao (@media print, @page A4)
  - Content-Disposition: attachment (download automatico)
  - Suporte a filtro por brand e week_id

- **Frontend** — Botao "Download" adicionado ao dashboard
  - `downloadWeeklyReport()` — abre download do relatorio HTML
  - Instrucao: "Ctrl+P para gerar PDF"

---

## Epic 13 — Gestao de Assets

**Status:** Done

### Implementacao Backend (app.py)
- `DELETE /api/uploads/{purpose}/{filename}` — exclusao de arquivos
- `GET /api/assets/tags/{purpose}/{filename}` — leitura de tags/metadata
- `PUT /api/assets/tags/{purpose}/{filename}` — atualizacao de tags/metadata
- `GET /api/assets/search?q=&tag=&brand=&purpose=` — busca com filtros

Metadata armazenada em arquivos `.meta.json` ao lado de cada upload.

### Implementacao Frontend (index.html)
- Nova sub-tab "Uploads" na aba Assets
- Formulario de upload com campos: arquivo, proposito, marca, tags, descricao
- Grid visual com preview de imagens e videos
- Botao de exclusao por arquivo
- Busca e filtros por nome, tag, marca, proposito
- Tags exibidas como badges em cada card

### Variaveis Alpine.js adicionadas
- `uploadsFiltered`, `uploadAssetFile`, `uploadAssetPurpose`, `uploadAssetBrand`
- `uploadAssetTags`, `uploadAssetDescription`, `uploadAssetUploading`
- `uploadSearchQuery`, `uploadFilterPurpose`, `uploadFilterBrand`

### Metodos adicionados
- `loadUploadsAll()` — carrega uploads com metadata
- `doAssetUpload()` — upload com FormData + save tags
- `deleteUpload(file)` — exclusao com confirmacao
- `searchUploads()` — filtro client-side por nome/tag/marca/proposito

---

## Arquivos Modificados

| Arquivo | Alteracoes |
|---------|-----------|
| `packages/content-pipeline/src/content_pipeline/web/services.py` | Fix compliance, add claims validation, enhance dashboard stats |
| `packages/content-pipeline/src/content_pipeline/web/app.py` | New endpoints: assets CRUD, tags, search, report download |
| `packages/content-studio-frontend/index.html` | Dashboard KPIs, compliance claims UI, assets management, report download |
| `packages/content-pipeline/src/content_pipeline/web/static/index.html` | Sync copy of frontend |

---

*@pm (Morgan) — 2026-03-31 — Execucao YOLO mode*
