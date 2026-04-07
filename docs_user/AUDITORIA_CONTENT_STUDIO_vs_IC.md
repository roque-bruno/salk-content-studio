# AUDITORIA ESTRATEGICA — Content Studio vs Inteligencia Competitiva

**Projeto:** Content Studio (Producao de Conteudo Social Media)
**Auditado por:** Squad IC — Orion (AIOX Master)
**Data:** 2026-04-07
**Classificacao:** ESTRATEGICO — USO INTERNO
**Fonte cruzada:** 16 fases de IC concluidas, 22 tabelas SQLite, 82+ documentos de pesquisa

---

## VEREDICTO EXECUTIVO

O Content Studio e uma **peca de engenharia impressionante** — sistema completo, compliance nativo, multi-marca, custo marginal proximo de zero. O problema nao e o sistema. O problema e que **a estrategia de conteudo dentro do sistema nao esta calibrada com os dados reais do mercado** que temos.

**Score geral de alinhamento: 62/100** — Sistema excelente, estrategia desalinhada.

| Dimensao | Score | Veredicto |
|----------|:-----:|-----------|
| Compliance/Regulatorio | 95/100 | Excelente — ANVISA, termos proibidos, ETRUS bloqueado `[F: REGRAS-DE-NEGOCIO-COMPLETAS.md §9.2 quality_gate_checks, §9.5 termos_proibidos]` |
| Arquitetura tecnica | 90/100 | Solido — FastAPI, YAML, pipeline ciclico `[F: SOBRE-O-PROJETO.md §2 Stack Tecnologica]` |
| Identidade de marca | 85/100 | Bom — brandbooks bem definidos `[F: REGRAS-DE-NEGOCIO-COMPLETAS.md §1.1-1.4 brandbooks YAML]` |
| Claims e argumentos | 55/100 | **INCOMPLETO** — 42 claims `[F: REGRAS-DE-NEGOCIO-COMPLETAS.md §2 claims_aprovados.yaml]` vs 80+ diferenciais `[F: 04_relatorios/tecnico/DIFERENCIAIS_POSITIVOS_MENDEL.md]` |
| Canais prioritarios | 35/100 | **DESALINHADO** — Instagram first `[F: REGRAS-DE-NEGOCIO-COMPLETAS.md §5 conteudo_strategy.yaml]` vs ICP validado `[F: memory/reference_icp_digital_validado.md §Canais VALIDADOS]` |
| Volume/frequencia | 40/100 | **SUPERESTIMADO** — 48 pcs/sem `[F: SOBRE-O-PROJETO.md §3.2 Metricas]` para 2.452 seguidores `[F: 04_relatorios/pesquisa/BENCHMARK_MENDEL_SALK_DIGITAL.md:32]` |
| Jornada de compra | 30/100 | **CRITICO** — conteudo nao mapeia para as 7 fases `[F: 04_relatorios/pesquisa/JORNADA_COMPRA_HOSPITALAR_BRASIL.md:39-110]` |
| Alocacao de pilares | 50/100 | **AJUSTAR** — COMMAND supervalorizado `[F: memory/feedback_command_nicho.md]`, licitacoes subvalorizado |
| Integracao com CRM | 10/100 | **INEXISTENTE** — sem link Bitrix24 `[F: memory/reference_bitrix24_auditoria_real.md — 0 automacoes]` |
| SEO/Google | 5/100 | **AUSENTE** — Google canal #2 validado `[F: memory/reference_icp_digital_validado.md:42]`, zero estrategia `[F: 04_relatorios/pesquisa/SCORING_PRESENCA_DIGITAL.md — Score SEO]` |

---

## LEGENDA DE FONTES

As referencias `[F: ...]` neste documento apontam para arquivos e secoes especificos do projeto IC:

| Prefixo | Caminho base |
|---------|-------------|
| `REGRAS-DE-NEGOCIO-COMPLETAS.md` | `docs_user/squads/producao-social-midia/REGRAS-DE-NEGOCIO-COMPLETAS.md` |
| `SOBRE-O-PROJETO.md` | `docs_user/squads/producao-social-midia/SOBRE-O-PROJETO.md` |
| `04_relatorios/...` | `C:\Users\CONSULTORIA\Documents\Projeto-Diferenciais\04_relatorios\...` |
| `memory/...` | `C:\Users\CONSULTORIA\.claude\projects\...\memory\...` |
| `DB:tabela` | `06_dados_extraidos/inteligencia_competitiva.db` — tabela SQLite |

---

## PARTE 1 — ISSUES CRITICOS (DEVEM ser corrigidos antes de escalar)

### ISSUE #1 — Canal prioritario INVERTIDO (Severidade: CRITICA)

**O que o Content Studio faz:**
`[F: REGRAS-DE-NEGOCIO-COMPLETAS.md §5 conteudo_strategy.yaml — pillar_weights e platform_specs]`
- Instagram e o canal principal (60-70% Reels, 5x/semana)
- LinkedIn secundario
- YouTube terciario
- WhatsApp apenas como "atomizacao"
- Google/SEO: inexistente

**O que a IC validou (ICP Digital com fontes BR rastreavies):**

| Rank | Canal | Score | Justificativa IC | Fonte IC |
|------|-------|:-----:|------------------|----------|
| 1 | **WhatsApp** | 95 | Canal #1 B2B BR. 70% empresas BR usam para vendas. 82% brasileiros usam WhatsApp com hospitais. Reps usam diariamente | `memory/reference_icp_digital_validado.md:34-38` — E-Commerce Brasil, Tuvis Healthcare |
| 2 | **Google (SEO/SEM)** | 90 | 94% decisores B2B informados antes de contatar fornecedor. 93% pesquisam no Google antes de comprar | `memory/reference_icp_digital_validado.md:18-24` — Think with Google BR, E-Commerce Brasil |
| 3 | **YouTube** | 85 | 47% identificam YouTube + Google como fontes primarias B2B. 93% video importante para confianca | `memory/reference_icp_digital_validado.md:21-22` — Think with Google BR |
| 4 | **LinkedIn** | 80 | 83-85M usuarios BR, 65M tomadores de decisao. Zero ads de concorrentes | `memory/reference_icp_digital_validado.md:15,44` — Exame, PMC |
| 5 | **Email** | 75 | 39.5% open rate B2B. So KSS tem newsletter ativa entre concorrentes | `memory/reference_icp_digital_validado.md:45` |
| 6 | **Instagram** | 45 | Brand awareness generico. NAO gera leads B2B healthcare | `04_relatorios/pesquisa/SCORING_PRESENCA_DIGITAL.md §2.1 — scoring IG max 8pts de 100` |

**Impacto:** O sistema investe 60-70% do esforco no canal que a IC classifica como **6o de 6** para conversao B2B healthcare. Enquanto isso, WhatsApp (#1) e Google (#2) tem **zero** estrategia.

**Recomendacao:**
1. WhatsApp deve ter estrategia propria (nao atomizacao) — sequencias de nurturing, catalogo digital, broadcasts segmentados
2. SEO deve ser pilar estrategico — artigos tecnicos, landing pages por produto, blog com claims rastreáveis
3. YouTube deve subir para canal #2 (demos, specs, comparativos)
4. LinkedIn mantem prioridade (#3)
5. Instagram desce para awareness/branding (#4) — 20-30% do esforco, nao 60-70%

---

### ISSUE #2 — Claims incompletos vs Diferenciais Positivos IC (Severidade: ALTA)

**O que o Content Studio tem:** 42 claims (20 LEV + 10 KRATUS + 3 OSTUS + 3 KRONUS + 2 COMMAND + 3 comparativos + 4 institucionais)
`[F: REGRAS-DE-NEGOCIO-COMPLETAS.md §2 claims_aprovados.yaml — contagem por grupo]`

**O que a IC mapeou:**
`[F: 04_relatorios/tecnico/DIFERENCIAIS_POSITIVOS_MENDEL.md — linhas 10-81]`

Claims AUSENTES do Content Studio que sao argumentos validados:

**KRATUS — 14 diferenciais mapeados, apenas 10 no sistema:**
`[F: 04_relatorios/tecnico/DIFERENCIAIS_POSITIVOS_MENDEL.md:16-29 — tabela TOP Diferenciais KRATUS]`

| Diferencial IC | Status no Content Studio | Impacto Comercial |
|----------------|------------------------|--------------------|
| Potencia 840 VA (2,1x maior que qualquer nacional) `[F: DIFERENCIAIS_POSITIVOS:16]` | **AUSENTE** | CRITICO — argumento imbativel |
| Area livre arco C 2.293 mm (maior do mercado) `[F: DIFERENCIAIS_POSITIVOS:17]` | **AUSENTE** | CRITICO — ortopedistas compram por isso |
| 7 secoes radiotransparentes `[F: DIFERENCIAIS_POSITIVOS:23]` | **AUSENTE** | ALTO — visibilidade radiologica completa |
| Sistema 3 baterias 36V (unico no mercado) `[F: DIFERENCIAIS_POSITIVOS:21]` | **AUSENTE** | ALTO — seguranca em emergencia |
| Carga de teste 1.012 kg (2,2x nominal) `[F: DIFERENCIAIS_POSITIVOS:22]` | **AUSENTE** | MEDIO — margem de seguranca documentada |
| Rodizios auto-travantes com trava centralizada `[F: DIFERENCIAIS_POSITIVOS:24]` | **AUSENTE** | MEDIO — seguranca operacional |
| Estofamento PU antistatico `[F: DIFERENCIAIS_POSITIVOS:25]` | **AUSENTE** | MEDIO — seguranca com eletrocauterio |
| 30+ acessorios compativeis `[F: DIFERENCIAIS_POSITIVOS:27]` | **AUSENTE** | ALTO — portfolio mais completo |

**FOCOS 3LEV/4LEV — diferenciais ausentes:**
`[F: 04_relatorios/tecnico/DIFERENCIAIS_POSITIVOS_MENDEL.md:72-80 — tabela TOP Diferenciais 3LEV/4LEV]`

| Diferencial IC | Status no Content Studio | Impacto |
|----------------|------------------------|---------|
| Camera integrada na manopla (M1LEC, 160K lux) `[F: DIFERENCIAIS_POSITIVOS:74]` | Parcial (LEV-20 generico) | ALTO — exclusivo |
| 4LEV profundidade 1.930 mm (~2x mercado) `[F: DIFERENCIAIS_POSITIVOS:76]` | **AUSENTE** | CRITICO — specs de produto |
| 5 articulacoes (vs 3-4 tipico) `[F: DIFERENCIAIS_POSITIVOS:77]` | **AUSENTE** | ALTO — posicionamento |
| Recarga 2-4,5h vs KSS 12h (6x mais rapido) `[F: DIFERENCIAIS_POSITIVOS:78]` | **AUSENTE** | CRITICO — argumento comparativo |
| Vida util equipamento 10 anos (2x concorrentes) `[F: DIFERENCIAIS_POSITIVOS:79]` | **AUSENTE** | ALTO — TCO |

**Recomendacao:** Expandir banco de claims de 42 para ~65-70, incorporando todos os diferenciais validados pela IC com fonte documental.

---

### ISSUE #3 — Conteudo desconectado da Jornada de Compra Real (Severidade: CRITICA)

**O que a IC mapeou — 7 fases da jornada de compra hospitalar:**
`[F: 04_relatorios/pesquisa/JORNADA_COMPRA_HOSPITALAR_BRASIL.md:39-110 — Fases 1 a 5 detalhadas com fontes acadêmicas (Tese USP, Engeclinic, 1000Medic, Portais Hospitais BR)]`

| Fase | Quem decide | O que busca | Conteudo necessario |
|------|-------------|------------|---------------------|
| 1. Identificacao necessidade `[F: JORNADA:39-51]` | Eng. Clinica + Medicos | Obsolescencia, custo manutencao | Calculadora TCO, comparativo vida util |
| 2. Planejamento `[F: JORNADA:54-73]` | Eng. Clinica + Financeiro | TCO, viabilidade | Whitepaper TCO mesa cirurgica, ROI calculator |
| 3. Especificacao tecnica `[F: JORNADA:75-91]` | Eng. Clinica | Specs detalhadas, normas | Ficha tecnica comparativa, video demo, datasheet PDF |
| 4. Cotacao/Consulta `[F: JORNADA:93-100]` | Compras | Precos, prazos, documentacao | Proposta padrao, docs para licitacao, ANVISA |
| 5. Avaliacao `[F: JORNADA:102-109]` | Comite multidisciplinar | Demonstracao, referencias | Cases de clientes, video instalacao, depoimentos |
| 6. Decisao | Diretoria + Comite | ROI final, compliance | Apresentacao executiva, comparativo final |
| 7. Pos-compra | Eng. Clinica + Usuarios | Treinamento, suporte | Tutoriais, manuais rapidos, contato AT |

**O que o Content Studio produz:**
`[F: REGRAS-DE-NEGOCIO-COMPLETAS.md §5 conteudo_strategy.yaml — pillar_weights por marca]`

| Pilar Salk | % | Fase da jornada atendida | Gap |
|-----------|---|--------------------------|-----|
| Produto em Destaque | 30% | Fase 1 (awareness) | Nao gera acao |
| Educacional Tecnico | 25% | Fase 2-3 (planejamento/spec) | OK mas generico |
| Cases e Social Proof | 20% | Fase 5 (avaliacao) | Bom |
| COMMAND | 15% | Nenhuma especifica | Sobrevalorizado `[F: memory/feedback_command_nicho.md]` |
| Licitacoes e TCO | 10% | Fase 4 (cotacao) | Subvalorizado |

**Fases SEM cobertura (nenhum pilar do Content Studio endereca):**
- **Fase 2 (TCO/ROI):** Zero conteudo de calculadora, whitepaper, comparativo financeiro
- **Fase 3 (Spec tecnica):** Sem datasheets comparativos sistematicos — specs existem na IC `[F: 04_relatorios/tecnico/DIFERENCIAIS_POSITIVOS_MENDEL.md]` mas nao alimentam o sistema
- **Fase 6 (Decisao executiva):** Sem conteudo para diretoria hospitalar
- **Fase 7 (Pos-compra):** Zero — maior gap de todos

**Recomendacao:** Redesenhar pilares para mapear fases da jornada:

| Pilar Proposto | % | Fases | Formato principal |
|---------------|---|-------|-------------------|
| Awareness/Produto | 20% | 1 | Instagram, YouTube Shorts |
| Educacional/Specs | 25% | 2-3 | YouTube Long, LinkedIn PDF, Blog/SEO |
| Prova Social/Cases | 20% | 5 | LinkedIn, Instagram, YouTube |
| TCO/ROI/Licitacao | 20% | 4, 6 | LinkedIn, Email, WhatsApp, PDF |
| Pos-venda/Suporte | 10% | 7 | YouTube, WhatsApp, Email |
| Institucional | 5% | Transversal | LinkedIn, Instagram |

---

### ISSUE #4 — COMMAND supervalorizado (Severidade: ALTA)

**O que o Content Studio faz:** COMMAND = 15% do conteudo Salk (1 post/semana)
`[F: REGRAS-DE-NEGOCIO-COMPLETAS.md §5 conteudo_strategy.yaml — pillar_weights.salk.command = 15%]`

**O que a IC diz:**
`[F: memory/feedback_command_nicho.md]`
- COMMAND e nicho: apenas hospitais universitarios e acreditados
- Vendas em queda (confirmado por Bruno)
- Funcionalidade (controle fora da area esteril) parece atrativa, mas hospitais priorizam otimizacao de salas (mais cirurgias/dia)
- Zero processos publicos de "sala integrada" mapeados no cruzamento triplo `[F: DB:cruzamento_triplo — sem registros "sala integrada"]`
- Gisele pediu para buscar diferenciais positivos, nao nichos `[F: memory/feedback_diretoria_v2_pivotar.md]`

**Recomendacao:** Reduzir COMMAND de 15% para 5% (1 post a cada 2 semanas). Transferir os 10% para TCO/ROI/Licitacao.

---

## PARTE 2 — ISSUES DE MEDIA SEVERIDADE

### ISSUE #5 — Volume de producao superestimado

**Dados de audiencia (posicao competitiva real):**
`[F: 04_relatorios/pesquisa/AUDITORIA_INSTAGRAM_CONCORRENTES.md:12-31 — Tabela Consolidada Perfis Instagram]`
- Salk Instagram: **2.452** seguidores — posicao **#8**/17 no ranking `[F: AUDITORIA_INSTAGRAM:30]`
- Mendel Instagram: **1.133** seguidores — posicao **#12**/17 `[F: AUDITORIA_INSTAGRAM:29]`
- KSS (principal concorrente): **8.177** seguidores com 863 posts `[F: AUDITORIA_INSTAGRAM:14]`
- MACOM (lider digital): **~12.000** seguidores com 2.657 posts `[F: AUDITORIA_INSTAGRAM:22]`

**Dados de contexto operacional:**
- Budget MKT digital atual: **R$0** `[F: memory/project_respostas_diretoria_2026-03-31.md — "investimento digital atual = R$0"]`
- Equipe: 1 gestora + 1 designer (nao dedicadas) `[F: memory/reference_plano_mkt_crm.md — equipe definida]`

**Metas do Content Studio:**
`[F: SOBRE-O-PROJETO.md §3.2 Metricas de Sucesso]`
- MVP: 5 masters + 25-40 derivados/semana = **30-45 pecas/semana**
- Regime: ~48 pecas/semana
- Salk: 5x IG + 5x LinkedIn + 3x YT + 3x FB = **16 posts/semana so para 1 marca**
`[F: REGRAS-DE-NEGOCIO-COMPLETAS.md §4 platform_specs.yaml — posting_frequency por plataforma]`

**Analise comparativa:**
- KSS tem 863 posts `[F: AUDITORIA_INSTAGRAM:14]` em ~10 anos = ~1,6 posts/semana historico
- MACOM (lider) tem 2.657 posts `[F: AUDITORIA_INSTAGRAM:22]` = ~5 posts/semana
- O Content Studio quer fazer **3x mais que o lider do mercado** com audiencia 5x menor
- PRD v1 ja foi cancelado por volume excessivo (227-265/mes) `[F: SOBRE-O-PROJETO.md §1.4 Historico — v1 cancelado]`

**Recomendacao:**
Fase 1 (mes 1-3): 3 masters/semana (Salk only) = ~15-24 derivados = **18-27 total**
Fase 2 (mes 4-6): Adicionar Mendel (2 masters) = ~30-40 total
Fase 3 (mes 7+): Avaliar metricas antes de escalar

---

### ISSUE #6 — Sem estrategia de SEO/Google

**Dados IC que justificam Google como canal #2:**
`[F: memory/reference_icp_digital_validado.md:18-24]`
- 94% decisores B2B ja informados ANTES de contatar fornecedor (Think with Google BR)
- 93% brasileiros pesquisam no Google antes de comprar (E-Commerce Brasil)
- 56% usam buscadores 1x/semana no processo de decisao (Think with Google BR)
- Engenheiros clinicos pesquisam especificacoes tecnicas no Google `[F: 04_relatorios/pesquisa/JORNADA_COMPRA_HOSPITALAR_BRASIL.md:75-91 — Fase 3 Especificacao Tecnica]`

**Presenca SEO atual:**
`[F: 04_relatorios/pesquisa/SCORING_PRESENCA_DIGITAL.md §2.5 — SEO/Web Traffic scoring]`
- Mendel/Salk nao aparecem na pagina 1 para keywords estrategicas
- Score SEO estimado: 0/10 na camada de Alcance Digital

**O Content Studio nao contempla:**
`[F: REGRAS-DE-NEGOCIO-COMPLETAS.md — nenhuma secao de SEO, blog, ou landing pages]`
- Blog/artigos para SEO
- Landing pages por produto com specs
- Schema markup para equipamentos medicos
- Estrategia de backlinks (ABIMO, ANVISA, portais de engenharia clinica)

**Recomendacao:** Adicionar modulo de conteudo SEO — 2 artigos/semana (1 Salk + 1 Mendel) que atomizam para redes. O blog seria fonte-mae para atomizacao, nao o contrario.

---

### ISSUE #7 — Personas corretas, priorizacao incorreta

**O que a IC validou sobre quem inicia a compra:**
`[F: 04_relatorios/pesquisa/JORNADA_COMPRA_HOSPITALAR_BRASIL.md:46-51 — "Fontes que iniciam a demanda (por ordem de frequencia)"]`
1. **Engenharia Clinica** (60%) — identifica obsolescencia e custos
2. **Corpo medico** (25%) — demanda por nova tecnologia
3. **Diretoria** (10%) — expansao estrategica
4. **Compras** (5%) — renovacao vs substituicao

**Comite decisor hospitalar:**
`[F: memory/reference_icp_digital_validado.md:27-33 — PMC/ECRI/Think with Google]`
- Decisao multidisciplinar: 4-6 pessoas
- Engenheiro clinico especifica (tecnico), Diretor CC demanda (clinico), CFO aprova (financeiro), Procurement executa

**O que o Content Studio prioriza:**
`[F: REGRAS-DE-NEGOCIO-COMPLETAS.md §3 buyer_personas.yaml — 4 personas com peso igual]`
- Salk: todas as 4 personas com peso igual
- Pilares nao diferenciam por persona

**Recomendacao:** Engenharia Clinica deve ser persona #1 com ~40% do conteudo direcionado. Compras sobe para persona #2 (30%). Equipe Medica #3 (20%). Administrador #4 (10%).

---

### ISSUE #8 — Battlecards nao alimentam o sistema

**O que a IC tem (acervo completo de materiais de venda):**
`[F: 04_relatorios/vendas/ — 12 arquivos]`
- `BATTLECARD_FOCOS_vs_KSS.md` — argumentos contra principal concorrente (focos)
- `BATTLECARD_FOCOS_vs_MEDLIGHT.md` — argumentos contra Medlight
- `BATTLECARD_KRATUS_vs_BARRFAB.md` — contra novo BF683 TDP
- `BATTLECARD_KRATUS_vs_KSS.md` — contra Vision T
- `BATTLECARD_OSTUS_vs_STRYKER.md` — contra importados
- `BATTLECARD_KRONUS_vs_IMPORTADOS.md` — contra serras importadas
- `PLAYBOOK_OBJECOES_MESAS.md` / `_FOCOS.md` / `_OSTUS.md` / `_KRONUS.md` — respostas para objecoes comuns
- `TREINAMENTO_VENDAS_PORTFOLIO.md` — argumentario completo
- `TREINAMENTO_VENDAS_SALK.md` — treinamento equipe comercial

**O que o Content Studio usa:** Nenhum desses dados `[F: REGRAS-DE-NEGOCIO-COMPLETAS.md §2 claims_aprovados.yaml — 42 claims genericos, sem referencia a battlecards]`. Os claims sao genericos ("menor custo da categoria") sem o contexto competitivo especifico.

**Recomendacao:** Criar pillar content a partir dos battlecards:
- "LEV vs media de mercado: 5 specs que importam" (sem citar concorrentes)
- "Por que Ra=99 muda o resultado cirurgico" (educacional) `[F: DIFERENCIAIS_POSITIVOS:49 — Ra=99]`
- "KRATUS: 840 VA — o que isso significa na pratica" (tecnico) `[F: DIFERENCIAIS_POSITIVOS:16 — 840 VA]`
- "Recarga em 2h vs 12h: o impacto na rotatividade do CC" (comparativo generico) `[F: DIFERENCIAIS_POSITIVOS:78 — 2-4,5h vs 12h]`

---

## PARTE 3 — ISSUES DE BAIXA SEVERIDADE / OPORTUNIDADES

### ISSUE #9 — Datas sazonais incompletas

**O sistema tem 8 datas.**
`[F: REGRAS-DE-NEGOCIO-COMPLETAS.md §7 editorial_calendar.yaml — seasonal_dates]`

Faltam:

| Data | Evento | Relevancia |
|------|--------|-----------|
| Marco | Hospitalar Fair (se aplicavel) | Principal feira do setor |
| 15/05 | Dia do Engenheiro Biomedico | Persona #1 `[F: JORNADA:46-48 — Engenharia Clinica inicia 60% das compras]` |
| Agosto | SOBRACIL (congresso cirurgia) | Awareness medico |
| Outubro | CBEB (congresso eng. biomedica) | Engenharia clinica |
| Nov/Dez | Temporada de orcamento hospitalar | Licitacoes + CAPEX `[F: memory/feedback_prospeccao_vs_licitacao.md — publico=passivo, organizado por ciclos orcamentarios]` |

### ISSUE #10 — Frequencia por plataforma Mendel

**O sistema propoe:** Instagram 4x/semana + LinkedIn 4x/semana + YouTube 2x/semana = 10 posts/semana
`[F: REGRAS-DE-NEGOCIO-COMPLETAS.md §4 platform_specs.yaml — posting_frequency.mendel]`

**Mendel tem 1.133 seguidores** `[F: 04_relatorios/pesquisa/BENCHMARK_MENDEL_SALK_DIGITAL.md:44]`. 10 posts/semana e desproporcional.

**Recomendacao:** Mendel: 2x/semana LinkedIn + 1x/semana YouTube (demo tecnica) + 1x/semana Instagram = 4 total. LinkedIn e o canal primario para Mendel (publico tecnico) `[F: memory/reference_icp_digital_validado.md:44 — LinkedIn validado para decisores B2B]`.

### ISSUE #11 — Atomizacao sem WhatsApp como canal primario

**O mapa de atomizacao trata WhatsApp como derivado** ("whatsapp_broadcast" com max 1000 chars).
`[F: REGRAS-DE-NEGOCIO-COMPLETAS.md §6 atomization_maps.yaml — whatsapp_broadcast como derivado]`

Mas WhatsApp e o canal #1 validado `[F: memory/reference_icp_digital_validado.md:41]`:
- 70% empresas BR usam para vendas `[F: E-Commerce Brasil — citado em reference_icp_digital_validado.md:55]`
- 82% brasileiros usam WhatsApp com hospitais `[F: Tuvis Healthcare — citado em reference_icp_digital_validado.md:59]`
- 47% dos deals Mendel passam por WhatsApp `[F: reference_icp_digital_validado.md:41]`

Deveria ter:
- Sequencias de nurturing por produto (5-7 mensagens)
- Catalogo digital por WhatsApp Business
- Conteudo formatado para encaminhamento (reps encaminham para clientes) `[F: memory/feedback_prospeccao_vs_licitacao.md — PRIVADO=ativo(prospecção), reps sao canal principal]`
- Templates de mensagem para cada fase da jornada `[F: 04_relatorios/pesquisa/JORNADA_COMPRA_HOSPITALAR_BRASIL.md:39-110]`

---

## PARTE 4 — O QUE ESTA BEM (Manter)

| Aspecto | Avaliacao | Detalhes | Fonte |
|---------|-----------|---------|-------|
| Compliance ANVISA | Excelente | Termos proibidos, quality gate, ETRUS bloqueado | `REGRAS-DE-NEGOCIO-COMPLETAS.md §9.2, §9.5` |
| Tecnica NB2 | Excelente | Produto real integrado na cena, nunca wallpaper | `REGRAS-DE-NEGOCIO-COMPLETAS.md §9.1 nb2_image_generation` |
| Regras de logo | Correto | Mendel=tecnico, Salk=comercial | `REGRAS-DE-NEGOCIO-COMPLETAS.md §1.1 salk_brandbook, §1.2 mendel_brandbook` |
| Composicao Canva | Correto | Specs validadas, margens, gradientes | `REGRAS-DE-NEGOCIO-COMPLETAS.md §9.1 design_specs` |
| Bloqueio ETRUS | Correto | Previa 5, sem registro ANVISA | `REGRAS-DE-NEGOCIO-COMPLETAS.md §2 claims — "ETRUS: bloqueado"` |
| COMMAND restrito | Correto | CMD-01 e CMD-02 apenas, sem ETRUS | `REGRAS-DE-NEGOCIO-COMPLETAS.md §2 claims — command group` |
| Persona Clones | Inteligente | Dr. Marcelo, Fernanda, Dra. Ana, Carlos — bom QA | `REGRAS-DE-NEGOCIO-COMPLETAS.md §9.3 copywriter_personas` |
| Pipeline ciclico | Correto | Feedback loop de performance | `SOBRE-O-PROJETO.md §2 Pipeline de Producao` |
| 3 camadas (worker/IA/humano) | Correto | 40/45/15% — equilibrio adequado | `SOBRE-O-PROJETO.md §2 Camadas de Validacao` |
| Custo por peca | Excelente | ~R$1 vs R$500-2000 agencia | `SOBRE-O-PROJETO.md §3.3 Comparativo Custos` |

---

## PARTE 5 — PLANO DE CORRECAO PROPOSTO

### Sprint 1 — Recalibracao Estrategica (Semana 1)

| # | Acao | Responsavel | Impacto | Fonte da decisao |
|---|------|-------------|---------|------------------|
| 1.1 | Expandir banco de claims de 42 → 65-70 com dados IC | @analyst + Content Squad | ALTO | `04_relatorios/tecnico/DIFERENCIAIS_POSITIVOS_MENDEL.md` |
| 1.2 | Redesenhar pilares de conteudo (mapear para jornada de compra) | @po + @analyst | CRITICO | `04_relatorios/pesquisa/JORNADA_COMPRA_HOSPITALAR_BRASIL.md` |
| 1.3 | Reprioritizar canais: WhatsApp > Google > YouTube > LinkedIn > Instagram | @architect + Content Squad | CRITICO | `memory/reference_icp_digital_validado.md` |
| 1.4 | Reduzir COMMAND de 15% → 5% | @po | MEDIO | `memory/feedback_command_nicho.md` |
| 1.5 | Ajustar frequencia: Salk 10/sem, Mendel 4/sem (nao 16+10) | @pm | ALTO | `04_relatorios/pesquisa/AUDITORIA_INSTAGRAM_CONCORRENTES.md` — benchmarks |

### Sprint 2 — Novos Canais (Semanas 2-3)

| # | Acao | Responsavel | Impacto | Fonte da decisao |
|---|------|-------------|---------|------------------|
| 2.1 | Criar estrategia WhatsApp Business (sequencias, catalogo, templates) | @dev + Content Squad | CRITICO | `memory/reference_icp_digital_validado.md:34-41` |
| 2.2 | Criar modulo SEO (blog, landing pages, schema markup) | @dev + @analyst | ALTO | `memory/reference_icp_digital_validado.md:18-24, 42` |
| 2.3 | Integrar battlecards IC como fonte de conteudo | @analyst | ALTO | `04_relatorios/vendas/BATTLECARD_*.md` (6 arquivos) |
| 2.4 | Adicionar conteudo pos-venda (tutoriais, manuais rapidos) | @po + @dev | MEDIO | `JORNADA_COMPRA:Fase 7` — gap total |

### Sprint 3 — Metricas e CRM (Semanas 3-4)

| # | Acao | Responsavel | Impacto | Fonte da decisao |
|---|------|-------------|---------|------------------|
| 3.1 | Integrar Bitrix24 CRM (leads por UTM, tracking) | @dev + @devops | CRITICO | `memory/reference_bitrix24_auditoria_real.md — 8.7% WR, 0 automacoes` |
| 3.2 | Dashboard de metricas por fase da jornada | @dev | ALTO | `JORNADA_COMPRA — 7 fases como framework` |
| 3.3 | Feedback loop com equipe comercial (Amanda/Sabrina/Daniel) | @pm | ALTO | `memory/project_contexto_comercial.md — vendedores ativos` |
| 3.4 | A/B testing de formatos por canal | Content Squad | MEDIO | Diretriz Gisele: quick wins, dados acima de opiniao `[F: memory/feedback_diretoria_v2_pivotar.md]` |

---

## PARTE 6 — REDISTRIBUICAO PROPOSTA DE CANAIS E PILARES

### Canais — Esforco proposto vs atual

| Canal | Atual (%) | Proposto (%) | Justificativa IC | Fonte |
|-------|:---------:|:------------:|------------------|-------|
| Instagram | 60% | 20% | Awareness apenas, nao converte B2B healthcare | `SCORING_PRESENCA_DIGITAL.md §2.1 — IG max 8/100 pts` |
| LinkedIn | 20% | 25% | Decisores B2B, eng. clinica, compras | `reference_icp_digital_validado.md:44 — 65M decisores` |
| YouTube | 10% | 20% | Demos, specs, #3 canal validado | `reference_icp_digital_validado.md:21 — 47% fonte B2B` |
| WhatsApp | 2% | 20% | Canal #1 validado, reps usam diariamente | `reference_icp_digital_validado.md:41 — 47% deals Mendel` |
| Google/SEO | 0% | 10% | Canal #2 validado, engenheiros pesquisam specs | `reference_icp_digital_validado.md:42 — 94% B2B pesquisam` |
| Email | 5% | 5% | Follow-up, documentacao | `reference_icp_digital_validado.md:45 — 39.5% open rate` |
| Facebook | 3% | 0% | Descontinuar — ROI nulo para B2B healthcare | `SCORING_PRESENCA_DIGITAL.md — sem evidencia conversao B2B` |

### Pilares Salk — Proposta recalibrada

| Pilar | Atual | Proposto | Fase Jornada | Fonte da recalibracao |
|-------|:-----:|:--------:|:------------:|----------------------|
| Awareness/Produto | 30% | 20% | 1 | `JORNADA_COMPRA:39-51 — Fase 1` |
| Educacional/Specs | 25% | 25% | 2-3 | `JORNADA_COMPRA:54-91 — Fases 2-3` |
| Cases/Social Proof | 20% | 20% | 5 | `JORNADA_COMPRA:102-109 — Fase 5` |
| COMMAND/Sala Integrada | 15% | 5% | Nicho | `memory/feedback_command_nicho.md` |
| TCO/ROI/Licitacao | 10% | 20% | 4, 6 | `JORNADA_COMPRA:93-100 — Fase 4` + `feedback_prospeccao_vs_licitacao.md` |
| Pos-venda/Suporte | 0% | 10% | 7 | `JORNADA_COMPRA — Fase 7 sem cobertura` |

---

## RESUMO DE PRIORIDADES

| Prioridade | Issue | Acao-chave | Fonte primaria |
|:----------:|-------|-----------|----------------|
| P0 | Canal prioritario invertido | Redesenhar mix: WhatsApp/Google/YouTube acima do Instagram | `reference_icp_digital_validado.md` |
| P0 | Jornada de compra desconectada | Mapear pilares para 7 fases reais | `JORNADA_COMPRA_HOSPITALAR_BRASIL.md` |
| P1 | Claims incompletos | Expandir banco com diferenciais IC | `DIFERENCIAIS_POSITIVOS_MENDEL.md` |
| P1 | CRM inexistente | Integrar Bitrix24 | `reference_bitrix24_auditoria_real.md` |
| P2 | COMMAND supervalorizado | Reduzir de 15% → 5% | `feedback_command_nicho.md` |
| P2 | Volume superestimado | Comecar com 18-27 pecas/semana, nao 48 | `AUDITORIA_INSTAGRAM_CONCORRENTES.md` |
| P2 | SEO ausente | Criar modulo blog/landing pages | `reference_icp_digital_validado.md:42` |
| P3 | Battlecards nao integrados | Alimentar pillar content com dados IC | `04_relatorios/vendas/BATTLECARD_*.md` |
| P3 | WhatsApp como canal primario | Estrategia propria, nao atomizacao | `reference_icp_digital_validado.md:34-41` |

---

> **NOTA FINAL:** O Content Studio e uma arma poderosa. O problema nao e a arma — e a mira. Com os ajustes propostos, o sistema passa de "fabrica de conteudo para Instagram" para "maquina de geracao de demanda B2B alinhada com a jornada real de compra hospitalar". A diferenca entre postar e vender.

---

*Auditoria realizada por Squad IC — Orion (AIOX Master)*
*Todas as afirmacoes possuem fonte rastreavel [F: arquivo:secao/linha]*
*Co-Authored-By: Claude Opus 4.6*
