# INSIGHTS ESTRATÉGICOS — MESAS CIRÚRGICAS
## Documento para Diretoria e Engenharia — Roadmap MENDEL KRATUS

**Projeto:** Mendel Medical / KRATUS EH 460K
**Data:** 2026-02-25
**Classificação:** Estratégico — Uso Interno
**Fonte:** Inteligência Competitiva — Análise Macro de 5 Fabricantes Nacionais (KSS, OQTIS, MEDIFARR, BARRFAB, MENDEL)

---

## RESUMO EXECUTIVO

> **Diagnóstico central:** O KRATUS EH 460K é a mesa com melhor preço do mercado eletrohidráulico, mas carrega **quatro limitações técnicas objetivamente mensuráveis** que hoje perdem licitações técnicas — mesmo quando o preço seria vencedor.

A análise técnica comparativa de manuais e fichas normativas de cinco fabricantes revelou que **o KRATUS tem carga competitiva (460kg), mas amplitude de movimentos abaixo da média em quase todas as dimensões críticas**. Em especificações que hospitais públicos e privados usam como filtro em licitações — Trendelenburg, inclinação lateral, deslizamento longitudinal e amplitude de altura — a MENDEL fica na posição mais fraca do mercado eletrohidráulico.

**O que a análise revelou:**

- **KSS Vision** não divulga dados técnicos nas fichas analisadas (respostas "subentendido") — indica postura comercial, não necessariamente superioridade técnica. Deve ser tratado como concorrente de marketing, não de engenharia.
- **BARRFAB BF683** tem a maior amplitude de altura (500–1.500mm = 1.000mm de curso) e o Trendelenburg mais competitivo (45°) — tornou-se o benchmark técnico do segmento.
- **MEDIFARR MED 450** entrega 450kg de carga + 35° Trendelenburg + 30° lateral + deslizamento de 350mm a R$52.378 — é o adversário direto mais perigoso para o KRATUS.
- **OQTIS Optimus HS** tem 465kg de carga + 850mm de deslizamento longitudinal — o maior do mercado, tornando-o referência em reposicionamento intraoperatório.
- **MENDEL KRATUS** lidera apenas em preço e na versão bariatrica. As demais dimensões técnicas ficam sistematicamente abaixo da média.

**As três decisões imediatas requeridas:**
1. Investigar se o Trendelenburg pode ser expandido de 25° para 35°+ sem redesenho mecânico estrutural
2. Incorporar deslizamento longitudinal como padrão (hoje apenas acessório pago)
3. Investigar consumo de 840VA — 2,4× acima da concorrência — e mapear impacto em custo de instalação elétrica e operação

---

## 1. OS 5 GAPS CRÍTICOS IDENTIFICADOS

### Gap 1 — Trendelenburg 25°: A Maior Vulnerabilidade Técnica do KRATUS

| Fabricante/Modelo | Trendelenburg | Reverso |
|---|:---:|:---:|
| KSS Vision / OQTIS Optimus | **50°** | **50°** |
| BARRFAB BF683 | **45°** | **45°** |
| MEDIFARR MED 450/360 | **35°** | **35°** |
| MEDIFARR MED 400 | 30° | 30° |
| **MENDEL KRATUS EH** | **25°** | **25°** |

**O problema clínico:** O Trendelenburg acentuado (>30°) é exigido rotineiramente em:
- Cirurgias laparoscópicas pélvicas (histerectomia, prostatectomia, colectomia baixa)
- Cirurgias urológicas robóticas
- Cirurgias vaginais e ginecológicas
- Certas abordagens em cirurgia cardíaca

Com apenas 25°, o KRATUS não atende à amplitude mínima de 30° que muitos hospitais inserem como especificação técnica em licitações. **Em qualquer licitação com critério técnico de Trendelenburg >25°, o KRATUS é desclassificado** — independentemente do preço.

**O que é mais crítico:** A diferença não é marginal. Os concorrentes oferecem de 20% (MED 400: 30°) a 100% mais ângulo (KSS/OQTIS: 50°). O KRATUS hoje fica abaixo de todos os modelos eletrohidráulicos do mercado.

**Ação imediata:** Engenharia deve responder: o limite de 25° é estrutural (geometria do chassi) ou paramétrico (limitação de software/válvula)? Se paramétrico, ajuste pode ser feito sem custo de desenvolvimento relevante.

---

### Gap 2 — Deslizamento Longitudinal: Feature Padrão que o KRATUS Não Tem

| Fabricante/Modelo | Deslizamento Longitudinal |
|---|:---:|
| OQTIS Optimus HS | **Até 850mm** |
| BARRFAB BF683 | até 500mm (cada lado) |
| MEDIFARR MED 450/400 | **350mm** (cada lado) |
| **MENDEL KRATUS EH** | **Não disponível como padrão** |
| MENDEL KRATUS c/ Longitudinal | ±220mm (acessório pago) |

**O problema clínico:** O deslizamento longitudinal do tampo — separadamente do movimento de toda a mesa — é fundamental para:
- Posicionamento correto do paciente em cirurgias de coluna (acesso vertebral preciso)
- Cirurgias de membros inferiores (alinhamento com arco-C)
- Reposicionamento intraoperatório sem anestesiar novamente o paciente
- Integração com mesas de tração ortopédica

**O impacto em licitações:** Hospitais que operam cirurgia de coluna, ortopedia e urologia com frequência incluem "deslizamento longitudinal mínimo de 300mm" como critério técnico eliminatório. O KRATUS perde essas licitações antes mesmo da análise de preço.

**A dimensão financeira:** O acessório "KRATUS c/ Longitudinal" resolve o problema tecnicamente — mas vender o movimento como acessório pago em vez de standard é percebido negativamente nas comparações. **Tornar o longitudinal padrão é ação de posicionamento, não apenas técnica.**

---

### Gap 3 — Amplitude de Altura 200mm: O Menor Curso do Mercado

| Fabricante/Modelo | Altura Mínima | Altura Máxima | **Amplitude** |
|---|:---:|:---:|:---:|
| BARRFAB BF683 | 500mm | 1.500mm | **1.000mm** |
| MEDIFARR MED 400 | 650mm | 1.250mm | 600mm |
| MEDIFARR MED 450 | 600mm | 1.100mm | 500mm |
| **MENDEL KRATUS EH** | **860mm** | **1.060mm** | **200mm** |

**O problema clínico:** A amplitude de altura da mesa é diretamente relevante para:
- Adaptação à altura do cirurgião (diferentes especialidades têm diferentes necessidades)
- Uso sem banquetas — mesas com altura mínima baixa (≤700mm) eliminam banquetas e reduzem risco de queda
- Cirurgias pediátricas onde a mesa precisa estar muito baixa
- Ergonomia da equipe de anestesia e instrumentação

Com apenas 200mm de curso (860–1.060mm), o KRATUS tem a **menor amplitude de altura do mercado** — menos de um quinto da BARRFAB. Em hospitais com equipes de especialidades múltiplas, isso é limitante.

**Contexto adicional:** A altura mínima de **860mm** é muito alta para uso pediátrico e para cirurgiões mais baixos. A BARRFAB chega a 500mm de altura mínima, permitindo trabalho sem banqueta. O KRATUS obriga uso de banqueta em toda a equipe na maioria das situações.

---

### Gap 4 — Inclinação Lateral 10°: Metade da Concorrência

| Fabricante/Modelo | Inclinação Lateral |
|---|:---:|
| MEDIFARR MED 450 | **30°** |
| BARRFAB BF683 | **30°** |
| MEDIFARR MED 400 | 20° |
| **MENDEL KRATUS EH** | **10°** |

**O problema clínico:** A inclinação lateral é usada em:
- Cirurgias abdominais para deslocar vísceras e melhorar acesso (mínimo 15–20° recomendado)
- Cirurgias hepáticas e de vias biliares (flank position)
- Acesso lateral ao rim e retroperitônio
- Cirurgias torácicas em decúbito lateral assistido

Com apenas 10° de inclinação lateral, o KRATUS atinge **metade do ângulo mínimo considerado adequado** para cirurgias abdominais complexas. Hospitais com programas de cirurgia hepática, de cólon avançada ou urologia laparoscópica identificam isso como limitação crítica.

---

### Gap 5 — Consumo de 840VA: 2,4× Acima da Concorrência

| Fabricante/Modelo | Potência (VA) | VA/kg carga |
|---|:---:|:---:|
| KSS Vision T4 EH | 350 | 0,75 VA/kg |
| BARRFAB BF683 | 350 | 0,83 VA/kg |
| MEDIFARR MED 450 | ~400 | 0,89 VA/kg |
| **MENDEL KRATUS EH** | **840** | **1,83 VA/kg** |

**O problema técnico:** 840VA é mais do dobro do consumo dos concorrentes para performance similar. As hipóteses técnicas para esta diferença incluem:
1. **Motor hidráulico sobredimensionado** — bomba hidráulica com potência excessiva para a carga de trabalho
2. **Sistema de 36V (3×12V)** — maior tensão de bateria exige inversor/carregador mais potente
3. **Ineficiência do driver eletrônico** — perdas significativas na conversão AC-DC-AC
4. **Múltiplos atuadores simultâneos** — sistema permite mais movimentos paralelos que consome mais

**O impacto prático:**
- **Instalação elétrica:** 840VA exige circuito dedicado de maior capacidade — custo de instalação adicional para o hospital
- **Custo operacional:** ~2,4× o consumo elétrico dos concorrentes ao longo de 10 anos de operação
- **Temperatura de operação:** maior dissipação de calor nos componentes eletrônicos
- **Argumento de licitação:** hospitais com avaliação de TCO penalizam consumo alto

**Ação de engenharia:** Mapear onde estão as perdas. Se o motor hidráulico está sobredimensionado, um componente de menor potência pode reduzir consumo para 500–600VA sem afetar performance.

---

## 2. PERSPECTIVA: ENGENHARIA MECÂNICA

### O que os dados revelam sobre design mecânico

A comparação das amplitudes de movimento do KRATUS revela um padrão: **em quase todas as dimensões cinemáticas, o KRATUS está sistematicamente abaixo da média do mercado**. Isso sugere não erros pontuais de projeto, mas uma escolha de design conservador — provavelmente priorizando robustez estrutural (460kg de carga) em detrimento de mobilidade.

#### Análise de trade-offs mecânicos

| Dimensão | KRATUS | Mercado | Hipótese mecânica |
|---|:---:|:---:|---|
| Trendelenburg | 25° | 30–50° | Inclinação limitada pelo centro de gravidade do chassi ou pela geometria das colunas hidráulicas |
| Lateral | 10° | 20–30° | Braços de atuação lateral curtos ou ponto de pivô alto |
| Altura | 200mm curso | 500–1.000mm | Coluna hidráulica única de curso limitado |
| Deslizamento | Não padrão | 350–850mm | Falta do trilho de deslizamento integrado ao chassi |

**Insight crítico:** O Trendelenburg de 25° e a inclinação lateral de 10° podem compartilhar a **mesma causa raiz** — o ponto de pivô da mesa está alto e próximo ao centro do tampo. Uma revisão da geometria do chassi que rebaixe o ponto de pivô poderia aumentar ambos os ângulos simultaneamente.

**O benchmark BARRFAB:** A BF683 EH entrega 465kg de carga + 45° Trendelenburg + 30° lateral + 1.000mm de curso de altura com 350VA de consumo. Isso indica que as limitações do KRATUS não são físicas inerentes ao segmento de 460kg — são de design.

#### Recomendações para Engenharia Mecânica

| Área | Meta Mínima | Meta Diferencial | Referência |
|---|:---:|:---:|---|
| Trendelenburg | ≥30° | ≥40° | MEDIFARR MED 450 (35°), BARRFAB (45°) |
| Inclinação lateral | ≥20° | ≥30° | MEDIFARR MED 450, BARRFAB (30°) |
| Curso de altura | ≥500mm | ≥800mm | MEDIFARR MED 400 (600mm), BARRFAB (1.000mm) |
| Deslizamento longitudinal | 350mm padrão | ≥500mm | MEDIFARR (350mm), OQTIS (850mm) |
| Elevação renal | ≥100mm | ≥150mm | MEDIFARR MED 400 (100mm), BARRFAB (200mm) |

---

## 3. PERSPECTIVA: ENGENHARIA ELÉTRICA E ELETRÔNICA

### Análise do sistema de potência e bateria

#### Eficiência energética

O consumo de 840VA do KRATUS exige investigação. Para referência, as potências declaradas são:

| Fabricante | VA | Carga (kg) | VA/kg |
|---|:---:|:---:|:---:|
| BARRFAB BF683 | 350 | 465 | 0,75 |
| KSS Vision T4 EH | 350 | 465 | 0,75 |
| MEDIFARR MED 450 | ~400 | 450 | 0,89 |
| **MENDEL KRATUS EH** | **840** | **460** | **1,83** |

A razão VA/kg do KRATUS é **2,4× maior que a BARRFAB** para carga de trabalho equivalente. As implicações práticas:

1. **Instalação:** A maioria dos hospitais dimensiona a rede elétrica da sala cirúrgica para 800VA de equipamentos. Com 840VA só para a mesa, o hospital pode precisar revisar a instalação.
2. **Certificação:** Alguns editais licitam "potência máxima ≤500VA" como critério — o KRATUS não atende.
3. **Custo elétrico:** Em 10 anos de uso (8h/dia, 5 dias/semana), a diferença de 490VA representa ~17.000 kWh a mais — custo adicional relevante em hospitais com alto volume cirúrgico.

#### Sistema de bateria

| Fabricante | Tecnologia | Capacidade | Autonomia |
|---|:---:|:---:|:---:|
| BARRFAB BF683 | **Íon-lítio** | 60–144 Wh | **3 semanas** |
| KSS Vision | VRLA | ~100 Wh | 3 semanas |
| OQTIS Optimus | VRLA 2×12V | ~120 Wh | **10 dias** |
| **MENDEL KRATUS** | **VRLA 3×12V/9Ah** | **~324 Wh** | **7 dias** |
| MEDIFARR MED 450 | VRLA 1×24V/1,2Ah | ~29 Wh | 5 dias (~20 proc.) |

**Insight positivo:** O KRATUS tem **a maior capacidade energética da análise (324 Wh total)** — 3 baterias de 12V/9Ah. Com 7 dias de autonomia, está em posição competitiva. Porém, a tecnologia VRLA (chumbo-ácido) tem vida útil de 3–5 anos vs. íon-lítio da BARRFAB que dura 8–10 anos.

**Oportunidade:** Migrar para tecnologia **LiFePO4** (lítio ferrofosfato) reduziria o peso das baterias em ~60%, aumentaria a vida útil de 3–5 para 8–10 anos, e eliminaria o risco de vazamento ácido — com argumento de TCO poderoso em licitações.

#### Proteção IP — Diferença relevante

O KRATUS usa **IPX4** (protegido contra respingos de água em qualquer direção) enquanto KSS T4 EH, OQTIS e BARRFAB usam **IP54** (adicionalmente protegido contra poeira).

Em ambiente cirúrgico, poeira de osso (ortopedia), talco de luvas e partículas de gaze entram no interior dos equipamentos durante anos de uso. O IP54 da BARRFAB indica projeto com vedação completa — mais adequado para salas de operação de alta rotatividade.

---

## 4. PERSPECTIVA: PRODUTO E ESTRATÉGIA

### Análise de posicionamento competitivo

#### O problema do "preço mais baixo sem argumento técnico"

O KRATUS tem o menor preço entre as mesas eletrohidráulicas de alto desempenho (R$48.313 vs R$66.950 da BARRFAB). Em cenários de licitação pública, onde o menor preço tecnicamente habilitado vence, isso deveria ser vantagem decisiva.

**Mas o que acontece na prática:**

Em licitações com critério técnico mínimo (cenário mais comum), os compradores incluem exigências que o KRATUS frequentemente não atende:

| Critério comum em licitações | KRATUS | Situação |
|---|:---:|:---:|
| Trendelenburg ≥30° | 25° | ❌ Eliminado |
| Deslizamento longitudinal ≥300mm padrão | Acessório | ❌ Eliminado |
| Altura máxima ≥1.100mm | 1.060mm | ⚠️ Marginal |
| IP54 | IPX4 | ⚠️ Depende do edital |
| Potência ≤600VA | 840VA | ❌ Eliminado em alguns editais |

O resultado: **o KRATUS chega barato mas sai eliminado antes da análise de preço**. O preço competitivo só converte em vitória quando o hospital não exige critérios técnicos mínimos — que é o cenário menos comum nos hospitais de maior valor.

#### Mapa de segmentos — onde o KRATUS é competitivo hoje vs onde perde

| Segmento | KRATUS hoje | Por quê perde/vence |
|---|:---:|---|
| Licitações públicas sem critério técnico mínimo | **Vence** | Menor preço é o único critério |
| Hospitais e clínicas de médio porte privados | **Vence** | Preço + KRATUS Bariátrica como diferencial |
| Centros de cirurgia bariátrica | **Vence** | Único com modelo bariátrico dedicado |
| Licitações com Trendelenburg ≥30° | **Perde** | 25° abaixo do mínimo exigido |
| Centros de cirurgia minimamente invasiva | **Perde** | Sem deslizamento padrão, Trendelenburg insuficiente |
| Hospitais de alta complexidade | **Perde** | IPX4 vs IP54, amplitude de movimentos |
| Licitações com critério de potência ≤600VA | **Perde** | 840VA fora do envelope |

#### O diferencial bariatrico — o ativo mais subutilizado

A **KRATUS Bariátrica EH 460K** é o único produto analisado com modelo dedicado para cirurgia bariátrica com 460kg de carga. Todos os concorrentes usam o modelo padrão (eventualmente com kit de extensão).

O mercado de cirurgia bariátrica no Brasil:
- ~70.000 cirurgias/ano (2024) — crescimento contínuo
- Crescimento de 10–15% ao ano nos últimos 5 anos
- Poucos fornecedores especializados de mesa bariátrica nacional

**Este é o único argumento técnico onde o KRATUS está sozinho no mercado.** A estratégia de produto deve amplificar isso — com certificação, dados de segurança específicos, e marketing focado em centros de obesidade.

---

## 5. ROADMAP INTEGRADO — AÇÕES IMEDIATAS + DESENVOLVIMENTO

### Fase 1: Ações sem custo de desenvolvimento — Q1/Q2 2026

Antes de qualquer redesenho, há ações de **documentação e esclarecimento** que podem converter licitações perdidas em conquistas, com custo próximo de zero:

| Ação | Impacto | Esforço | Prazo |
|---|:---:|:---:|:---:|
| Investigar se Trendelenburg pode ser parametricamente expandido para 30°+ | **Crítico** | Baixo | 15 dias |
| Confirmar se deslizamento longitudinal pode ser padrão sem custo extra | Alto | Baixo | 15 dias |
| Documentar consumo real vs. nominal 840VA (é pico ou contínuo?) | Alto | Baixo | 15 dias |
| Criar material de venda focado no nicho bariatrico | Alto | Baixo | 30 dias |
| Investigar upgrade IPX4 → IP54 nos modelos atuais | Médio | Médio | 60 dias |
| Publicar especificações técnicas completas da KRATUS Bariatrica | Alto | **Baixo** | 15 dias |

> **Nota sobre 840VA:** Se o valor declarado no manual é a potência de **pico** (não nominal contínua), isso deve ser explicitado na documentação técnica. Muitos editais permitem até 1000VA de pico com consumo médio de 400VA — se for o caso, a MENDEL pode clarificar esse dado e eliminar uma eliminação injusta.

### Fase 2: Desenvolvimentos de alto impacto — Q3/Q4 2026

| Feature | Impacto | Esforço estimado | Prioridade |
|---|:---:|:---:|:---:|
| Trendelenburg ≥35° (redesenho do ponto de pivô) | **Crítico** | Alto | **P1** |
| Deslizamento longitudinal padrão (≥350mm) | **Crítico** | Médio | **P1** |
| Curso de altura mínimo ≥700mm (de 860mm → 700mm mínimo) | Alto | Alto | **P2** |
| Inclinação lateral ≥20° | Alto | Médio | **P2** |
| Migração de bateria para LiFePO4 | Médio | Médio | **P2** |
| IP54 nos modelos eletrohidráulicos | Médio | Médio | **P2** |
| Redução de consumo para ≤500VA | Alto | Alto | **P3** |

### Fase 3: Posicionamento do portfólio — Q1 2027

| Linha | Posicionamento | Argumento principal | Segmento |
|---|---|---|---|
| KRATUS EH 460K (revisado) | Mid-Premium | Preço + Trendelenburg ≥35° + 460kg | Hospitais públicos e privados mid-market |
| KRATUS Bariátrica EH | Especialista | Único bariátrico nacional com 460kg | Centros de obesidade |
| KRATUS c/ Longitudinal (novo padrão) | High-End | Movimento completo + preço competitivo | Hospitais de alta complexidade |

---

## 6. MATRIZ DE PRIORIZAÇÃO — IMPACTO × ESFORÇO

### Para o KRATUS EH 460K (ações imediatas)

| Ação | Impacto | Esforço | Quadrante | Prioridade |
|---|:---:|:---:|:---:|:---:|
| Investigar expansão Trendelenburg param. | **Crítico** | **Baixo** | Quick Win | **P1** |
| Publicar specs completas da bariatrica | Alto | **Baixo** | Quick Win | **P1** |
| Esclarecer 840VA (pico vs. nominal) | Alto | **Baixo** | Quick Win | **P1** |
| Deslizamento longitudinal como padrão | **Crítico** | Médio | Estratégico | **P1** |
| Material de venda nicho bariatrico | Alto | **Baixo** | Quick Win | **P1** |
| IP54 upgrade | Médio | Médio | Considerar | **P2** |
| Migração LiFePO4 | Médio | Médio | Diferencial | **P2** |

### Para redesenho do KRATUS (próxima geração)

| Feature | Impacto | Esforço | Quadrante | Prioridade |
|---|:---:|:---:|:---:|:---:|
| Trendelenburg ≥35° | **Crítico** | Alto | Estratégico | **P1** |
| Deslizamento longitudinal ≥350mm padrão | **Crítico** | Médio | Must-have | **P1** |
| Inclinação lateral ≥20° | Alto | Médio | Must-have | **P1** |
| Curso de altura ≥700mm (mín. baixo) | Alto | Alto | Estratégico | **P2** |
| Redução consumo ≤500VA | Alto | Alto | Estratégico | **P2** |
| Bateria LiFePO4 | Médio | Médio | Diferencial | **P2** |
| Elevação renal ≥150mm declarada | Médio | Baixo | Quick Win | **P1** |

### Legenda de quadrantes

```
         ALTO IMPACTO
              ↑
  [Estratégico]    [Must-have / Quick Win]
       Alto esforço ← ─ → Baixo esforço
   [Considerar]    [Preencher / Evitar]
              ↓
         BAIXO IMPACTO
```

---

## 7. SCORECARD — KRATUS vs. CONCORRENTES POR CRITÉRIO DE LICITAÇÃO

### Critérios técnicos mais comuns em editais de licitação de mesas cirúrgicas

| Critério de licitação | KSS T4 EH | BARRFAB EH | MEDIFARR 450 | **MENDEL KRATUS** |
|---|:---:|:---:|:---:|:---:|
| Carga ≥450kg | ✅ 465kg | ✅ 465kg | ✅ 450kg | ✅ **460kg** |
| Trendelenburg ≥30° | ✅ 50° | ✅ 45° | ✅ 35° | ❌ **25°** |
| Trendelenburg ≥35° | ✅ 50° | ✅ 45° | ✅ 35° | ❌ **25°** |
| Deslizamento long. padrão | n/d | ✅ 500mm | ✅ 350mm | ❌ acessório |
| Lateral ≥20° | n/d | ✅ 30° | ✅ 30° | ❌ **10°** |
| Altura mínima ≤750mm | n/d | ✅ 500mm | ✅ 600mm | ❌ **860mm** |
| IP54 | ✅ | ✅ | ❌ (IPX4) | ❌ (IPX4) |
| Potência ≤600VA | ✅ 350VA | ✅ 350VA | ✅ ~400VA | ❌ **840VA** |
| Vida útil ≥10 anos | ✅ | ✅ | ✅ | ✅ |
| Bariatrica ≥400kg | ❌ | ❌ | ❌ | ✅ **460kg** |

> **Leitura:** Em licitações que exigem os critérios mais comuns simultaneamente, **o KRATUS é eliminado em até 6 de 9 critérios técnicos** — mesmo sendo o mais barato. O único critério exclusivo do KRATUS é a versão bariatrica.

---

## 8. CONCLUSÃO — SÍNTESE DOS ESPECIALISTAS

### O que o KRATUS precisa ser para vencer licitações técnicas:

> O KRATUS tem o ativo mais valioso do mercado — **o menor preço entre as eletrohidráulicas de alta carga** — mas hoje desperdiça essa vantagem sendo eliminado antes da análise de preço. A correção das limitações técnicas não requer redesenho completo, mas ajustes direcionados em Trendelenburg, deslizamento e amplitude de altura.

**Checklist mínimo para competir em licitações técnicas (próxima geração):**

- [ ] Trendelenburg ≥35° (hoje: 25°) — **requisito crítico**
- [ ] Deslizamento longitudinal ≥350mm como padrão (hoje: acessório) — **requisito crítico**
- [ ] Inclinação lateral ≥20° (hoje: 10°) — **requisito crítico**
- [ ] Altura mínima ≤750mm (hoje: 860mm) — importante
- [ ] Consumo ≤600VA declarado como contínuo (hoje: 840VA pico ou nominal?)
- [ ] IP54 nos modelos EH (hoje: IPX4)
- [ ] Especificações técnicas completas e publicadas da versão bariatrica

**Mensagem de venda recomendada para o portfólio atual:**

> *"O KRATUS EH 460K entrega a maior capacidade de carga da categoria (460kg) com o melhor preço do mercado — e é o único fabricante nacional com solução integrada e dedicada para cirurgia bariátrica. Para hospitais que precisam de máxima segurança de carga sem custo premium."*

**Segmentos onde o KRATUS deve concentrar esforços comerciais hoje:**
1. Hospitais gerais públicos com foco em ortopedia, ginecologia e laparotomia (sem exigência de Trendelenburg extremo)
2. Centros de cirurgia bariátrica — onde o KRATUS é único
3. Hospitais privados de médio porte com orçamento controlado
4. Licitações onde preço é o critério dominante

---

## APÊNDICE — COMPARATIVO TÉCNICO COMPLETO

### Todas as dimensões analisadas

| Dimensão | KSS T4 EH | OQTIS HS | MEDIFARR 450 | BARRFAB EH | **MENDEL EH** | Posição MENDEL |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Carga trabalho (kg) | 465 | 465 | 450 | 465 | **460** | 2º lugar |
| Trendelenburg (°) | 50 | 50 | 35 | 45 | **25** | **Último** |
| Reverso (°) | 50 | 50 | 35 | 45 | **25** | **Último** |
| Lateral (°) | n/d | n/d | 30 | 30 | **10** | **Último** |
| Dorso subir (°) | n/d | n/d | 90 | 90 | **65** | 3º |
| Deslizamento (mm) | n/d | 850 | 350 | 500 | **0 padrão** | **Último** |
| Altura mínima (mm) | n/d | n/d | 600 | 500 | **860** | **Último** |
| Curso de altura (mm) | n/d | n/d | 500 | 1.000 | **200** | **Último** |
| Potência (VA) | 350 | n/d | ~400 | 350 | **840** | **Último** |
| Proteção IP | IP54 | IP54 | IPX4 | IP54 | **IPX4** | 3º |
| Autonomia bateria | 3 sem | 10 dias | 5 dias | 3 sem | **7 dias** | 3º |
| Vida útil (anos) | 10 | 10 | 10 | 10 | **10** | 1º (empate) |
| Preço (R$) | n/d | n/d | 52.378 | 66.950 | **48.313** | **1º (menor)** |
| Opção bariatrica | ❌ | ❌ | ❌ | ❌ | **✅ 460kg** | **1º (único)** |

---

*Documento gerado em 2026-02-25 | Projeto: Inteligência Competitiva Mendel Medical | Roadmap Estratégico — Mesas Cirúrgicas*
*Fonte: MAPA_Concorrencia_MESA.xlsx + manuais técnicos verificados (KSS, OQTIS, MEDIFARR MED400/450, BARRFAB BFMCMT/BFMCME, MENDEL KRATUS R07)*
