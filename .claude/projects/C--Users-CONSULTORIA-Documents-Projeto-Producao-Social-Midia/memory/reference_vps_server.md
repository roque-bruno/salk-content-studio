---
name: VPS Server Details
description: Servidor VPS WHM do Manager Grupo — hospeda salkmedical.com, dayho.com.br. Destino do deploy do Content Studio.
type: reference
---

**IP:** 162.240.13.51
**SSH porta:** 22022
**Painel:** WHM (Web Host Manager) — VPS controlado
**Domínios hospedados:** salkmedical.com, dayho.com.br (e possivelmente outros do Manager Grupo)
**DNS resolver interno:** manager05.MANAGER.local (192.168.10.249)

**studio.salkmedical.com:**
- Hoje: CNAME → synkra-content-studio.onrender.com (Render)
- Futuro: A record → 162.240.13.51 (VPS)

**Render (legado):**
- URL: synkra-content-studio.onrender.com
- Status: funcionando (v2.0.0, versao antiga)
- Sera desativado apos migracao pro VPS

**GitHub repo:** roque-bruno/salk-content-studio (publico)
**GitHub secrets configurados:** RENDER_API_KEY, RENDER_SERVICE_ID, STUDIO_API_URL, STUDIO_USER, STUDIO_PASS

**Squad de infra:** Equipe dedicada gerencia o servidor WHM. Comunicacao via documento de requisicao.
