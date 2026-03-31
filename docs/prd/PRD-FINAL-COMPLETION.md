# PRD Final — Salk Content Studio v2.0 Completion

**Versao:** 3.0-FINAL
**Data:** 2026-03-31
**Status:** EXECUCAO
**Autor:** Orion (AIOX Master)

---

## 1. Contexto

O Salk Content Studio v2.0 e o sistema web para a gestora de marketing do Manager Grupo produzir e gerenciar conteudo para redes sociais de 4 marcas (Salk Medical, Mendel Medical, Manager Grupo, Dayho) no setor B2B healthcare.

**Estado atual:**
- Frontend: 9.115 linhas (Alpine.js SPA), 22 tabs funcionais
- Backend: 2.305 linhas (FastAPI), 113 endpoints
- Pipeline Python: 40+ modulos (NB2, video, automacao, publishers)
- 16 commits a frente de origin/main

**O que falta para entrega final:**

---

## 2. Gaps Identificados na Auditoria

### 2.1 MOBILE RESPONSIVENESS (CRITICO)
- Media queries existem mas sao basicas (900px, 768px, 600px, 480px)
- Tabs complexas (studio, video, editor, calendar) NAO foram testadas em mobile
- Sidebar mobile com hamburger existe mas drawers/modals nao adaptam bem
- Dashboard grid colapsa mas KPIs ficam apertados
- Forms com multiplas colunas nao stackam em mobile
- Kanban horizontal nao tem scroll hint em telas pequenas

### 2.2 FLUXO DE PRODUCAO END-TO-END
- Nao existe um wizard/fluxo guiado: "Criar peca do zero ate publicar"
- A gestora precisa saber QUAL tab ir em QUAL ordem
- Falta breadcrumb de progresso da peca ("Briefing > Copy > Design > Review > Publicar")
- Quick Produce existe mas nao conecta com publish flow

### 2.3 NOTIFICACOES E FEEDBACK
- Sistema de notificacoes existe no frontend (badge + drawer) mas backend nao gera notificacoes reais
- Falta endpoint GET /api/notifications
- Falta websocket ou polling para notificacoes em tempo real
- Toast notifications sao transitorias — gestora pode perder avisos importantes

### 2.4 BUSCA GLOBAL
- Search bar existe no header mas nao busca em todos os dados
- Falta search em: reviews, calendar slots, claims, hashtags, settings
- Command palette (Ctrl+K) busca tabs e acoes mas nao pecas por conteudo

### 2.5 PERFORMANCE & LOADING
- Skeleton loading existe para board, mas tabs secundarias carregam em branco
- Nao ha cache de dados no frontend (cada troca de tab re-fetcha)
- Falta indicador de progresso para operacoes longas (generate-image, video pipeline)
- Falta retry automatico em falhas de rede

### 2.6 PERSISTENCIA DE ESTADO
- Filtros nao persistem entre sessoes (brand, product, status filters)
- Estado do editor (copy em progresso) nao salva automaticamente
- Historico de busca nao e mantido
- Dashboard layout persiste (localStorage) mas outros prefs nao

### 2.7 ONBOARDING & HELP
- Onboarding welcome modal existe mas e basico
- Falta tour guiado nas funcionalidades principais
- Falta tooltips contextuais nos botoes de acao
- Falta pagina de help/FAQ inline

### 2.8 EXPORTACAO & RELATORIOS
- CSV export existe para pecas
- Falta export PDF do dashboard
- Falta export do calendario editorial
- Relatorio semanal (GET /api/report/weekly) existe no backend mas nao tem UI
- Falta compartilhamento de relatorio por link

### 2.9 INTEGRACAO VISUAL
- Phone preview existe mas so para copy (nao mostra imagem + copy juntos)
- Falta preview de como o post vai parecer no Instagram/LinkedIn/Facebook
- Falta grid preview (como o feed do Instagram vai ficar com os novos posts)
- Falta preview de carrossel

### 2.10 GESTAO DE EQUIPE & PERMISSIONS
- Login/auth existe (JWT) mas e single-user
- Falta conceito de roles (gestora, designer, revisora)
- Falta log de atividades (quem fez o que)
- Falta assignment de pecas para membros da equipe

### 2.11 BACKEND GAPS
- Muitos endpoints retornam mock data (nao conectam com servicos reais)
- Settings store salva em JSON file — nao e production-grade
- Falta rate limiting nos endpoints
- Falta CORS configurado corretamente para deploy
- Falta health check mais completo (verificar conectividade com APIs externas)
- Upload endpoint existe mas nao persiste arquivos de forma robusta

### 2.12 POLISH VISUAL FINAL
- Animacoes de transicao entre tabs sao abruptas
- Falta micro-animacoes em acoes (botao pressionado, card criado)
- Status pills poderiam ter icones alem de cores
- Falta dark/light mode toggle (so dark agora)
- Favicons e app icons nao existem (manifest.json tem placeholders)

---

## 3. Plano de Execucao — 8 Rounds

### ROUND 16: Mobile-First Responsive Overhaul (@dev)
**Prioridade:** CRITICA
**Escopo:**
- [ ] Rewrite complete mobile CSS (< 768px): stack all grids to single column
- [ ] Mobile-optimized header: compact logo, hamburger, only essential actions
- [ ] Swipeable kanban board para mobile (horizontal scroll with snap)
- [ ] Responsive forms: all multi-column layouts stack on mobile
- [ ] Touch-friendly: minimum 44px tap targets, swipe gestures
- [ ] Bottom navigation bar for mobile (tabs mais usadas)
- [ ] Drawer/modal full-screen on mobile
- [ ] Test at 375px (iPhone SE), 390px (iPhone 14), 768px (iPad)

### ROUND 17: Production Wizard & Flow Guide (@dev)
**Prioridade:** CRITICA
**Escopo:**
- [ ] Step-by-step production wizard: Briefing > Copy > Visual > Review > Publish
- [ ] Piece progress indicator (breadcrumb bar no drawer de detalhe)
- [ ] Guided first-piece flow for new users
- [ ] Smart suggestions: "Peca X esta pronta para revisao" toasts
- [ ] Quick actions context menu: right-click or long-press on piece
- [ ] Batch operations toolbar: select multiple pieces, change stage, delete
- [ ] "O que fazer agora?" dashboard widget showing pending actions per stage

### ROUND 18: Notification System & Activity Log (@dev)
**Prioridade:** ALTA
**Escopo:**
- [ ] Backend: GET /api/notifications endpoint com notificacoes persistidas
- [ ] Backend: Gerar notificacoes em acoes (peca criada, review aprovada, etc)
- [ ] Frontend: Notification center (drawer com historico completo)
- [ ] Frontend: Polling a cada 30s para novas notificacoes
- [ ] Activity log tab: quem fez o que e quando (audit trail)
- [ ] Notification preferences: escolher o que gera notificacao
- [ ] Badge count atualizado em tempo real

### ROUND 19: Social Media Preview & Grid (@dev)
**Prioridade:** ALTA
**Escopo:**
- [ ] Instagram feed preview: mockup do grid 3x3 com posts existentes + novos
- [ ] Instagram story preview: mockup 9:16
- [ ] LinkedIn post preview: mockup com avatar da marca + copy + imagem
- [ ] Facebook post preview: mockup com imagem + copy
- [ ] Carousel preview: swipeable mockup multi-slide
- [ ] Platform-specific character limits e warnings
- [ ] Preview responsivo (simula tela do celular no desktop)

### ROUND 20: Data Caching, Performance & Retry (@dev)
**Prioridade:** ALTA
**Escopo:**
- [ ] Frontend data cache layer com TTL (pieces, calendar, reviews = 60s cache)
- [ ] Skeleton loading for ALL tabs (not just board)
- [ ] Progressive loading: load visible tab first, preload adjacent
- [ ] Retry with exponential backoff para API calls
- [ ] Long-operation progress: image gen mostra % progresso
- [ ] Optimistic UI updates (move card, update immediately, rollback on error)
- [ ] Filter persistence in localStorage
- [ ] Auto-save draft copy every 30s

### ROUND 21: Reports, Export & Weekly Summary (@dev)
**Prioridade:** MEDIA
**Escopo:**
- [ ] Weekly report UI tab: integrar /api/report/weekly com visualizacao
- [ ] PDF export do dashboard (html2canvas + jsPDF via CDN)
- [ ] Calendar export: download .ics do calendario editorial
- [ ] Share report via link (gerar URL temporaria)
- [ ] Email digest mockup (preview de como o email semanal ficaria)
- [ ] Export pecas como zip (copy + imagem + metadata JSON)
- [ ] Print-friendly views for all tabs (not just dashboard)

### ROUND 22: Onboarding, Help & Polish (@dev)
**Prioridade:** MEDIA
**Escopo:**
- [ ] Interactive onboarding tour (highlight key features step by step)
- [ ] Contextual help tooltips on every major action button
- [ ] Help page with FAQ, keyboard shortcuts, glossary
- [ ] Tab transition animations (smooth fade/slide)
- [ ] Micro-animations: button press, card creation, stage change
- [ ] Status pills with icons (not just colored dots)
- [ ] Favicons and PWA icons (generate from Salk logo)
- [ ] Loading states refinement: shimmer effect everywhere
- [ ] Error boundaries: friendly error messages when API fails

### ROUND 23: Backend Hardening & Deploy Prep (@dev)
**Prioridade:** CRITICA
**Escopo:**
- [ ] CORS configuration for production domain
- [ ] Rate limiting middleware (slowapi)
- [ ] Health check endpoint: verify all external API keys
- [ ] File upload persistence (save to disk with proper naming)
- [ ] Database migration: SQLite schema versioning
- [ ] Environment-based config (dev vs prod)
- [ ] Startup validation: check required API keys exist
- [ ] Error logging middleware (structured JSON logs)
- [ ] Gzip compression middleware
- [ ] Static file cache headers (1 year for hashed assets)
- [ ] requirements.txt audit: pin all versions
- [ ] Dockerfile for production deployment
- [ ] docker-compose.yml: app + nginx reverse proxy
- [ ] README.md with deployment instructions

---

## 4. Distribuicao por Squad

| Round | Agente Principal | Agente Support | Estimativa |
|-------|-----------------|----------------|------------|
| 16 | @dev (Dex) | @ux-design-expert (Uma) | Frontend CSS |
| 17 | @dev (Dex) | @pm (Morgan) | Frontend JS+HTML |
| 18 | @dev (Dex) | @data-engineer (Dara) | Full-stack |
| 19 | @dev (Dex) | @ux-design-expert (Uma) | Frontend HTML+CSS |
| 20 | @dev (Dex) | @architect (Aria) | Frontend JS |
| 21 | @dev (Dex) | @analyst (Alex) | Full-stack |
| 22 | @dev (Dex) | @ux-design-expert (Uma) | Frontend |
| 23 | @dev (Dex) | @devops (Gage) | Backend + Infra |

---

## 5. Criterios de Aceite Final

### O sistema esta PRONTO quando:
1. Funciona em mobile (iPhone 14 / iPad) sem layout quebrado
2. Gestora consegue criar peca do zero ate publicar sem ajuda tecnica
3. Todas as tabs carregam em < 2s com skeleton loading
4. Notificacoes informam sobre mudancas de status das pecas
5. Preview mostra como o post vai ficar na rede social
6. Dashboard pode ser exportado como PDF
7. Backend roda com Docker em qualquer servidor
8. Todas as API keys sao validadas na inicializacao
9. README explica como fazer deploy

---

## 6. Definition of Done

- [ ] Todos os 8 rounds implementados e commitados
- [ ] Zero TODO/FIXME/PLACEHOLDER no codigo
- [ ] Mobile testado em 3 breakpoints (375px, 390px, 768px)
- [ ] Todos os endpoints com error handling adequado
- [ ] Dockerfile + docker-compose funcional
- [ ] README.md com instrucoes de deploy
- [ ] Push para remote via @devops
