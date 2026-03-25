# Premissas Regulatórias — Mapeamento Competitivo de Focos e Mesas Cirúrgicas
**Projeto:** Inteligência Competitiva — Mendel Medical / ETROS
**Data:** Fevereiro de 2026
**Finalidade:** Contextualizar as normas técnicas e regulatórias que fundamentam os parâmetros do MAPA de Concorrência para leitura pela equipe de Engenharia

---

## 1. Estrutura Regulatória Aplicável

### 1.1 Focos Cirúrgicos

| Norma | Título | Relevância |
|-------|--------|-----------|
| **ABNT NBR IEC 60601-2-41:2011** | Equipamento eletromédico — Requisitos particulares para segurança básica e desempenho essencial de **focos cirúrgicos** e focos de diagnóstico | Principal norma técnica — todos os parâmetros de fotometria, segurança elétrica e irradiância são avaliados conforme esta norma |
| **ABNT NBR IEC 60601-1:2010** | Requisitos gerais para segurança básica e desempenho essencial | Norma mãe — aplicável a todos os equipamentos eletromédicos; exigências de isolamento, proteção elétrica e classificação |
| **ABNT NBR IEC 60601-1-2** | Perturbações eletromagnéticas — Requisitos e ensaios | Compatibilidade eletromagnética (EMC/EMI) — obrigatório para uso em centro cirúrgico |
| **RDC ANVISA 751/2022** | Registro de Produtos para a Saúde | Exige registro válido na ANVISA antes da comercialização; focos são classificados como Classe de Risco II ou III |

### 1.2 Mesas Cirúrgicas

| Norma | Título | Relevância |
|-------|--------|-----------|
| **ABNT NBR IEC 60601-1:2010** | Equipamento eletromédico — Requisitos gerais | Classificação elétrica, segurança mecânica, resistência de carga |
| **ABNT NBR IEC 60601-1-6** | Usabilidade | Ergonomia e facilidade de operação — exigência de validação de usabilidade |
| **ABNT NBR IEC 60601-1-11** | Requisitos para equipamentos em ambiente de cuidados domiciliares | Contexto de transporte e ambiente de uso |
| **ISO 13485:2016** | Sistemas de gestão da qualidade para dispositivos médicos | Obrigatório para fabricação e comercialização — exigido pela ANVISA |
| **RDC ANVISA 751/2022** | Registro de Produtos para a Saúde | Mesas cirúrgicas são Classe de Risco III (alta complexidade, contato direto com paciente) |

---

## 2. Parâmetros Fotométricos — Focos Cirúrgicos (ABNT NBR IEC 60601-2-41)

Esta seção explica **por que cada parâmetro existe** no MAPA de Concorrência de Focos.

### 2.1 Iluminância Central (Ec — lux)
- **O que é:** Intensidade luminosa no ponto central do campo iluminado, medida a 1 metro de distância
- **Exigência da norma:** Mínimo de **40.000 lux** no campo central; máximo de **160.000 lux**
- **Por que importa:** Iluminância insuficiente compromete a visualização de tecidos durante cirurgias longas; iluminância excessiva provoca fadiga ocular e aquecimento tecidual
- **No MAPA:** Linha "Iluminância máxima (lux)"

### 2.2 Campo Luminoso — d50 e d10 (mm)
- **O que é:** Diâmetro do campo onde a iluminância é ≥ 50% (d50) e ≥ 10% (d10) do valor central
- **Exigência da norma:** d50 deve estar entre 100 mm e 300 mm; d10 entre d50 e 350 mm
- **Por que importa:** Define a "abertura" do foco — campos muito pequenos exigem reposicionamento constante; muito grandes iluminam a equipe, causando ofuscamento
- **No MAPA:** Linhas "Diâmetro d50 (mm)" e "Diâmetro d10 (mm)"

### 2.3 Profundidade de Iluminação (mm)
- **O que é:** Distância axial na qual a iluminância permanece ≥ 20% ou ≥ 60% do valor máximo
- **Exigência da norma:** Profundidade a 60% deve ser reportada pelo fabricante
- **Por que importa:** Quanto maior a profundidade, melhor a visualização em cavidades profundas (cirurgias abdominais, torácicas). É um diferencial técnico crítico.
- **No MAPA:** Linhas "Profundidade de iluminação @60% (mm)" e "@20% (mm)"

### 2.4 Índice de Reprodução de Cor (Ra e R9)
- **O que é:** Ra = média do rendimento de cor em 8 cores padrão; R9 = reprodução da cor vermelha especificamente
- **Exigência da norma:** Ra ≥ 85 (mínimo obrigatório); mercado exige Ra ≥ 90
- **Por que importa:** O R9 alto é essencial para distinguir tecidos, vasos sanguíneos e órgãos durante cirurgia. Ra baixo mascara hemorragias e altera percepção do estado do tecido.
- **No MAPA:** Linhas "CRI — Ra" e "R9"

### 2.5 Irradiância (Ee — W/m²)
- **O que é:** Potência de radiação térmica emitida no campo cirúrgico
- **Exigência da norma:** Ee/Ec ≤ 3,85 W/m² por cada 1.000 lux (ABNT NBR IEC 60601-2-41, item 201.12.4.4)
- **Por que importa:** Limite de segurança para evitar aquecimento tecidual e desidratação do campo cirúrgico. LED tem vantagem sobre halogênio neste quesito.
- **No MAPA:** Linha "Irradiância Ee (W/m²)"

### 2.6 Classificação de Proteção (IP)
- **O que é:** Índice de proteção contra poeira (1° dígito) e líquidos (2° dígito)
- **Exigência mínima:** IP54 para uso em centro cirúrgico (protegido contra poeira e respingos)
- **Por que importa:** Ambiente cirúrgico exige lavagem e desinfecção com produtos químicos. IP baixo compromete a vida útil e a segurança elétrica.
- **No MAPA:** Linha "Proteção IP"

### 2.7 Classificação Elétrica (Parte Aplicada)
- **O que é:** Tipo de proteção elétrica do ponto de aplicação ao paciente
- **Tipos:** Tipo B (corpo flutuante, sem proteção de desfibrilador), Tipo BF (body floating, proteção de desfibrilador), Tipo CF (cardiac floating, proteção máxima)
- **Relevante para focos:** Tipo B ou BF — a cabeça do foco não toca o paciente, mas fica no campo estéril
- **No MAPA:** Linha "Parte aplicada (tipo)"

---

## 3. Parâmetros Técnicos — Mesas Cirúrgicas (ABNT NBR IEC 60601-1)

### 3.1 Carga Máxima (kg)
- **Exigência:** Resistência mecânica validada em ensaios estáticos e dinâmicos
- **Relevância clínica:** Cirurgias bariátricas exigem mesas com capacidade ≥ 450 kg; padrão geral ≥ 200 kg
- **Tendência de mercado:** Demanda crescente por mesas bariátricas (obesidade é problema de saúde pública)

### 3.2 Posições e Ângulos (Trendelenburg, Lateral, Reverso)
- **Trendelenburg:** Cabeça abaixo, pernas acima — essencial para cirurgias pélvicas e laparoscopia
- **Reverso:** Cabeça acima — cirurgias abdominais superiores e bariátricas
- **Lateral:** Inclinação lateral — cirurgias torácicas e ortopédicas
- **Exigência clínica:** Trendelenburg ≥ 25° é considerado adequado para laparoscopia segura

### 3.3 Transparência Radiológica (Raios-X)
- **O que é:** Capacidade do tampo de deixar passar raios-X sem interferência
- **Por que importa:** Cirurgias ortopédicas e vasculares exigem fluoroscopia intraoperatória em tempo real; tampo radiolúcido elimina necessidade de troca de mesa
- **Impacto no custo hospitalar:** Mesa com tampo radiolúcido evita a aquisição de mesa de fluoroscopia separada

### 3.4 Sistema de Bateria e Autonomia
- **Exigência:** Operação elétrica contínua em caso de falta de energia
- **Relevância:** Segurança crítica — paciente não pode ficar preso em posição inclinada em caso de queda de energia
- **Parâmetro avaliado no MAPA:** Tipo de bateria, tensão, capacidade (Ah) e autonomia estimada

### 3.5 Classificação de Risco ANVISA — Mesas
- **Classe III** (alto risco): Regulamentado pela RDC 751/2022
- **Exige:** Registro ANVISA válido, ensaios de conformidade, relatório técnico de segurança, certificação por OCP (Organismo de Certificação de Produto) acreditado pelo INMETRO

---

## 4. Processo de Registro ANVISA — Como Interpretar os Dados

### 4.1 O que um Registro ANVISA garante
- Produto testado e aprovado conforme normas ABNT/IEC aplicáveis
- Fabricante com ISO 13485 ou equivalente certificado
- Bulas, manuais e rotulagem aprovados em português
- Rastreabilidade de lote e pós-mercado ativo

### 4.2 O que NÃO garante
- Que o produto seja o melhor tecnicamente — apenas que é seguro e atende requisitos mínimos
- Que os dados do manual sejam as melhores especificações disponíveis no mercado
- **Por isso o MAPA existe:** para comparar além do mínimo regulatório

### 4.3 Como consultar no portal ANVISA
- Acesse: **https://consultas.anvisa.gov.br/#/produtos-medicos/**
- Filtros úteis: Razão Social do Fabricante, Categoria do Produto
- Categorias relevantes:
  - Focos Cirúrgicos: categoria "Foco Cirúrgico" ou "Luminária Cirúrgica"
  - Mesas Cirúrgicas: categoria "Mesa Cirúrgica"
- Os links diretos para os registros de cada fabricante estão listados na seção 5 deste documento

---

## 5. Registros ANVISA por Fabricante

> **Portal de consulta oficial:** https://consultas.anvisa.gov.br/#/produtos-medicos/
> **Fonte complementar (busca indexada):** https://www.smerp.com.br/anvisa/

---

### 5.1 Focos Cirúrgicos

#### KSS Comércio e Indústria de Equipamentos Médico LTDA
- **Produto:** Foco Cirúrgico SKYLED
- **Nº Registro ANVISA:** 10242640034 — **VÁLIDO**
- **CNPJ:** 79.805.263/0001-28
- **Link registro:** https://www.smerp.com.br/anvisa/?ac=prodDetail&anvisaId=10242640034
- **Busca por empresa:** https://consultas.anvisa.gov.br/#/produtos-medicos/?nomeEmpresa=KSS

#### Med Light Equipamentos Médicos Hospitalares LTDA
- **Produto:** Foco Cirúrgico Illumina / Apollo (família Illumina)
- **Nº Registro ANVISA:** 80712710005 — **VÁLIDO**
- **Link registro:** https://www.smerp.com.br/anvisa/?ac=prodDetail&anvisaId=80712710005
- **Busca por empresa:** https://consultas.anvisa.gov.br/#/produtos-medicos/?nomeEmpresa=MED+LIGHT
- **Manual do Usuário (ANVISA):** https://consultas.anvisa.gov.br/api/consulta/produtos/25351283857202058/anexo/T29401279/nomeArquivo/Manual+do+Usu%C3%A1rio+-+FT+Fam%C3%ADlia+Illumina+-+Rev.+12..pdf?Authorization=Guest

#### OQTIS Indústria de Equipamentos Hospitalares LTDA
- **Produto:** Foco Cirúrgico Sirius (S1, S2, S3)
- **CNPJ:** 47.806.382/0001-09 — Farroupilha, RS
- **Nº Registro ANVISA:** não indexado em buscas públicas — consultar diretamente no portal
- **Busca por empresa:** https://consultas.anvisa.gov.br/#/produtos-medicos/?nomeEmpresa=OQTIS
- **Site do produto:** https://oqtis.com.br/produtos/foco_cirurgico_sirius

#### MEDPEJ Equipamentos Médicos LTDA EPP
- **Produto:** Foco Cirúrgico FL-2000 TL (teto LED)
- **CNPJ:** 03.155.958/0001-40
- **Registros encontrados (família FL-2000):**
  - Nº 80127840017 — FL-2000-T (Lâmpada) — **VÁLIDO** → https://www.smerp.com.br/anvisa/?ac=prodDetail&anvisaId=80127840017
  - Nº 80127840020 — FL-2000-P (Lâmpada) — **VÁLIDO** → https://www.smerp.com.br/anvisa/?ac=prodDetail&anvisaId=80127840020
- **Busca por empresa:** https://consultas.anvisa.gov.br/#/produtos-medicos/?nomeEmpresa=MEDPEJ
- **Nota:** Os modelos TL de teto LED podem ter registro distinto — verificar no portal por empresa

#### MENDEL — Focos Cirúrgicos
- **Produto:** Foco Cirúrgico LED (modelos 3LEV, 4LEV — Teto/Parede, Simplex/Duplex/Triplex)
- **Nº Registro ANVISA:** 81205910005 — **VÁLIDO**
- **CNPJ:** 20.102.553/0001-62 — São José dos Pinhais, PR
- **Link registro:** https://www.smerp.com.br/anvisa/?ac=prodDetail&anvisaId=81205910005
- **Busca por empresa:** https://consultas.anvisa.gov.br/#/produtos-medicos/?nomeEmpresa=MENDEL

#### ETROS (marca da Mendel Medical)
- **Status:** A marca "ETROS" não foi localizada como razão social no cadastro ANVISA
- **Provável situação:** Os focos ETROS estão registrados sob a razão social da **Mendel** (CNPJ 20.102.553/0001-62) ou em fase de registro próprio
- **Ação recomendada:** Confirmar com a equipe jurídica/regulatório o CNPJ e razão social utilizados para o registro do ETROS na ANVISA
- **Busca por empresa:** https://consultas.anvisa.gov.br/#/produtos-medicos/?nomeEmpresa=MENDEL

---

### 5.2 Mesas Cirúrgicas

#### MENDEL — Mesa Cirúrgica KRATUS
- **Produto:** Mesa Cirúrgica KRATUS (EH 460K e variantes)
- **Nº Registro ANVISA:** 81205910007 — **VÁLIDO**
- **Link registro:** https://www.smerp.com.br/anvisa/?ac=prodDetail&anvisaId=81205910007
- **Manual KRATUS (ANVISA):** https://consultas.anvisa.gov.br/api/consulta/produtos/25351060214202208/anexo/T24758455/nomeArquivo/MM014-092406-R03+MANUAL+MESA+CIRURGICA+KRATUS.pdf?Authorization=Guest
- **Busca por empresa:** https://consultas.anvisa.gov.br/#/produtos-medicos/?nomeEmpresa=MENDEL

#### MEDIFARR Produtos para a Saúde LTDA
- **Produto:** Mesa Cirúrgica (MEC/S 140 mecânica + MED400/MED450 motorizadas)
- **CNPJ:** 07.540.203/0001-10 — Caxias do Sul, RS
- **Nº Registro ANVISA (mecânica):** 80918710001 — **VÁLIDO** → https://www.smerp.com.br/anvisa/?ac=prodDetail&anvisaId=80918710001
- **Busca por empresa:** https://consultas.anvisa.gov.br/#/produtos-medicos/?nomeEmpresa=MEDIFARR
- **Manual MED400 (ANVISA):** https://consultas.anvisa.gov.br/api/consulta/produtos/25351324830202022/anexo/T30398592/nomeArquivo/MEDIFARR+MANUAL+DO+OPERADOR+MED+400+-Rev5.pdf?Authorization=Guest
- **Manual MED450 (ANVISA):** https://consultas.anvisa.gov.br/api/consulta/produtos/25351324830202022/anexo/T30398591/nomeArquivo/MANUAL+MED450+Rev1+.pdf?Authorization=Guest
- **Nota:** Registro específico dos modelos MED400/450 (motorizados) — verificar por empresa no portal

#### BARRFAB Indústria e Comércio Imp. Exp. de Equipamentos Hospitalares LTDA
- **Produto:** Mesa Cirúrgica (linha BF683 — ST, EH, TD, TDP, TDO, TDV, RX)
- **CNPJ:** 02.836.248/0001-12 — Farroupilha, RS
- **Busca por empresa:** https://consultas.anvisa.gov.br/#/produtos-medicos/?nomeEmpresa=BARRFAB
- **Manual técnico (ANVISA):** https://consultas.anvisa.gov.br/api/consulta/produtos/25351311925201003/anexo/T26105620/nomeArquivo/Manual+de+Instru%C3%A7%C3%B5es+de+Uso+e+T%C3%A9cnico+de+Servi%C3%A7os+-+BFMCMT+MMXXIV+-+17.pdf?Authorization=Guest
- **Site oficial:** https://www.barrfab.com.br
- **Nota:** Número de registro específico (estilo 80xxxxxxx) — consultar diretamente no portal por empresa

---

## 6. Premissas de Leitura do MAPA de Concorrência

A equipe de Engenharia deve considerar as seguintes premissas ao analisar os MAPAs:

### 6.1 Fonte dos Dados
- Todos os dados foram extraídos diretamente dos **manuais do usuário e de instalação** dos fabricantes, disponíveis nos registros ANVISA de cada empresa
- Dados não encontrados nos manuais foram sinalizados como **"Não especificado"** ou **"?"** — NÃO foram estimados ou inventados
- Onde existe incerteza, a célula foi marcada com "verificar" ou deixada em branco

### 6.2 Limitações Conhecidas
| Lacuna | Motivo | Impacto |
|--------|--------|---------|
| MENDEL Bariatrica (coluna AG) — maioria vazia | Bariatrica é acessório (tampo alargado +300mm), não modelo separado; manual não lista specs distintas | Baixo — a diferença é dimensional, não técnica |
| ETROS colunas AC-AF — emergência, câmera, controle sem fio | São specs do produto próprio que a equipe deve preencher | Alto — completar com dados internos |
| MEDIFARR coluna S — modelo não identificado | Manual MED400 cobre modelos 360/400; MED450 é separado; há referência a modelo adicional não documentado | Médio — verificar catálogo interno |

### 6.3 Como a Engenharia Deve Usar os MAPAs
1. **Identificar gaps de produto:** Onde a Mendel/ETROS está abaixo do mercado em parâmetros normativos
2. **Identificar oportunidades de diferenciação:** Onde pode superar a concorrência além do mínimo regulatório
3. **Validar requisitos de projeto:** Usar como referência para especificação mínima e desejada nos novos produtos
4. **Priorizar ensaios:** Focar em parâmetros onde a concorrência apresenta melhores valores (Ra, R9, profundidade de campo, Trendelenburg)

---

## 7. Glossário de Termos Técnicos

| Termo | Definição |
|-------|-----------|
| **Ec (lux)** | Iluminância — quantidade de luz que incide por unidade de área |
| **Ee (W/m²)** | Irradiância — potência de radiação eletromagnética por unidade de área |
| **Ra** | Color Rendering Index (CRI) médio — fidelidade de reprodução de cores (0-100) |
| **R9** | Índice de reprodução da cor vermelha especificamente — crítico para tecidos biológicos |
| **d50** | Diâmetro do campo onde Ec ≥ 50% do valor central |
| **d10** | Diâmetro do campo onde Ec ≥ 10% do valor central |
| **IP54** | Proteção contra poeira (5) e respingos d'água de qualquer direção (4) |
| **Tipo B / BF** | Classificação de segurança elétrica da parte aplicada (contato com paciente) |
| **VRLA** | Valve-Regulated Lead Acid — bateria selada regulada por válvula (sem manutenção) |
| **Trendelenburg** | Posição do paciente com cabeça abaixo e pernas elevadas |
| **Radiolúcido** | Material que deixa passar raios-X sem atenuar a imagem (tampo transparente ao RX) |
| **RDC** | Resolução da Diretoria Colegiada — ato normativo da ANVISA |
| **OCP** | Organismo de Certificação de Produto — entidade acreditada pelo INMETRO |

---

*Documento elaborado para uso interno da equipe de Engenharia da Mendel Medical.*
*Fevereiro de 2026 — Inteligência Competitiva — Projeto Diferenciais*
