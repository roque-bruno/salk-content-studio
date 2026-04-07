# Regras de Negocio Completas — Content Studio Manager Grupo

> **Documento gerado em:** 2026-04-07
> **Fonte:** 18 arquivos YAML em `squads/content-production/data/`
> **Uso:** Referencia unica de TODAS as variaveis estrategicas, regras, argumentos e configuracoes do sistema de producao de conteudo.

---

## Indice

1. [Brandbooks (4 Marcas)](#1-brandbooks)
2. [Diretrizes de Logo e Regras Visuais Globais](#2-diretrizes-de-logo-e-regras-visuais-globais)
3. [Buyer Personas](#3-buyer-personas)
4. [Claims Aprovados (Banco de Argumentos)](#4-claims-aprovados)
5. [Termos Proibidos (Compliance)](#5-termos-proibidos)
6. [Banco de Hashtags](#6-banco-de-hashtags)
7. [Specs de Plataforma](#7-specs-de-plataforma)
8. [Calendario Editorial](#8-calendario-editorial)
9. [UTM Patterns](#9-utm-patterns)
10. [Copywriters por Marca](#10-copywriters-por-marca)
11. [Geracao de Imagem (NB2)](#11-geracao-de-imagem-nb2)
12. [Estrategia de Conteudo](#12-estrategia-de-conteudo)
13. [Atomizacao](#13-atomizacao)
14. [Quality Gate (Disaster Check)](#14-quality-gate)
15. [Briefing Atlas](#15-briefing-atlas)

---

## 1. Brandbooks

### 1.1 Salk Medical (Prioridade 1 — Comercial/Vendas)

| Campo | Valor |
|-------|-------|
| **Nome** | Salk Medical |
| **Foco** | Comercial / Vendas |
| **Tagline** | Sala Cirurgica Inteligente |
| **Site** | salkmedical.com.br |

**Tom de Voz:**
- **Primario:** Consultivo, confiante, orientado a resultados
- **Adjetivos:** Eficiente, Confiavel, Acessivel, Inovador
- **Proibido:** Agressivo, Vendedor, Arrogante, Superficial
- **CTA Style:** Consultivo — "Saiba mais", "Converse com um especialista", "Solicite uma demonstracao"
- **Nivel linguistico:** Profissional mas acessivel — gestores hospitalares entendem sem ser engenheiros

**Paleta de Cores:**
| Cor | HEX |
|-----|-----|
| Primary | #003366 |
| Secondary | #0066CC |
| Accent | #FFFFFF |
| Background Dark | #001a33 |
| Success | #34d399 |
| Warning | #f59e0b |

**Logo:**
- Posicao: Canto superior direito ou inferior esquerdo
- Largura: 180-200px
- Clear space: Minimo 20px
- **Regra:** Usar em conteudo COMERCIAL — vendas, preco, atendimento, cases, licitacoes
- **Nunca com:** Conteudo tecnico puro (usar Mendel)

**Pilares de Conteudo:**
| Pilar | % | Descricao |
|-------|---|-----------|
| Produto em Destaque | 30% | Specs, demos, diferenciais de LEV, KRATUS, OSTUS, KRONUS, COMMAND |
| Educacional Tecnico | 25% | FAQ, tendencias em CC, guias de compra |
| Cases e Social Proof | 20% | Instalacoes, depoimentos, numeros, logos de clientes |
| Sala Cirurgica Inteligente | 15% | Conceito COMMAND, integracao, futuro do CC |
| Licitacoes e TCO | 10% | Processo de compra, compliance, custo-beneficio |

**Personas-alvo:**
| Persona | Papel | Preocupacoes |
|---------|-------|-------------|
| Engenheiro Clinico | Decisor tecnico | Certificacoes, Compatibilidade, Manutencao, ANVISA |
| Gestor de Compras | Decisor financeiro | TCO, Licitacao, Prazo, Garantia |
| Equipe Medica | Usuario final | Usabilidade, Seguranca, Conforto, Integrado |
| Administrador Hospitalar | Decisor estrategico | ROI, Eficiencia, Modernizacao, Imagem |

**Produtos:**
| Produto | Tipo | Status | Regras Especiais |
|---------|------|--------|-----------------|
| LEV | Foco Cirurgico LED | ATIVO | Luz focada para baixo, Nunca dispersao lateral, Dramatic studio = melhor tecnica |
| KRATUS | Mesa Cirurgica | ATIVO | — |
| OSTUS | Mesa Ortopedica | ATIVO | — |
| KRONUS | Coluna de Distribuicao | ATIVO | — |
| COMMAND | Sistema Integrado CC | ATIVO | Verificar independencia do ETRUS |
| ETRUS | A definir | **BLOQUEADO** | **PROIBIDO publicar, NAO lancado** |

**Regras Visuais (Salk):**
- NB2: Produto integrado na cena. NUNCA wallpaper + colagem.
- NB2 Prompt: Descrever APENAS cenario, NUNCA o produto.
- NB2 Concorrente: NUNCA equipamento medico concorrente. Negative prompt obrigatorio.
- LEV Luz: FOCADA para baixo, NUNCA dispersa/lateral. Sem glow, rays, spreading.
- Pessoas: NUNCA geradas por IA.
- Clinico: NUNCA cenas clinicas geradas por IA.
- Texto/Logo: NUNCA via IA. Adicionar no Canva.
- Fidelidade: Cores e aparencia DEVEM corresponder ao produto real.
- Certificacoes: Exibir apenas validas e atuais.
- ANVISA badge: Obrigatorio em toda peca — 12-14pt, branco 50% opacidade.

**Composicao Canva:**
| Elemento | Especificacao |
|----------|--------------|
| Margens | 60px (5.5% da largura) |
| Headline | 36pt bold, alinhado a esquerda, topo |
| Spec line | 18-20pt light, branco 70% opacidade, tracking +80-100, centralizado rodape |
| ANVISA | 12-14pt, branco 50% opacidade, canto inferior direito |
| Gradientes | Preto→transparente: topo 40-60%, rodape 50-70% |
| Zona protegida | NUNCA texto sobre produto ou reflexo |

**Redes Sociais:** LinkedIn: salkmedical | Instagram: @salkmedical | Facebook: salkmedical | YouTube: @salkmedical

**Termos Proibidos (Salk):** ETRUS, o melhor, o unico, garante, cura, 100% seguro, infalivel, sem riscos

---

### 1.2 Mendel Medical (Prioridade 2 — Autoridade/Fabricante)

| Campo | Valor |
|-------|-------|
| **Nome** | Mendel Medical |
| **Foco** | Autoridade / Fabricante |
| **Tagline** | Fabricante Nacional de Equipamentos Medicos |
| **Site** | mendelmedical.com.br |
| **CNPJ** | 20.102.553/0001-62 |

**Tom de Voz:**
- **Primario:** Tecnico, preciso, autoritativo
- **Adjetivos:** Rigoroso, Inovador, Certificado, Seguro
- **Proibido:** Informal, Superficial, Vendedor, Hype
- **CTA Style:** Tecnico — "Consulte a ficha tecnica", "Veja os dados completos", "Acesse a documentacao"
- **Nivel linguistico:** Tecnico/engenharia — engenheiros clinicos e equipes tecnicas

**Paleta de Cores:**
| Cor | HEX |
|-----|-----|
| Primary | #1A1A2E |
| Secondary | #16213E |
| Accent | #FFFFFF |
| Background Dark | #0f0f1a |

**Logo:**
- Posicao: Canto superior direito
- Largura: 180-200px
- **Regra:** Usar em conteudo TECNICO — specs, fabricacao, engenharia, Ra/R9, normas, bastidores
- **Decisao:** Se tem numero tecnico (Ra, kg, mm, horas, lux) → Mendel

**Pilares de Conteudo:**
| Pilar | % | Descricao |
|-------|---|-----------|
| Bastidores da Fabrica | 35% | Processo de fabricacao, CNC, montagem, testes, qualidade |
| Engenharia e Inovacao | 30% | Desenvolvimento LEV, P&D, normas tecnicas, certificacoes |
| Dados Tecnicos Oficiais | 20% | Specs detalhadas com fonte ANVISA, comparativos com mercado |
| Time de Engenharia | 15% | Perfis, dia a dia, laboratorio, eventos tecnicos |

**Personas-alvo:**
| Persona | Papel | Preocupacoes |
|---------|-------|-------------|
| Engenheiro Clinico | Avaliador tecnico | Normas, Specs, Certificacoes, Comparativos |
| Engenheiro Biomedico | Especificador | ANVISA, ISO, Compatibilidade, Manutencao preditiva |

**Regras Visuais (Mendel):**
- NB2: Produto integrado na cena. Enfase em detalhes tecnicos.
- Cenarios: Laboratoriais, industriais, sala limpa. NUNCA clinicos com IA.
- Pessoas: NUNCA geradas por IA.
- Texto/Logo: NUNCA via IA.
- Certificacoes: Destaque ANVISA + ISO em toda peca.

**Redes Sociais:** LinkedIn: mendelmedical | Instagram: @mendelmedical | Facebook: mendelmedical | YouTube: @mendelmedical

---

### 1.3 Manager Grupo (Prioridade 3 — Institucional)

| Campo | Valor |
|-------|-------|
| **Nome** | Manager Grupo |
| **Foco** | Institucional / Employer Branding |
| **Tagline** | Integrando Solucoes |
| **Site** | managergrupo.com.br |

**Tom de Voz:**
- **Primario:** Acolhedor, institucional, inspirador
- **Adjetivos:** Integrado, Humano, Colaborativo, Inovador
- **Proibido:** Corporativo frio, Generico, Tecnico demais
- **CTA Style:** Institucional — "Conheca nosso time", "Faca parte", "Saiba mais sobre o grupo"

**Pilares de Conteudo:**
| Pilar | % | Descricao |
|-------|---|-----------|
| Cultura Organizacional | 40% | Valores, missao, dia a dia, equipe |
| Carreiras e Employer Branding | 35% | Vagas, depoimentos de colaboradores, beneficios |
| O Grupo | 25% | Apresentacao das empresas, cadeia de valor, eventos |

**Personas-alvo:**
| Persona | Papel | Preocupacoes |
|---------|-------|-------------|
| Candidato | Potencial colaborador | Cultura, Beneficios, Crescimento, Proposito |
| Stakeholder | Parceiro/fornecedor | Solidez, Valores, Portfolio, Reputacao |

**Regras Visuais:** Fotos REAIS da equipe e ambiente de trabalho. NUNCA pessoas geradas por IA. Estilo acolhedor, cores quentes, foco em pessoas reais.

**Redes Sociais:** LinkedIn: managergrupo | Instagram: @managergrupo | Facebook: managergrupo

---

### 1.4 Dayho (Prioridade 4 — Autoridade Industrial)

| Campo | Valor |
|-------|-------|
| **Nome** | Dayho |
| **Foco** | Autoridade Industrial |
| **Tagline** | Metalurgia de Precisao desde 1996 |
| **Site** | dayho.com.br |

**Tom de Voz:**
- **Primario:** Industrial, tecnico, solido
- **Adjetivos:** Preciso, Robusto, Experiente, Confiavel
- **Proibido:** Marketing puro, Superficial, Hype
- **CTA Style:** Industrial — "Solicite um orcamento", "Consulte nosso catalogo", "Fale com engenharia"

**Pilares de Conteudo:**
| Pilar | % | Descricao |
|-------|---|-----------|
| Capacidade Fabril | 60% | CNC, processos de usinagem, maquinario, ERP TOTVS |
| Precisao e Qualidade | 40% | Close-ups de pecas, controle de qualidade, rastreabilidade |

**Personas-alvo:**
| Persona | Papel | Preocupacoes |
|---------|-------|-------------|
| Comprador Industrial | Decisor de compra | Prazo, Qualidade, Volume, Preco |
| Engenheiro de Producao | Especificador tecnico | Tolerancias, Materiais, Acabamento, Rastreabilidade |

**Regras Visuais:** Fotos REAIS de maquinas CNC, pecas usinadas, ambiente fabril. Close-ups de precisao. Pode usar NB2 para renders de pecas em ambientes industriais.

**Redes Sociais:** LinkedIn: dayho | Instagram: @dayho

---

## 2. Diretrizes de Logo e Regras Visuais Globais

### Regra de Logo por Tipo de Conteudo (definida pela diretora — 2026-03-17)

| Marca | Quando Usar | Pilares | Regra |
|-------|------------|---------|-------|
| **Mendel** | Conteudo tecnico, specs, fabricacao, engenharia, Ra/R9, normas, bastidores | Bastidores da Fabrica, Engenharia e Inovacao, Dados Tecnicos Oficiais, Educacional Tecnico | Se tem numero tecnico → Mendel |
| **Salk** | Conteudo comercial, vendas, preco, atendimento, cases, licitacoes | Produto em Destaque, Cases e Social Proof, Licitacoes e TCO, Sala Cirurgica Inteligente | Se tem CTA de venda → Salk |

### Regras Visuais Globais

| Regra | Descricao |
|-------|-----------|
| Imagens de produto | SEMPRE foto real (PNG uploadado). IA renderiza produto INTEGRADO na cena. |
| Pessoas IA | NUNCA pessoas geradas por IA |
| Cenas clinicas IA | NUNCA cenas clinicas com IA |
| Aparencia do produto | Cores e aparencia DEVEM corresponder ao real |
| Certificacoes | Exibir apenas validas e atuais |
| Emojis de saude | NAO banalizar saude (caveiras, seringas, rostos doentes) |
| NB2 wallpaper | NUNCA gerar wallpaper + colar PNG (PROIBIDO). NB2 = produto integrado. |
| NB2 concorrente | NUNCA equipamento medico concorrente. Negative prompt obrigatorio. |
| LEV luz | FOCADA para baixo, NUNCA dispersa/lateral. Sem glow, rays, spreading. |
| Texto/logo IA | NUNCA gerar texto ou logo via IA. Adicionar no Canva. |

### Composicao Canva (validada 2026-03-18)

| Elemento | Especificacao |
|----------|--------------|
| Margens | 60px (5.5% da largura) |
| Logo | 180-200px largura |
| Headline | 36pt bold, alinhado esquerda, topo |
| Spec line | 18-20pt light, branco 70% opacidade, tracking +80-100, centralizado rodape |
| ANVISA badge | 12-14pt, branco 50% opacidade, canto inferior direito |
| Gradientes | Preto→transparente: topo 40-60%, rodape 50-70% |
| Zona protegida | NUNCA texto sobre produto ou reflexo |

---

## 3. Buyer Personas

### 3.1 Compras/Suprimentos

| Campo | Valor |
|-------|-------|
| **Titulo** | Gerente/Analista de Compras/Suprimentos |
| **Tambem conhecido como** | Setor de Compras, Comissao de Licitacao, Pregoeiro |
| **Papel na decisao** | Decisor financeiro / Gate de aprovacao |
| **Estagio do funil** | Meio-Fundo (Avaliacao → Decisao) |
| **Tom** | Direto, objetivo, focado em numeros e compliance |

**Keywords:** TCO, custo-beneficio, registro ANVISA, pregao eletronico, garantia, assistencia tecnica, pronta entrega, menor preco, termo de referencia

**Dores:**
- Fornecedores sem documentacao completa para licitacao
- Precos altos de equipamentos importados
- Dependencia de importacao para manutencao
- Prazos longos de entrega

**Copy exemplo:** "A KRATUS atende integralmente as especificacoes do Termo de Referencia. Registro ANVISA vigente. Menor custo de aquisicao da categoria."

**Melhores claims:** KR-08, KR-09, CMP-02, LEV-12
**Melhores plataformas:** LinkedIn, Email
**Melhores CTAs:** "Receba a documentacao completa para licitacao", "Solicite cotacao para pregao", "Solicite uma proposta personalizada"

### 3.2 Engenharia Clinica

| Campo | Valor |
|-------|-------|
| **Titulo** | Engenheiro(a) Clinico(a) |
| **Tambem conhecido como** | Engenharia Biomedica, Departamento de Eng. Clinica |
| **Papel na decisao** | Influenciador tecnico / Especificador |
| **Estagio do funil** | Topo-Meio (Awareness → Consideracao) |
| **Tom** | Altamente tecnico, preciso, detalhista |

**Keywords:** Ra/R9, NBR IEC 60601, vida util LEDs, intervalo de manutencao, pecas de reposicao, compatibilidade, diluicao de sombra, iluminancia, specs tecnicas

**Dores:**
- Falta de dados tecnicos detalhados de fabricantes nacionais
- Dificuldade de comparar specs entre produtos
- Preocupacao com vida util e manutencao
- Normas tecnicas desatualizadas nos catalogos

**Copy exemplo:** "LEV: Ra/R9=99. LED >300.000h. Conforme NBR IEC 60601-2-41. Sistema COMMAND com integracao ao campo esteril."

**Melhores claims:** LEV-01, LEV-04, LEV-06, LEV-07, LEV-10
**Melhores plataformas:** LinkedIn, YouTube Long, Email
**Melhores CTAs:** "Solicite a ficha tecnica completa", "Compare especificacoes: LEV vs media de mercado", "Agende uma demonstracao tecnica gratuita"

### 3.3 Equipe Medica / Cirurgioes

| Campo | Valor |
|-------|-------|
| **Titulo** | Cirurgiao(a) / Equipe Medica |
| **Tambem conhecido como** | Corpo Clinico, Equipe Cirurgica |
| **Papel na decisao** | Influenciador de uso / Usuario final |
| **Estagio do funil** | Topo (Awareness) |
| **Tom** | Profissional, centrado na experiencia de uso |

**Keywords:** fidelidade cromatica, ergonomia, fadiga visual, campo esteril, posicionamento preciso, conforto cirurgico, visibilidade

**Dores:**
- Fadiga visual em cirurgias longas
- Dificuldade de distincao de tecidos com iluminacao ruim
- Falta de controle de luz sem sair do campo esteril
- Sombras no campo operatorio

**Copy exemplo:** "Iluminacao que reproduz fielmente a cor dos tecidos. Controle de intensidade sem sair do campo esteril."

**Melhores claims:** LEV-01, LEV-02, LEV-06, LEV-08
**Melhores plataformas:** Instagram Reels, YouTube Shorts, LinkedIn
**Melhores CTAs:** "Assista a demonstracao completa", "Salve este post para consultar depois", "Envie para seu engenheiro clinico"

### 3.4 Administradores Hospitalares

| Campo | Valor |
|-------|-------|
| **Titulo** | Diretor(a) / Administrador(a) Hospitalar |
| **Tambem conhecido como** | Superintendencia, Gestao Hospitalar, Diretoria Administrativa |
| **Papel na decisao** | Decisor estrategico / Aprovador final |
| **Estagio do funil** | Meio-Fundo (Consideracao → Decisao) |
| **Tom** | Estrategico, orientado a ROI e gestao |

**Keywords:** ROI, reducao de custos, conformidade regulatoria, capacidade de atendimento, fabricacao nacional, investimento, eficiencia operacional

**Dores:**
- Pressao por reducao de custos
- Necessidade de compliance regulatorio
- Dependencia de importacao
- Dificuldade de justificar investimento em CC

**Copy exemplo:** "Investimento que se paga em X meses. Menor custo total de propriedade. Assistencia tecnica sem depender de importacao."

**Melhores claims:** CMP-02, KR-09, LEV-11, INST-01
**Melhores plataformas:** LinkedIn, Email
**Melhores CTAs:** "Solicite uma proposta personalizada", "Fale com um consultor tecnico", "Baixe o guia: Como especificar focos cirurgicos"

---

## 4. Claims Aprovados

> **REGRA:** Todo conteudo tecnico DEVE usar EXCLUSIVAMENTE claims deste banco. Nenhum claim pode ser inventado.

### Regras de Publicacao

| Produto | Status | Condicao |
|---------|--------|----------|
| LEV, KRATUS, OSTUS, KRONUS | Publicavel | — |
| ETRUS | **BLOQUEADO** | NAO lancado — PROIBIDO publicar |
| COMMAND | Restrito | Usar SOMENTE CMD-01 e CMD-02. NAO associar ao ETRUS |

### 4.1 Focos Cirurgicos — Linha LEV (20 claims)

| ID | Claim | Versao Acessivel | Fonte |
|----|-------|-------------------|-------|
| LEV-01 | Indice de Reproducao de Cor Ra 99 (linha LEV) | A luz mais proxima da realidade | Manual MM013-090070-R04 |
| LEV-02 | R9 ate 97 na cupula 4LEV — fidelidade na faixa do vermelho saturado | Precisao onde mais importa: na distincao de tecidos | Manual MM013-090070-R04 |
| LEV-03 | Iluminancia central maxima de ate 160.000 lux | Iluminacao cirurgica de alta intensidade | Manual MM013-090070-R04 |
| LEV-04 | Temperatura de cor ajustavel de 3.000 a 6.500K em 9 niveis | Luz personalizada para cada procedimento | Manual MM013-090070-R04 |
| LEV-05 | Protecao IP54 nas cupulas LEV | Vedado contra poeira e agua | Manual MM013-090070-R04 |
| LEV-06 | Cupulas LEV sem ventiladores — sem risco de contaminacao por ventilacao forcada | Higiene maxima no ambiente cirurgico | Manual MM013-090070-R04 |
| LEV-07 | LEDs com vida util superior a 226.000 horas | Mais de 25 anos de iluminacao em uso tipico | Manual MM013-090070-R04 |
| LEV-08 | Ate 8 horas de autonomia em emergencia (cupula 3LEV) | Seguranca mesmo sem energia | Manual MM013-090070-R04 |
| LEV-09 | Campo de luz ajustavel de 150 a 360mm | Foco preciso para cada tipo de procedimento | Manual MM013-090070-R04 |
| LEV-10 | Sistema ENDO disponivel nos modelos LE e LEV | Iluminacao especializada para endoscopia | Manual MM013-090070-R04 |
| LEV-11 | Dimmer de 20% a 100% para ajuste fino de intensidade | Controle preciso da intensidade luminosa | Manual MM013-090070-R04 |
| LEV-12 | Fabricado no Brasil pela Mendel Medical com registro ANVISA 81205910005 | Tecnologia nacional certificada | Registro ANVISA |
| LEV-13 | Conforme NBR IEC 60601-2-41 | Conformidade com norma internacional de seguranca | Manual MM013-090070-R04 |
| LEV-14 | Compativel com Sistema COMMAND para controle integrado de sala cirurgica | Controle total sem sair do campo esteril | Manual MM013-090070-R04 |
| LEV-15 | Manopla destacavel e autoclavavel em todos os modelos | Esterilizacao facil e segura | Manual MM013-090070-R04 |
| LEV-16 | Design aerodinamico compativel com fluxo laminar | Integracao com sistema de ventilacao da sala | Manual MM013-090070-R04 |
| LEV-17 | Configuracoes Simplex, Duplex e Triplex para montagem em teto | Configuracao sob medida para cada sala cirurgica | Manual MM013-090070-R04 |
| LEV-18 | Potencia de apenas 64W na cupula 4LEV para 160.000 lux | Eficiencia energetica superior | Manual MM013-090070-R04 |
| LEV-19 | Diluicao de sombra: ate 40% com 2 mascaras (cupula 4LEV) | Visao sem obstaculos durante o procedimento | Manual MM013-090070-R04 |
| LEV-20 | Camera integrada opcional (modelo M1LEC) | Registro visual do procedimento | Manual MM013-090070-R04 |

**Notas tecnicas detalhadas:**
- LEV-01: 3LEV Ra=99 R9=91. 4LEV Ra=99 R9=97. Linha LE Ra/R9=97
- LEV-03: 1L=60klx, 3LE=130klx, 3LEV=148klx, 4LE/4LEV/M1LE/M1LEC=160klx
- LEV-08: 3LEV=8h, 4LEV=6h, 1L=4:30h, 3LE=4h, 4LE=3h, M1LE/M1LEC=2h
- LEV-18: 3LEV=56,4W para 148klx, 4LEV=64W para 160klx
- LEV-19: 3LEV 1 mascara=15%, 2 mascaras=34%. 4LEV 1 mascara=14%, 2 mascaras=40%

### 4.2 KRATUS — Mesa Cirurgica (10 claims)

| ID | Claim | Versao Acessivel |
|----|-------|-------------------|
| KR-01 | Capacidade de carga de trabalho de 460 kg | Para todos os pacientes, sem limitacao |
| KR-02 | Carga de teste de 1.012 kg | Engenharia que inspira confianca |
| KR-03 | Versao bariatrica dedicada | Para todos os pacientes, sem importacao |
| KR-04 | Conforme Portaria 492/2007 para bariatrica | Certificada para cirurgias bariatricas |
| KR-05 | Sistema eletro-hidraulico de movimentacao | Movimentacao suave e precisa |
| KR-06 | Bateria com 7 dias de autonomia (3x12V/9Ah VRLA) | Autonomia que nao falha |
| KR-07 | Vida util do equipamento: 10 anos | Investimento de longa duracao |
| KR-08 | Registro ANVISA vigente n. 81205910007 | Certificacao nacional completa |
| KR-09 | Fabricacao nacional com assistencia tecnica propria | Suporte no seu fuso horario |
| KR-10 | Compativel com todas as especialidades cirurgicas | Versatilidade para qualquer procedimento |

### 4.3 OSTUS — Serra Cirurgica (3 claims)

| ID | Claim | Versao Acessivel |
|----|-------|-------------------|
| OS-01 | Kit completo: motor + 3 cabecotes + pedal | Tudo o que voce precisa em um kit |
| OS-02 | Versatilidade: sagital, reciprocante e perfurador | Tres funcoes em um equipamento |
| OS-03 | Fabricacao nacional | Tecnologia brasileira |

### 4.4 KRONUS — Suporte para Equipamentos (3 claims)

| ID | Claim | Versao Acessivel |
|----|-------|-------------------|
| KN-01 | 10+ configuracoes disponiveis (mono, bi, torre) | Configuracao personalizada |
| KN-02 | Kits especificos: UTI, RPA, Anestesia, Video HDMI | Solucoes dedicadas por especialidade |
| KN-03 | Fabricacao nacional com assistencia tecnica propria | Suporte rapido e acessivel |

### 4.5 COMMAND — Sistema Integrado (2 claims — RESTRITOS)

| ID | Claim | Status | Restricao |
|----|-------|--------|-----------|
| CMD-01 | Sistema de sala cirurgica integrada com controle centralizado | RESTRITO | NAO associar ao ETRUS |
| CMD-02 | IHM touch screen para controle de funcoes dos focos cirurgicos LEV | RESTRITO | NAO associar ao ETRUS |

### 4.6 Claims Comparativos (3 claims)

| ID | Claim | Restricao |
|----|-------|-----------|
| CMP-01 | Foco cirurgico LEV com Ra=99 e R9 ate 97 vs media de mercado Ra=85-92 | Incluir nota: *Baseado em dados publicos |
| CMP-02 | Menor custo de aquisicao na categoria EH (R$48.313 vs R$52.378-66.950) | NAO citar concorrentes por nome |
| CMP-03 | Unico fabricante nacional com mesa bariatrica dedicada | Verificar periodicamente |

### 4.7 Claims Institucionais (4 claims)

| ID | Claim |
|----|-------|
| INST-01 | Cadeia de valor verticalizada: fabricacao → montagem → comercializacao |
| INST-02 | Sede em Sao Jose dos Pinhais/PR — todas as empresas no mesmo endereco |
| INST-03 | Dayho existe desde 1996 — mais de 29 anos de experiencia |
| INST-04 | Grupo fundado em 2014 |

---

## 5. Termos Proibidos

> **Severidade:** BLOCKING — conteudo com esses termos e automaticamente reprovado.
> **Referencias legais:** RDC 96/2008, RDC 751/2022, RDC 848/2024, CFM Res. 2.336/2023

### 5.1 Produtos Bloqueados (CRITICAL)

| Termo | Razao | Alternativa |
|-------|-------|-------------|
| ETRUS | Produto NAO lancado — PROIBIDO | Usar LEV |
| foco cirurgico ETRUS | Produto NAO lancado | Foco cirurgico LEV |
| linha ETRUS | Produto NAO lancado | Linha LEV |
| novo foco cirurgico | Pode referir ao ETRUS | Foco cirurgico LEV |
| lancamento | Pode ser associado ao ETRUS | Evitar ou usar apenas para produtos ja publicados |

### 5.2 Superlativos e Absolutos (CRITICAL)

| Termo | Razao | Alternativa |
|-------|-------|-------------|
| o melhor | Sem evidencia comparativa | Referencia em qualidade de iluminacao cirurgica |
| o unico | Exclusividade dificil de sustentar | Um dos poucos fabricantes nacionais com... |
| o mais moderno | Subjetivo e nao mensuravel | Com tecnologia de ultima geracao |
| revolucionario | Hiperbole sem sustentacao | Inovador ou com avanco significativo |
| incomparavel | Superlativo absoluto | Com diferenciais significativos |
| perfeito | Absoluto impossivel | De alta precisao |
| infalivel | Nenhum equipamento e infalivel | Com alto indice de confiabilidade |

### 5.3 Promessas e Garantias (CRITICAL)

| Termo | Razao | Alternativa |
|-------|-------|-------------|
| garante melhores resultados | Nao se pode garantir resultado clinico | Projetado para oferecer condicoes ideais |
| elimina riscos | Impossivel | Contribui para a reducao de riscos |
| cura | Equipamento nao cura | Auxilia no procedimento |
| 100% seguro | Seguranca absoluta impossivel | Conforme normas de seguranca vigentes |

### 5.4 Comparativos Diretos (HIGH)

| Termo | Razao | Alternativa |
|-------|-------|-------------|
| melhor que [marca X] | Comparativo depreciativo | Usar CMP-01 (vs media de mercado) |
| superior ao [concorrente] | Citar concorrente proibido | Com specs acima da media de mercado* |
| [marca] nao oferece | Denigrir concorrente | Diferencial exclusivo: [feature] |

### 5.5 Urgencia Falsa (MEDIUM)

| Termo | Razao | Alternativa |
|-------|-------|-------------|
| ultimas unidades | Propaganda enganosa se falso | Permitido APENAS com estoque documentado |
| oferta por tempo limitado | Healthcare B2B nao e varejo | Condicoes especiais para projetos |
| nao perca | Tom inadequado para B2B healthcare | Conheca as condicoes |

### 5.6 Conteudo Visual Proibido (CRITICAL)

- Imagens clinicas reais sem consentimento por escrito
- Fotos de pacientes (reais ou geradas por IA)
- Cenas de procedimentos cirurgicos (reais ou IA)
- Pessoas geradas por IA
- Produto com aparencia alterada por IA (cor, formato, tamanho)
- Emojis que banalizam saude (caveiras, seringas, rostos doentes)
- Dados ou depoimentos inventados

### 5.7 Informacoes Alem do Registro (CRITICAL)

**Regra:** NAO divulgar especificacoes que nao constem no registro ANVISA.
- Indicacoes terapeuticas nao registradas
- Specs de produtos em desenvolvimento (pre-registro)
- Funcionalidades experimentais

### 5.8 Glossario de Traducao Segura

| Tecnico | Acessivel |
|---------|-----------|
| Ra/R9 = 99 | Luz que reproduz as cores exatamente como sao |
| NBR IEC 60601 | Certificado pelas normas brasileiras de seguranca |
| Capacidade bariatrica | Projetada para pacientes de todos os portes |
| Eletro-hidraulico | Movimentacao suave e precisa com controles eletronicos |
| Campo esteril | Sem comprometer a higiene do procedimento |
| CRI (Color Rendering Index) | Indice que mede a fidelidade das cores sob a luz |
| Diluicao de sombra | Visao clara sem obstaculos no campo operatorio |
| IHM Touch Screen | Painel de controle por toque |
| Vida util LEDs >300.000h | Mais de 30 anos de iluminacao em uso tipico |

---

## 6. Banco de Hashtags

### Regras de Uso

| Plataforma | Max | Estrategia |
|-----------|-----|-----------|
| Instagram | 11 | Core (3-5) + Produto (2-3) + Nicho (3-5) |
| LinkedIn | 3-5 | Apenas core + 1-2 tecnicos relevantes |
| YouTube | — | Tags no campo de tags, nao na descricao |
| Facebook | 3 | Apenas core |

### Salk Medical

**Core (sempre):** #SalkMedical, #EquipamentoMedico, #CentroCirurgico, #DispositivoMedico, #MedTech

**Produto (rotar):** #LEV, #FocoCirurgico, #KRATUS, #MesaCirurgica, #OSTUS, #SerraCirurgica, #KRONUS, #COMMAND, #SalaCirurgicaInteligente, #IluminacaoCirurgica

**Nicho (complementar):** #EngenhariaClinica, #SaudePublica, #HospitalBrasileiro, #FabricacaoNacional, #LicitacaoSaude, #ComprasHospitalares, #CirurgiaBrasil, #IndustriaBrasileira

**LinkedIn:** #EquipamentoMedico, #CentroCirurgico, #EngenhariaClinica, #DispositivoMedico, #FabricacaoNacional

### Mendel Medical

**Core:** #MendelMedical, #FabricanteBrasileiro, #EquipamentoMedico, #ANVISA, #MedTech

**Tecnico:** #EngenhariaClinica, #IEC60601, #QualidadeMedica, #ISO13485, #FabricacaoNacional, #PeD, #InovacaoMedica

**Nicho:** #IndustriaBrasileira, #EngenhariaDeProducao, #ControleDeQualidade, #CNC, #MetalmecAnica

### Manager Grupo

**Core:** #ManagerGrupo, #IntegrandoSolucoes, #B2BHealthcare

**Employer Branding:** #TrabalheConosco, #CulturaOrganizacional, #EquipeManagerGrupo, #CarreiraSaude, #VagasParana

**Institucional:** #GrupoEmpresarial, #SaoJoseDosPinhais, #IndustriaParanaense

### Dayho

**Core:** #Dayho, #Metalmecanica, #Usinagem

**Tecnico:** #CNC, #PrecisaoIndustrial, #ControleDeQualidade, #FabricacaoNacional, #IndustriaBrasileira

---

## 7. Specs de Plataforma

### Imagens

| Formato | Dimensoes | Aspecto | Max |
|---------|-----------|---------|-----|
| Instagram Feed Retrato | 1080x1350 | 4:5 | 30MB |
| Instagram Feed Quadrado | 1080x1080 | 1:1 | 30MB |
| Instagram Carousel | 1080x1350 (4:5), max 20 slides, ideal B2B 7-10 | 4:5 | 30MB |
| Instagram Stories | 1080x1920 | 9:16 | 30MB |
| Instagram Reel Cover | 1080x1920 | 9:16 | — |
| LinkedIn Post Paisagem | 1200x627 | 1.91:1 | 5MB |
| LinkedIn Post Quadrado | 1200x1200 | 1:1 | 5MB |
| LinkedIn Carousel PDF | 1080x1080 ou 1080x1350, ideal 8-12 pags | 1:1 ou 4:5 | 100MB |
| YouTube Thumbnail | 1280x720 | 16:9 | 2MB |
| Facebook Post | 1200x630 | 1.91:1 | 10MB |

### Videos

| Formato | Dimensoes | Duracao Ideal | Max |
|---------|-----------|--------------|-----|
| Instagram Reels | 1080x1920 (9:16) | 7-30s (viral) / 30-60s (educativo) | 3 min |
| Instagram Stories | 1080x1920 (9:16) | 15s por story | 60s |
| LinkedIn Video | 1920x1080 (16:9 ou 1:1) | < 90s | 10 min |
| YouTube Shorts | 1080x1920 (9:16) | 20-45s (geral) / 60-90s (B2B) | 3 min |
| YouTube Long | 1920x1080 (16:9) | 10-20 min (demo) / 30-60 min (webinar) | 12h |
| Facebook Video | 1080x1080 (1:1 ou 16:9) | < 60s | 240 min |

### Copy por Plataforma

| Plataforma | Chars | Nivel Tecnico | Tom | Hashtags |
|-----------|-------|--------------|-----|----------|
| Instagram Feed | 300-500 | 5/10 | Acessivel, visual | 11 |
| Instagram Reels | 15-60s script | 3/10 | Dinamico, direto | — |
| Instagram Stories | 1-2 frases | 3/10 | Casual-profissional | 3-5 |
| LinkedIn | 1500-3000 | 8/10 | Profissional, consultivo | 3-5 |
| YouTube Shorts | 20-90s script | 4/10 | Educativo, rapido | — |
| YouTube Long | 5-60 min script | 7/10 | Tutorial, demonstrativo | — |
| Facebook | 80-100 | 4/10 | Conversacional | — |

### Formatos Prioritarios

| Plataforma | 1o | 2o | 3o |
|-----------|----|----|-----|
| Instagram | Reels (60-70%) | Carousels 4:5 (20-30%) | Stories (5-10%) |
| LinkedIn | PDF Carousels (6.60% engagement) | Texto longo + imagem | Video nativo < 90s |
| YouTube | Shorts 9:16 (descoberta) | Videos longos 16:9 (conversao) | — |
| Facebook | Video curto | Posts com imagem | Grupos |

### Frequencia por Marca

**Salk Medical:**
- Instagram Feed: 5x/semana (3 Reels + 2 Carousels)
- Instagram Stories: Diario
- LinkedIn: 5x/semana (2 PDF + 2 Texto + 1 Video)
- YouTube Shorts: 3x/semana
- YouTube Long: 2x/mes
- Facebook: 3x/semana
- Melhores horarios: IG Ter-Qui 11h-13h | LI Ter-Qui 8h-10h | YT 14h-16h | FB 12h-15h

**Mendel Medical:**
- Instagram Feed: 4x/semana | Stories: 4x/semana | LinkedIn: 4x/semana | YouTube Shorts: 2x/semana | YouTube Long: 1x/mes | Facebook: 2x/semana

**Manager Grupo:**
- Instagram Feed: 2x/semana | Stories: 2x/semana | LinkedIn: 2x/semana | Facebook: 1x/semana

**Dayho:**
- Instagram Feed: 1x/semana | LinkedIn: 1x/semana

---

## 8. Calendario Editorial

### Template Semanal (Salk)

| Dia | Foco | Slots |
|-----|------|-------|
| Segunda | Planejamento & Copywriting | IG Carousel 4:5 (11-13h) + LI PDF Carousel (8-10h) |
| Terca | Producao Visual | IG Reel 15-30s (11-13h) + LI Texto+Imagem (8-10h) + FB Video/Post (12-15h) |
| Quarta | Atomizacao/Video | IG Reel 30-60s (11-13h) + YT Short (14-16h) + LI Texto longo (8-10h) |
| Quinta | Revisao & Aprovacao | IG Carousel 4:5 (11-13h) + LI PDF Carousel (8-10h) + FB Post (12-15h) + YT Short (14-16h) |
| Sexta | Agendamento & Distribuicao | IG Reel (11-13h) + LI Video <90s (8-10h) + FB Video (12-15h) |
| Diario | — | IG Stories (enquetes, bastidores, CTAs) |

### Metas MVP (Semanas 1-4)

| Marca | Masters/Semana | Derivados/Master | Foco |
|-------|---------------|------------------|------|
| Salk | 3 | 5-8 | LEV + KRATUS (prioridade maxima) |
| Mendel | 2 | 5-8 | LEV tecnico + KRATUS tecnico |
| Manager Grupo | 0 | — | Diferido para Epico 2 |
| Dayho | 0 | — | Diferido para Epico 2 |

### Metas Regime (Norte de longo prazo)

| Marca | Total/Semana |
|-------|-------------|
| Salk | ~23 |
| Mendel | ~16 |
| Manager Grupo | ~7 |
| Dayho | ~2 |

### Distribuicao de Pilares por Semana (Salk)

Produto: 2 posts | Educacional: 1 | Cases: 1 | COMMAND: 1 | Licitacoes: Quinzenal

### Datas Sazonais

| Data | Evento | Conteudo |
|------|--------|----------|
| 07/04 | Dia Mundial da Saude | Post institucional + dados do setor |
| 01/05 | Dia do Trabalho | Employer branding (Manager Grupo) |
| 12/05 | Dia do Enfermeiro | Homenagem + produto em contexto |
| 12/06 | Dia do Cirurgiao | Conteudo LEV + homenagem |
| 11/07 | Dia do Engenheiro | Conteudo Mendel + bastidores |
| 18/08 | Dia do Medico (Brasil) | Social proof |
| Novembro | Hospitalar (feira) | Cobertura do evento |
| Dezembro | Retrospectiva | Numeros, conquistas, agradecimento |

---

## 9. UTM Patterns

### Estrutura

`?utm_source={source}&utm_medium={medium}&utm_campaign={campaign}&utm_content={content}&utm_term={term}`

### Valores

| Componente | Valores |
|-----------|---------|
| Source | instagram, linkedin, youtube, facebook, email |
| Medium | social (organico), paid (futuro), email |
| Campaign | `{marca}-{ano}-{pilar}` — ex: salk-2026-produto |
| Content | `{formato}-{produto}-{id}` — ex: carousel-lev-001 |

### CTAs por Estagio do Funil

| Estagio | CTA Principal | Plataformas |
|---------|--------------|------------|
| Topo (Awareness) | Baixe o guia: Como especificar focos cirurgicos | Instagram, LinkedIn |
| Meio (Consideracao) | Compare especificacoes: LEV vs media de mercado | LinkedIn, YouTube |
| Meio (Avaliacao) | Agende uma demonstracao tecnica gratuita | LinkedIn, Email |
| Fundo (Decisao) | Solicite uma proposta personalizada | LinkedIn, Email |
| Fundo (Licitacao) | Receba a documentacao completa para licitacao | LinkedIn, Email |

### CTAs por Plataforma

| Plataforma | CTAs |
|-----------|------|
| Instagram | Link na bio, Salve para consultar, Envie para seu engenheiro clinico |
| LinkedIn | Comente "FICHA" e envio a especificacao, Link no primeiro comentario |
| YouTube | Se inscreva para mais conteudo tecnico, Assista a demo no link |
| Facebook | Compartilhe com quem precisa saber, Comente sua duvida |
| Email | [Botao] Agendar Demonstracao, [Botao] Baixar Catalogo Tecnico |

---

## 10. Copywriters por Marca

### Personalidades

| Marca | Copywriter | Tom | Publico |
|-------|-----------|-----|---------|
| Salk | Helena | Consultivo, confiante, resultados | Gestores hospitalares, eng. clinicos, compras |
| Mendel | Roberto | Tecnico, preciso, autoritativo | Engenheiros clinicos, biomedicos, especificadores |
| Manager Grupo | Carolina | Acolhedor, institucional, inspirador | Colaboradores, candidatos, parceiros |
| Dayho | Marcos | Industrial, tecnico, solido | Compradores industriais, eng. de producao |

### Regras Helena (Salk)

- CTA consultivo (nunca agressivo): "Saiba mais", "Converse com um especialista"
- Destaque beneficios praticos (TCO, eficiencia, conformidade)
- Evite jargao tecnico excessivo — acessivel mas profissional
- NUNCA mencione ETRUS / NUNCA use superlativos
- Claims APENAS de fontes aprovadas
- Sempre inclua referencia ANVISA quando aplicavel
- Emojis com moderacao (max 2-3 por post), NUNCA no inicio de frases tecnicas

**Regras por plataforma (Helena):**
- Instagram Post: max 2200 chars, hashtags na ultima linha (5-15), hook forte nos primeiros 150 chars
- Instagram Stories: max 200 chars, 3-5 hashtags, texto curto e direto
- LinkedIn: tom mais formal e tecnico, dados e metricas, max 3000 chars, 3-5 hashtags
- Email: assunto curto (max 60 chars), CTA claro, sem hashtags

### Regras Roberto (Mendel)

- Linguagem tecnica com dados precisos (Ra, lux, kg, normas)
- Destaque certificacoes (ANVISA, ISO, IEC)
- Use numeros e specs sempre que possivel
- CTA tecnico: "Consulte a ficha tecnica", "Veja dados completos"
- NUNCA simplifique demais — publico e tecnico

### Persona Clones (para revisao de copy)

| Persona | Nome | Perfil | Pergunta-chave |
|---------|------|--------|---------------|
| Eng. Clinico | Dr. Marcelo | Cetico com marketing, valoriza dados | "Os dados sao confiaveis? Tem registro ANVISA?" |
| Compras | Fernanda | Focada em numeros, justificar para diretoria | "Tem info de preco? Facilita licitacao?" |
| Equipe Medica | Dra. Ana | Pouco tempo, quer info direta | "Entendi em 5 segundos? Beneficio clinico real?" |
| Administrador | Carlos | Pensa estrategicamente, quer diferenciais | "Ajuda meu hospital a se posicionar? ROI claro?" |

---

## 11. Geracao de Imagem (NB2)

### Dimensoes do Prompt (6 categorias)

**Tecnica:**
| Preset | Descricao |
|--------|-----------|
| hero_shot | Professional hero shot photography, product centered |
| dramatic_studio | Dramatic studio photography with professional lighting setup |
| lifestyle | Lifestyle photography in real-world usage context |
| detail_macro | Macro detail photography showing craftsmanship and precision |
| environmental | Environmental photography showing product in its natural setting |

**Iluminacao:**
| Preset | Descricao |
|--------|-----------|
| dramatic_rim | Dramatic rim lighting with strong key light, deep shadows |
| soft_diffused | Soft diffused lighting, even illumination, minimal shadows |
| high_contrast | High contrast lighting with defined highlights and shadows |
| natural_window | Natural window light, soft and directional |
| clinical_bright | Bright clinical lighting, clean and even |

**Cenario:**
| Preset | Descricao |
|--------|-----------|
| centro_cirurgico | Modern surgical center, clean sterile environment, stainless steel |
| sala_exames | Medical examination room, clinical setting |
| corredor_hospital | Modern hospital corridor, wide and clean |
| laboratorio | High-tech laboratory, precision instruments |
| industrial | Industrial manufacturing floor, CNC machines |
| studio_neutro | Clean neutral photography studio, seamless background |

**Composicao:**
| Preset | Descricao |
|--------|-----------|
| central_hero | Centered composition, product as focal point, rule of thirds |
| angular_dramatico | Low angle dramatic shot, emphasizing scale |
| overhead_tech | Overhead technical view |
| three_quarter | Three-quarter view, showing depth |
| detail_close | Extreme close-up, filling frame with detail |

**Atmosfera:**
| Preset | Descricao |
|--------|-----------|
| premium_tech | Premium technology aesthetic, cool blue tones |
| clean_medical | Clean medical aesthetic, whites and soft blues |
| industrial_warm | Industrial warm tones, amber accents |
| modern_minimal | Modern minimalist, neutral palette |
| dramatic_dark | Dramatic dark mood, selective lighting |

**Detalhes Tecnicos:**
| Preset | Descricao |
|--------|-----------|
| 4k_landscape | 4K, 16:9 landscape, photorealistic |
| square_social | 1080x1080, square for social media |
| portrait_story | 1080x1920, portrait for stories/reels |
| wide_banner | 2560x720, wide banner for covers |

### Negativos Obrigatorios

**Universais:** text, watermark, logo, signature, letters, words, blurry, low quality, distorted, deformed, cartoon, illustration, painting, sketch

**Medicos:** surgical light, operating light, ceiling mounted light, surgical lamp, operating table, surgical table, examination table, medical monitor, patient monitor, display screen, pendant, ceiling mount arm, articulating arm, medical equipment, hospital equipment, medical device, competing medical equipment, other brand equipment, people faces, identifiable patients, blood, graphic medical content, blue monochrome, cyan tint, teal color, neon blue, blue cast

**LEV Especificos:** light rays spreading sideways, diffused glow, scattered light, lens flare, light bleeding, omnidirectional light, ceiling mounted fluorescent, ambient room lighting

### Regras por Produto

**LEV:**
- Must include: visible ceiling area, surgical field below
- Never include: scattered light, diffused glow, lateral rays, other ceiling lights
- Tecnicas preferidas: dramatic_studio, hero_shot
- Iluminacao: dramatic_rim, high_contrast
- Perspectiva camera: ao nivel da cama, olhando PARA CIMA
- Espaco: sala alta, teto proeminente, enfase vertical

**KRATUS:**
- Must include: clean floor area in center, wide room
- Never include: other surgical tables, examination couch, gurney
- Tecnicas: hero_shot, environmental
- Iluminacao: clinical_bright, soft_diffused
- Perspectiva: altura da cintura, levemente elevada
- Espaco: sala ampla, chao limpo, enfase horizontal

**OSTUS:**
- Must include: sterile instrument area, draped surgical surface
- Never include: other power tools, hand saw, competing instruments
- Tecnicas: detail_macro, hero_shot
- Iluminacao: clinical_bright, high_contrast
- Perspectiva: altura da mesa, close-up

**KRONUS:**
- Must include: visible ceiling with mounting rails, upper wall area, gas panels
- Never include: floor-standing rack, consumer monitor arm
- Tecnicas: hero_shot, environmental
- Iluminacao: soft_diffused, clinical_bright
- Perspectiva: altura de pe, olhando levemente para cima

### Mapa de Inferencia (produto por palavra-chave)

| Palavras | Produto |
|----------|---------|
| iluminacao, foco, luz, led, surgical light, visibilidade, lev | LEV |
| mesa, table, posicionamento, paciente, ergonomia, kratus | KRATUS |
| serra, saw, corte, ortopedia, osso, osteotomia, ostus | OSTUS |
| suporte, pendente, monitor, braco, articulado, kronus | KRONUS |

**Produto hero (padrao quando nenhum especificado):** LEV

### Dimension Presets

| Nome | Dimensoes |
|------|-----------|
| feed | 1080x1350 |
| square | 1080x1080 |
| stories | 1080x1920 |
| landscape | 1920x1080 |
| banner | 2560x720 |

### Product Top Picks (imagem PNG padrao)

| Query | Arquivo |
|-------|---------|
| lev / foco cirurgico | Foco de Teto e Parede/Simplex_4LEV.png |
| lev 4lev | Foco de Teto e Parede/Simplex_4LEV.png |
| lev 3lev | Foco de Teto e Parede/Simplex_3LEV.png |
| lev duplex | Foco de Teto e Parede/Duplex_3LEV_4LEV.png |
| kratus / mesa cirurgica | Mesa Cirurgica/KRATUS-EH-460K-ML-clean01.png |
| ostus / serra cirurgica | Serra Cirurgica/Serra Cirurgica OSTUS - full - PNG.png |
| kronus / suporte | Suporte para equipamentos/Suporte-p-Equipamentos-Kronus-biarticulada_clean.png |

---

## 12. Estrategia de Conteudo

### Pesos dos Pilares por Marca (%)

**Salk:** Produto 30% | Educacional 25% | Cases 20% | COMMAND 15% | Licitacoes 10%

**Mendel:** Produto Tecnico 35% | Engenharia 30% | Certificacoes 20% | Bastidores 15%

**Manager Grupo:** Cultura 35% | Inovacao 25% | Pessoas 25% | Institucional 15%

### Produtos Ativos por Marca

| Marca | Produtos |
|-------|----------|
| Salk | lev, kratus, ostus, kronus |
| Mendel | lev, kratus, ostus, kronus |
| Manager Grupo | (nenhum) |
| Dayho | (nenhum) |

### Personas por Pilar

| Pilar | Personas-alvo |
|-------|--------------|
| produto | eng_clinica, compras, equipe_medica |
| educacional | eng_clinica, admin_hospitalar |
| cases | admin_hospitalar, compras |
| command | eng_clinica, equipe_medica |
| licitacoes | compras, admin_hospitalar |
| produto_tecnico | eng_clinica |
| engenharia | eng_clinica |
| certificacoes | eng_clinica, compras |
| bastidores | eng_clinica |

### Tecnicas Visuais por Produto

| Produto | Tecnica | Iluminacao | Cenario | Atmosfera |
|---------|---------|-----------|---------|-----------|
| LEV | dramatic_studio | dramatic_rim | centro_cirurgico | premium_tech |
| KRATUS | hero_shot | high_contrast | centro_cirurgico | clean_medical |
| OSTUS | environmental | soft_diffused | centro_cirurgico | modern_minimal |
| KRONUS | detail_macro | clinical_bright | centro_cirurgico | premium_tech |

### Mapa de Formatos

| Formato | Preset Visual |
|---------|--------------|
| Carousel 4:5 | square_social |
| Reel 9:16 | portrait_story |
| Post 1:1 | square_social |
| Imagem 1200x627 | 4k_landscape |
| Banner | wide_banner |
| PDF Carousel | square_social |
| Video/Post | square_social |
| Shorts 9:16 | portrait_story |
| Video <90s | 4k_landscape |

---

## 13. Atomizacao

### Formatos por Plataforma

| Plataforma | Max Chars | Hashtags | Tom | CTA Style |
|-----------|----------|---------|-----|-----------|
| Instagram Post | 2200 | 30 | Visual, direto, emoji moderado | Link na bio, swipe, salve |
| Instagram Story | 200 | 5 | Ultra-curto, casual, urgente | Arraste pra cima, Toque, Vote |
| Instagram Reels | 300 | 15 | Dinamico, hook nos 3 primeiros segundos | Siga para mais, Comente, Compartilhe |
| LinkedIn Post | 3000 | 5 | Profissional, dados, storytelling | Comente, Saiba mais no link, Conecte-se |
| LinkedIn Article | 10000 | 3 | Formal, aprofundado, thought leadership | Leia completo, Compartilhe |
| Email Snippet | 500 | 0 | Pessoal, direto, valor claro | Clique aqui, Responda, Agende |
| WhatsApp Broadcast | 1000 | 0 | Conversacional, proximo | Responda SIM, Clique, Fale com consultor |

### Mapa de Atomizacao (Master → Derivados)

| Master | Derivados |
|--------|-----------|
| Carrossel | instagram_story, instagram_reels, linkedin_post, email_snippet |
| Post Unico | instagram_story, linkedin_post, whatsapp_broadcast |
| Video Longo | instagram_reels, instagram_story, linkedin_post |
| Artigo | linkedin_post, instagram_post, email_snippet, whatsapp_broadcast |

---

## 14. Quality Gate (Disaster Check)

### Checks que BLOQUEIAM publicacao (severity: block)

| ID | Check | Descricao | Auto-detectavel |
|----|-------|-----------|----------------|
| text_logo | Texto/Logo na Imagem | IA gera texto distorcido. Texto e logo sao adicionados no Canva. | Sim |
| competitor_equipment | Equipamento Concorrente | Nao pode conter equipamentos medicos alem do produto-alvo | Sim |
| identifiable_faces | Rostos Identificaveis | Risco legal (LGPD, direito de imagem) | Sim |
| graphic_clinical | Cenas Clinicas Graficas | Sangue, procedimentos abertos — inadequado para social media | Sim |
| lev_light_direction | Direcao da Luz LEV | LEV vende luz CONCENTRADA. Raios laterais contradizem o produto. (Especifico: LEV) | Sim |
| product_distortion | Distorcao do Produto | Proporcoes erradas, partes faltando, deformacoes | Sim |

### Checks que geram ALERTA (severity: warn)

| ID | Check | Descricao | Auto-detectavel |
|----|-------|-----------|----------------|
| image_quality | Qualidade Tecnica | Blur, artefatos, ruido, baixa resolucao | Sim |
| composition_format | Composicao e Formato | Produto cortado, muito pequeno, composicao inadequada | Sim |
| brand_colors | Paleta de Cores | Cores que conflitam com identidade visual | Nao |
| empty_scene | Cenario Vazio/Generico | Cenario sem contexto (anti-pattern validado) | Sim |

---

## 15. Briefing Atlas

### System Prompt do Atlas (Estrategista de Conteudo)

**Identidade:** Atlas, estrategista de conteudo do Manager Grupo para redes sociais B2B healthcare.

**Regras Inegociaveis:**
1. ETRUS esta BLOQUEADO — nunca mencionar
2. NUNCA prometer resultados medicos
3. NUNCA usar superlativos (o melhor, o unico, garante, infalivel)
4. Claims SOMENTE dos aprovados — NUNCA inventar
5. Tom deve seguir o brandbook da marca
6. Briefing DEVE ser ESPECIFICO ao produto e tema, NUNCA generico
7. Se produto selecionado: mencionar specs e diferenciais reais
8. Se nenhum produto: escolher 1-2 mais relevantes e justificar
9. claims_sugeridos DEVEM ser IDs do banco (ex: LEV-01, KRATUS-03)

**Formato de saida (YAML):**
```yaml
objetivo: "string — especifico ao tema e produto"
mensagem_chave: "string — com diferencial tecnico real do produto"
cta: "string — consultivo, nunca vendedor"
tom: "string"
formato_visual: "string — descricao do cenario para imagem NB2"
hashtags_sugeridas: ["string"]
claims_sugeridos: ["ID do claim — ex: LEV-01"]
notas_visuais: "string — instrucoes especificas para cenario da imagem"
produto_recomendado: "string — produto escolhido e por que"
```

---

## Resumo Quantitativo

| Categoria | Quantidade |
|-----------|-----------|
| Marcas (brandbooks) | 4 |
| Produtos ativos | 4 (LEV, KRATUS, OSTUS, KRONUS) + 1 restrito (COMMAND) + 1 bloqueado (ETRUS) |
| Buyer personas | 4 |
| Claims aprovados | 42 (20 LEV + 10 KRATUS + 3 OSTUS + 3 KRONUS + 2 COMMAND + 3 comparativos + 4 institucionais) |
| Termos proibidos | 5 categorias com ~20 termos |
| Hashtags curadas | ~60 por marca |
| Specs de plataforma | 6 plataformas, 10 formatos de imagem, 6 de video |
| Copywriters | 4 personalidades + 4 persona clones |
| Dimensoes de prompt NB2 | 6 categorias, ~30 presets |
| Negativos obrigatorios | ~50 termos em 3 categorias |
| Regras de produto NB2 | 4 produtos com must/never/tecnicas/perspectiva |
| Pilares de conteudo | 5 (Salk) + 4 (Mendel) + 3 (Manager) + 2 (Dayho) = 14 |
| Formatos de atomizacao | 7 plataformas + 4 mapas master→derivado |
| Quality gate checks | 10 (6 bloqueiam + 4 alertam) |
| Datas sazonais | 8 |
| Arquivos YAML fonte | 18 |

---

> **Fonte unica de verdade:** Todos esses dados sao editaveis pela gestora de marketing em `https://studio.salkmedical.com/` nas secoes **Marca** e **Motor IA** do sidebar.
