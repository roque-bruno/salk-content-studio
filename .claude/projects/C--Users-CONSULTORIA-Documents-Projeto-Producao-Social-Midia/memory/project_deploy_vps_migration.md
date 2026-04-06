---
name: Deploy VPS Migration
description: Migracao do Content Studio de Render para VPS WHM proprio (162.240.13.51). Documento de requisicao gerado para squad infra.
type: project
---

Migracao do Salk Content Studio do Render (synkra-content-studio.onrender.com) para VPS proprio com WHM.

**Status (2026-03-31):** Documento de requisicao gerado (`docs/REQUISICAO-INFRA-CONTENT-STUDIO.md`), aguardando squad de infra completar 14 itens.

**Arquitetura decidida:**
- Docker container no VPS 162.240.13.51
- Apache reverse proxy (WHM) → 127.0.0.1:8000
- SSL via AutoSSL do WHM
- DNS: studio.salkmedical.com → A record para o VPS (hoje aponta pro Render via CNAME)
- CI/CD: GitHub Actions → SSH (usuario `deployer`) → docker compose up
- Backup: /opt/content-studio/{data,uploads,settings}

**Why:** Render free tier tem cold start de 15-30s e eh infraestrutura externa desnecessaria. VPS WHM ja esta pago, tem uptime 100%, e eh controlado pela equipe.

**How to apply:** Quando squad infra devolver checklist completo: gerar deploy key SSH, atualizar `.github/workflows/deploy.yml` (trocar Render API por SSH), commitar fixes pendentes, executar primeiro deploy. Testar com 4 comandos curl de validacao do documento.

**Pendencias antes do deploy:**
1. Squad infra completar os 14 itens do checklist
2. Commitar fixes do frontend (drawer x-if, conexao, retry, cache headers)
3. Gerar SSH deploy key e configurar no GitHub Secrets
4. Configurar GOOGLE_API_KEY no .env de producao
