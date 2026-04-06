---
name: Frontend Fixes Pending Commit
description: Fixes aplicados ao index.html do Content Studio ainda nao commitados — drawer, conexao, retry, cache headers
type: project
---

Fixes aplicados em 2026-03-31, presentes em ambos os arquivos (sincronizados):
- `packages/content-studio-frontend/index.html`
- `packages/content-pipeline/src/content_pipeline/web/static/index.html`

**Fixes:**

1. **Drawer x-if** — Convertido de `x-show` para `<template x-if="showPieceDetail">`. Remove o drawer completamente do DOM quando fechado, em vez de depender de CSS display:none. Resolve bug onde o drawer aparecia no layout mesmo com showPieceDetail=false.

2. **Conexao estavel** — `connectionOk` agora so marca `false` em erro de rede (`TypeError` = servidor inacessivel). Erros HTTP (404, 500) mantêm `connectionOk = true` porque o servidor respondeu.

3. **Retry inteligente** — Retry (3 tentativas) agora so acontece em falha de rede. Erros HTTP fazem `break` imediato (sem retry inutil). Elimina o banner "Reconectando ao servidor..." quando endpoints retornam 404/500.

4. **Anti-cache headers** — Meta tags `Cache-Control: no-cache`, `Pragma: no-cache`, `Expires: 0` adicionadas ao head.

5. **Diretorio de dados** — Criado `packages/squads/content-production/data/` (health check reclamava que nao existia).

**Why:** Estes fixes estao aplicados localmente mas NAO commitados. Precisam entrar no proximo commit antes do deploy.

**How to apply:** No proximo commit, incluir ambos os index.html. Mensagem sugerida: `fix: drawer DOM removal, connection stability, smart retry, cache headers`
