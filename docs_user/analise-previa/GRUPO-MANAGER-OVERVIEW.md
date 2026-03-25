# Manager Grupo — Overview Completo dos Ativos Digitais
**Gerado por:** Orion (aiox-master) — 2026-03-13
**Objetivo:** Mapeamento read-only de todos os sites do grupo

---

## 1. VISÃO GERAL DO GRUPO

### Estrutura Corporativa
- **Nome:** Manager Grupo — "Integrando Soluções"
- **Fundação:** 2014
- **Sede:** Rua Expedicionário Antônio Machado, 40, Afonso Pena, São José dos Pinhais, PR — CEP 83.050-535
- **Setor:** B2B Saúde e Indústria
- **Posicionamento:** "Excelência em oferta e variedades para o setor da saúde"
- **Contato Central:** +55 (41) 3138-5900 | SAC: 0800 041 7255
- **Horário:** Seg-Sex 8h às 17h45

### 5 Unidades de Negócio

| # | Empresa | Papel | URL | Status |
|---|---------|-------|-----|--------|
| 1 | **Manager Grupo** | Holding / Portal institucional | managergrupo.com.br | Ativo |
| 2 | **Mendel Medical** | Fabricante equipamentos médicos | mendelmedical.com.br | Ativo — FOCO DO PROJETO |
| 3 | **Salk Medical** | Comercialização / Representação | salkmedical.com.br | Ativo |
| 4 | **Dayho Metalmecânica** | Usinagem / Metalurgia | dayho.com.br | Ativo |
| 5 | **Salk Fitness** | Equipamentos fitness | salkfitness.com.br | Em hibernação |

### Cadeia de Valor
```
Dayho (fabrica peças/estruturas) → Mendel (monta equipamentos médicos) → Salk Medical (comercializa) → Hospitais/Clínicas
                                                                          ↑
                                                               Manager Grupo (coordena)
```

### Endereço Único
Todas as 5 empresas operam no **mesmo endereço físico** e compartilham o **mesmo servidor** (162.240.13.51).

---

## 2. COMPARATIVO TÉCNICO DOS SITES

| Aspecto | Manager Grupo | Salk Medical | Mendel Medical | Dayho | Salk Fitness |
|---------|--------------|-------------|---------------|-------|-------------|
| **WP Version** | 6.8.5 | 6.8.5 | 6.9.4 | Não detectado | 6.9.4 |
| **Page Builder** | Elementor | Elementor Pro 3.32.4 | Elementor Pro 3.35.5 | Elementor | Elementor |
| **Tema** | Manager (custom) | Hello Elementor Child | Hello Elementor | Dayho (custom v3.0) | Salk Fitness (custom) |
| **Produto Engine** | — | JetEngine | Elementor nativo | — | WooCommerce |
| **Chat** | Bitrix24 | Não | Bitrix24 | Bitrix24 | Não |
| **Analytics** | GA4 + GTM | GTM + FB Pixel | GA + GTM | Não detectado | Não detectado |
| **LMS** | Tutor LMS + Pro | — | — | — | — |
| **E-commerce** | WooCommerce (ref.) | — | — | — | WooCommerce |
| **Formulários** | — | CF7/WPForms | CF7 + WPForms | — | CF7 |
| **Blog Ativo** | Vazio/inativo | Parado out/2025 | Não verificado | Não detectado | Parado fev/2018 |
| **Servidor** | 162.240.13.51 | 162.240.13.51 | 162.240.13.51 | 162.240.13.51 | 162.240.13.51 |

### Credenciais WordPress (Admin)

| Site | URL Admin | User | Permissão |
|------|-----------|------|-----------|
| Manager Grupo | managergrupo.com.br/wp-admin/ | botmanager | Administrador |
| Salk Medical | salkmedical.com.br/wp-admin/ | botsalk | Administrador |
| Mendel Medical | mendelmedical.com.br/wp-admin | botmendel | Administrador |
| Dayho | dayho.com.br/wp-admin/ | botdayho | Administrador |
| Salk Fitness | salkfitness.com.br/wp-admin | botfitness | Administrador |

> **Senhas em:** `docs_user/acessos.txt`
> **WHM root:** 162.240.13.51:2087 | user: root

---

## 3. SITE 1 — MANAGER GRUPO (managergrupo.com.br)

### Propósito
Portal institucional da holding. Funciona como hub de redirecionamento para os sites das empresas do grupo.

### Navegação
- Home | Blog | Quem Somos | Nossas Redes | Painel

### Conteúdo
- **Homepage:** Banners rotativos com promoção de cada empresa do grupo
- **Quem Somos:** Texto institucional genérico — sem missão/visão/valores explícitos
- **Blog:** Página existe mas está **vazia** (sem artigos visíveis)
- **Painel:** Área restrita (Tutor LMS — sistema de cursos/treinamento)

### Features Especiais
- **Tutor LMS + Pro** — Sistema de aprendizado com cursos, certificados, gradebook
- **Restrict Content Pro** — Conteúdo restrito por membership
- **WooCommerce** — Referenciado no código (possível venda de cursos/memberships)

### Avaliação
| Aspecto | Score |
|---------|-------|
| Conteúdo institucional | ⚠️ Raso — falta história, missão, valores, equipe |
| Blog | ❌ Vazio |
| LMS | ✅ Infraestrutura montada (Tutor LMS) |
| SEO | ❌ Sem conteúdo indexável |
| Design | ⚠️ Funcional mas básico |

---

## 4. SITE 2 — SALK MEDICAL (salkmedical.com.br)

> **Overview completo em:** `docs_user/SALK-MEDICAL-OVERVIEW.md`

### Resumo
- **Propósito:** Catálogo comercial B2B de equipamentos médicos
- **33+ produtos** em 6 categorias (Focos, Mesas, Serras, Suportes, Carrinhos)
- **Sala Cirúrgica Inteligente** como diferencial
- **FAQ robusto** (17 perguntas)
- **Área de Downloads** com login obrigatório
- **Blog:** 10+ artigos, **parado desde outubro 2025**

### Stack Diferenciado
- JetEngine para catálogo (filtros avançados)
- Happy Elementor Addons
- WP Download Manager
- GDPR Cookie Consent

---

## 5. SITE 3 — MENDEL MEDICAL (mendelmedical.com.br)

> **Overview prévio na sessão anterior** — site principal do projeto

### Resumo
- **Propósito:** Site institucional + catálogo do fabricante
- **Stack:** WP 6.9.4, Elementor Pro 3.35.5
- **Plugins:** CF7, WPForms (duplicado), Owl Carousel, Responsive Lightbox
- **Chat:** Bitrix24
- **Analytics:** GA (2 IDs)
- **Cache:** W3TC Disk Enhanced
- **DB:** 2 installs WP (prefixos wp_ e wps_)

---

## 6. SITE 4 — DAYHO METALMECÂNICA (dayho.com.br)

### Propósito
Site institucional da unidade de metalurgia/usinagem. Apresenta serviços B2B industriais.

### Navegação
- Home | Soluções | Destaques | Quem Somos | Nossas Redes

### História
- **Fundação:** 1996 — manutenção de equipamentos e usinagem
- **1997:** Primeiro produto médico-hospitalar (autoclaves)
- **2014:** Integração ao Manager Grupo, reformulação de marca
- **Produção:** 1.000+ itens diferentes na carteira

### Serviços (3 páginas dedicadas)

#### Usinagem Convencional
| Equipamento | Especificação |
|-------------|--------------|
| Tornos convencionais | Curso X: Ø330mm, Barra: Ø50mm, Curso Z: 1500mm |
| Fresadoras convencionais | X: 900mm, Y: 400mm, Z: 250mm |
| Brunidora | — |
| Retífica plana | — |

#### Usinagem CNC
| Equipamento | Especificação |
|-------------|--------------|
| Tornos CNC | Curso X: Ø110mm, Barra: Ø31mm |
| Fresadoras CNC | X: 1700mm, Y: 680mm, Z: 600mm |
| Centro de Usinagem | X: 400mm, Y: 300mm, Z: 350mm |
| Software | Autodesk PowerMILL |

#### Serralheria Industrial
| Setor | Equipamentos |
|-------|-------------|
| Furação | Furadeira coluna, bancada, rosqueadeira |
| Corte | Serra fita, serra circular, guilhotina |
| Solda | MIG, TIG, oxiacetilênica |
| Dobra | Dobradeira de tubo |
| Acabamento | Retífica manual, esmerilhadeira, lixadeira |

### Destaques
- **ERP TOTVS Protheus** (desde 2015) — rastreabilidade completa
- **Controle de qualidade** em todas as peças

### Cores de Marca
- Preto: #111111
- Laranja: #F58634 (Pantone 715 C)
- Cinza: #A9ABAE
- Branco: #FFFFFF

### Contato
- Email: contato@dayho.com.br
- Formulário redirecionado para salkmedical.com.br/fale-conosco/

### Avaliação
| Aspecto | Score |
|---------|-------|
| Conteúdo técnico | ✅ Bom — especificações de máquinas, processos detalhados |
| Blog | ❌ Inexistente |
| SEO | ⚠️ Sem detecção de analytics/GTM |
| Design | ✅ Moderno, com hero animado e stats |
| Integração grupo | ⚠️ Formulário redireciona para Salk Medical |

---

## 7. SITE 5 — SALK FITNESS (salkfitness.com.br)

### Propósito
Site de equipamentos fitness para academias. **Claramente em hibernação.**

### Navegação
- Home | Produtos | Blog | Quem Somos | Nossas Redes | Parceiros | Eventos

### Evidências de Hibernação
- **Produtos:** "Logo teremos novidades" (placeholder, sem catálogo)
- **Blog:** 20+ artigos publicados entre out/2016 e fev/2018, **parado há 8 anos**
- **Eventos:** Últimos de 2016 (Felipe Franco workshop, Equipotel SP)
- **WooCommerce** instalado mas sem produtos visíveis
- **Conteúdo institucional** genérico e raso

### Blog (período ativo 2016-2018)
| Tipo de Conteúdo | % |
|-----------------|---|
| Business/Marketing para academias | ~40% |
| Exercícios e equipamentos | ~35% |
| Saúde e bem-estar | ~15% |
| Eventos e patrocínios | ~10% |

### Contato
- Email: contato@salkfitness.com.br
- Formulário redirecionado para salkmedical.com.br/fale-conosco/

### Avaliação
| Aspecto | Score |
|---------|-------|
| Conteúdo | ❌ Desatualizado (2016-2018) |
| Produtos | ❌ Placeholder — sem catálogo real |
| Blog | ❌ Inativo há 8 anos |
| Relevância | ⚠️ Em hibernação — manutenção mínima |
| Risco | ⚠️ WP desatualizado pode ser vetor de ataque no servidor compartilhado |

---

## 8. ANÁLISE CROSS-SITE — OPORTUNIDADES E RISCOS

### Padrões Identificados

**Positivos:**
- Todas no mesmo servidor/endereço — facilita gestão centralizada
- Identidade visual parcialmente consistente (logos do grupo no footer)
- Salk Medical é o site mais completo (catálogo, FAQ, SAC, Downloads)
- Dayho tem bom conteúdo técnico para B2B industrial

**Negativos:**
1. **Blogs mortos em TODOS os sites** — nenhum site tem blog ativo em 2026
2. **Versões de WP inconsistentes** — 6.8.5 e 6.9.4 misturados
3. **Formulários redirecionam para Salk Medical** — Dayho e Salk Fitness não têm formulários próprios
4. **Analytics ausente** em Dayho e Salk Fitness
5. **Salk Fitness é um risco de segurança** — site abandonado com WP no servidor compartilhado
6. **SEO técnico inexistente** — sem Schema.org, sem estratégia de conteúdo
7. **Conteúdo institucional raso** — especialmente Manager Grupo e Salk Fitness
8. **Duplicação de plugins** — CF7 + WPForms em alguns sites
9. **Bitrix24 inconsistente** — presente em Manager e Mendel, ausente em Salk Medical e Dayho

### Matriz de Prioridade

| Site | Prioridade | Ação Recomendada |
|------|-----------|-----------------|
| **Mendel Medical** | 🔴 ALTA | Foco principal do projeto — Brownfield Discovery + redesign |
| **Salk Medical** | 🟡 MÉDIA | Atualização de stack, SEO, blog, Schema.org |
| **Dayho** | 🟢 BAIXA | Analytics, formulário próprio, manutenção |
| **Manager Grupo** | 🟢 BAIXA | Conteúdo institucional, blog, LMS activation |
| **Salk Fitness** | ⚪ MÍNIMA | Avaliar: manter mínimo ou desativar por segurança |

### Riscos de Segurança

| Risco | Severidade | Afeta |
|-------|-----------|-------|
| Sites abandonados no mesmo servidor | ALTA | Todos (servidor compartilhado) |
| WP desatualizado (Salk Fitness) | MÉDIA | Salk Fitness → potencial vetor para todos |
| Sem WAF/ModSecurity verificado | MÉDIA | Todos |
| Plugins duplicados/não utilizados | BAIXA | Mendel, Salk Medical |
| Analytics ausente = sem visibilidade | MÉDIA | Dayho, Salk Fitness |

---

## 9. INVENTÁRIO COMPLETO DE ATIVOS DIGITAIS

### Sites (5)
| # | Domínio | Páginas | Produtos | Blog Posts |
|---|---------|---------|----------|-----------|
| 1 | managergrupo.com.br | ~5 | 0 | 0 |
| 2 | salkmedical.com.br | ~12 | 33+ | 10+ |
| 3 | mendelmedical.com.br | ~8 | ~20 | A verificar |
| 4 | dayho.com.br | ~6 | 0 (serviços) | 0 |
| 5 | salkfitness.com.br | ~8 | 0 (placeholder) | 20+ (inativos) |

### Redes Sociais
| Rede | Salk Medical | Mendel | Manager | Dayho | Fitness |
|------|-------------|--------|---------|-------|---------|
| Facebook | @salkmedical | Sim | @managergrupo | Não detectado | Não detectado |
| Instagram | @salkmedical | Sim | (usa @salkmedical) | Não detectado | Não detectado |
| YouTube | UCUcQrUcbOB0RPX0uVWhOawQ | Sim | Não detectado | Não detectado | Não detectado |

### Sistemas Internos
- **LMS:** Tutor LMS no Manager Grupo (cursos, certificados)
- **CRM:** Bitrix24 (Manager, Mendel)
- **ERP:** TOTVS Protheus (Dayho, desde 2015)
- **Downloads:** WP Download Manager (Salk Medical, login-gated)

### Infraestrutura
- **Servidor:** 162.240.13.51 (HostGator/cPanel, compartilhado)
- **WHM:** Porta 2087, acesso root
- **cPanel:** Porta 2083, 5 usuários (1 por site)
- **SSH:** Bloqueado (porta 22 fechada)
- **wp-cli:** Não disponível
- **Acesso:** cPanel UAPI via Python urllib

---

*Documento gerado automaticamente — Orion (aiox-master) — Projeto Mendel Medical*
