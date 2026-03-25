# INSIGHTS ESTRATÉGICOS — FOCOS CIRÚRGICOS
## Documento para Diretoria e Engenharia — Roadmap MENDEL + ETROS

**Projeto:** Mendel Medical / ETROS
**Data:** 2026-02-25
**Classificação:** Estratégico — Uso Interno
**Fonte:** Inteligência Competitiva — Análise Macro de 5 Fabricantes Nacionais

---

## RESUMO EXECUTIVO

> **Oportunidade identificada:** Nenhum fabricante nacional combina hoje os quatro requisitos técnicos premium simultaneamente. A ETROS pode ser o primeiro.

O mercado brasileiro de focos cirúrgicos LED de teto é composto por cinco players ativos (KSS, MEDLIGHT, OQTIS, MEDPEJ, MENDEL) e um emergente a monitorar (BARRFAB). A análise técnica detalhada de manuais, fichas normativas e dados de campo revela **lacunas claras e não disputadas** que representam a janela de oportunidade para o lançamento da linha ETROS.

**O que a análise revelou:**

- **OQTIS** é o líder técnico em eficiência térmica (50% menos calor que a média), mas tem Ra=98 — não atinge o topo colorimétrico.
- **MEDPEJ e MEDLIGHT** lideram em colorimetria (Ra=99/R9=99), mas têm vida útil curta (5 anos) e outras fraquezas.
- **KSS** lidera em conformidade normativa e profundidade de campo, mas tem Ra=96 — o pior índice de cor do mercado.
- **MENDEL** (linha atual) tem Ra=99, mas R9=91 na 3LEV — a maior vulnerabilidade da marca em campo clínico — e diluição de sombra de apenas 14–15%.

**A lacuna estratégica:** nenhum fabricante combina `Ee/Ec ≤2,0` + `Ra≥99` + `R9≥97` + `diluição de sombra ≥65%` + `câmera UHD` + `vida útil 10 anos`. A ETROS tem a oportunidade de ser o primeiro produto nessa posição.

**Decisões imediatas requeridas:**
1. Confirmar meta R9≥97 em todos os modelos ETROS (corrige a ferida da MENDEL 3LEV)
2. Endereçar diluição de sombra com arquitetura de múltiplos pontos de luz
3. Priorizar eficiência térmica (Ee/Ec) como argumento central de licitação vs MENDEL atual

---

## 1. OS 5 GAPS CRÍTICOS IDENTIFICADOS

### Gap 1 — R9=91 na MENDEL 3LEV: Vulnerabilidade Colorimétrica

| Indicador | MENDEL 3LEV | Mercado | Impacto |
|-----------|:-----------:|:-------:|---------|
| R9 (vermelho) | **91** ⚠️ | 96–99 | Pior índice de todo o mercado |
| Ra (geral) | 99 ✓ | 96–99 | Topo do mercado |

**O problema:** Em cirurgias de alta complexidade, o R9 baixo dificulta a distinção visual entre tecidos vasculares e estruturas adjacentes. Hospitais de referência (Sírio-Libanês, Albert Einstein, Beneficência) que avaliam KSS (R9=96), OQTIS (R9=97) ou MEDPEJ (R9=99) percebem essa diferença. A MENDEL 3LEV é atualmente vulnerável em demonstrações técnicas.

**Ação ETROS:** R9≥97 deve ser requisito não-negociável em todos os modelos — não herdar a limitação da 3LEV.

---

### Gap 2 — Diluição de Sombra: 14% vs 88% do Líder

| Fabricante | Diluição c/ 1 máscara | Arquitetura |
|------------|:--------------------:|-------------|
| MENDEL 3LEV | ~15% ⚠️ | Poucos pontos LED |
| MENDEL 4LEV | ~14% ⚠️ | Poucos pontos LED |
| KSS SKYLED 160 | 78% | Múltiplos módulos |
| OQTIS S2/S3 | **88%** ✓✓ | 48–72 LEDs distribuídos |
| MEDLIGHT Sat | 58% | Satélites integrados |

**O problema:** Em cirurgias laparoscópicas e robóticas — segmento de maior crescimento — o cirurgião, câmeras e instrumentos frequentemente interceptam o foco. Com 14% de diluição, qualquer obstáculo cria pontos cegos no campo. OQTIS usa isso ativamente em demonstrações contra MENDEL.

**Ação ETROS:** Arquitetura de LED deve garantir ≥60% de diluição de sombra. Exige redesenho da distribuição de pontos de luz na cúpula.

---

### Gap 3 — Eficiência Térmica: MENDEL gera 50% mais calor que OQTIS

| Fabricante | Ee/Ec (mW/m²lx) | Calor cabeça |
|------------|:---------------:|:------------:|
| OQTIS S2 | **1,38** ✓✓ | <1°C |
| OQTIS S3 | 1,56 ✓✓ | <1°C |
| MENDEL 4LEV | 2,19 | n/e |
| KSS 160 | 3,40 | <2°C |
| MENDEL 3LEV | **3,12** ⚠️ | n/e |

**O problema:** Em cirurgias longas (4–12h), o calor gerado pelo foco provoca desconforto, sudorese e fadiga. A MENDEL 3LEV gera 2,26× mais calor por klx do que o OQTIS S2 — e a MENDEL 4LEV ainda gera 58% mais. Em demos contra OQTIS, o argumento do conforto térmico pesa decisivamente.

**Ação ETROS:** Meta Ee/Ec ≤2,0 mW/m²lx para posicionamento diferenciado vs MENDEL atual, e aproximação ao desempenho OQTIS.

---

### Gap 4 — Câmera Integrada: Dados Ausentes na MENDEL

| Fabricante | Câmera | Resolução | Zoom |
|------------|:------:|:---------:|:----:|
| KSS | Sim | Full HD / UHD (4K) | 20–30x |
| OQTIS | Sim | Full HD / UHD | 30x |
| MEDLIGHT | Sim | 1080p / 4K opcional | n/e |
| MEDPEJ TL | **Não** ⚠️ | — | — |
| MENDEL | **A confirmar** ⚠️ | — | — |

**O problema:** Cirurgias videoassistidas representam tendência crescente no mercado hospitalar. Fabricantes sem câmera ou sem especificações técnicas declaradas perdem licitações hospitalares que exigem sistema de imageamento integrado. A ausência de dados da MENDEL impede qualquer argumento comparativo em licitações.

**Ação ETROS:** Câmera Full HD mínimo (UHD no topo de linha) deve ser feature obrigatória com especificações declaradas completas.

---

### Gap 5 — Vida Útil de LEDs: MENDEL abaixo dos líderes

| Fabricante | Vida útil LEDs | Vida útil equip. | TCO |
|------------|:--------------:|:----------------:|:---:|
| KSS | >300.000h | 10 anos | ✓✓ |
| OQTIS | >300.000h | 10 anos | ✓✓ |
| MENDEL | >226.000h | 10 anos | ✓ |
| MEDLIGHT | 200.000h | 5 anos | — |
| MEDPEJ | ≥100.000h | 5 anos | ⚠️ |

**O problema:** Em licitações públicas com análise de TCO (Custo Total de Propriedade), a vida útil dos LEDs é linha de cálculo direta. Com 226.000h vs 300.000h dos líderes, a MENDEL perde 25% em argumento de TCO — o que representa custo de manutenção e substituição mais cedo.

**Ação ETROS:** ≥300.000h posiciona a ETROS em paridade com KSS e OQTIS — e supera a própria MENDEL no argumento de TCO.

---

## 2. PERSPECTIVA: ENGENHARIA ÓPTICA

### O que os dados revelam sobre design óptico

A análise dos campos luminosos dos cinco fabricantes expõe **três filosofias de design óptico distintas**, com implicações diretas na experiência cirúrgica:

#### Filosofia A: Concentração máxima (OQTIS)
- d50/d10 = 84% no Sirius S3 — campo muito concentrado e homogêneo
- 72 LEDs distribuídos em anel → diluição de sombra de 88%
- Ee/Ec = 1,38–1,56 → dissipação de calor excepcional por design óptico
- **Conclusão:** a eficiência térmica do OQTIS não é apenas eletrônica — é consequência do design óptico: mais LEDs de menor potência individual geram o mesmo fluxo com menos calor por ponto

#### Filosofia B: Campo gradual (MEDLIGHT)
- d50/d10 = 34% — transição suave do núcleo para a periferia
- Evita o "efeito holofote" que irrita cirurgiões em procedimentos longos
- Trade-off: menor intensidade no campo periférico, exige mais ajuste de posição
- **Conclusão:** design deliberado para hospitais que valorizam conforto visual sobre intensidade máxima

#### Filosofia C: Ponto único poderoso (KSS SKYLED 65)
- Maior profundidade de campo absoluta (2.850mm a 20% de Ec)
- Porém diluição de sombra = 0 (foco único)
- **Conclusão:** excelente para cirurgias abertas com pouco instrumento, inadequado para laparoscopia

### Recomendações para Engenharia Óptica ETROS

| Parâmetro óptico | Meta mínima | Meta diferencial | Referência |
|------------------|:-----------:|:----------------:|-----------|
| Número de pontos LED | ≥24 | ≥48 | OQTIS S2 (48), S3 (72) |
| Distribuição d50/d10 | ≥55% | ≥70% | OQTIS S1 (71%), S2 (79%) |
| Profundidade @20% | ≥1.800mm | ≥2.000mm | MENDEL 4LEV atual (1.930mm) |
| Profundidade @60% | ≥700mm | ≥1.000mm | KSS 120 (1.040mm) |
| Campo ajustável | 150–350mm | 110–380mm | MEDLIGHT Apollo |
| Diluição de sombra 1 máscara | ≥60% | ≥80% | OQTIS S2/S3 (88%) |

**Insight crítico de óptica:** A diluição de sombra da MENDEL 3LEV/4LEV (14–15%) é consequência direta da arquitetura de poucos pontos de luz de alta potência. Para atingir ≥60%, é necessário redesenhar a distribuição de LEDs na cúpula — não é ajuste de firmware.

**Oportunidade de diferenciação:** Nenhum fabricante declara lux uniformidade do campo (ratio central/periférico). Publicar este dado com método de medição IEC 60601-2-41 seria diferencial técnico em licitações.

---

## 3. PERSPECTIVA: ENGENHARIA ELÉTRICA E ELETRÔNICA

### Análise de Eficiência e Sistemas de Potência

#### Eficiência energética por fabricante

| Fabricante | Modelo referência | VA | Ec máx | VA/klx | Posição |
|------------|:-----------------:|:--:|:------:|:------:|:-------:|
| MEDLIGHT | Apollo 03x03 | 30 | 90klx | **0,33** | 🥇 |
| KSS | SKYLED 160 | 70 | 160klx | 0,44 | 🥈 |
| OQTIS | Sirius S2 | ~55 | 160klx | ~0,34 | 🥇/🥈 |
| MENDEL | 4LEV | 106,5W | 160klx | **0,67** | 🥉 |
| MEDPEJ | TLMx máx | 130 | 160klx | 0,81 | — |

**Problema técnico de MENDEL:** consumo de 0,63–0,67 VA/klx vs 0,44 da KSS implica ~52% mais consumo para a mesma iluminância. Em hospitais com centros cirúrgicos de 10–20 salas operando 8–12h/dia, isso representa custo elétrico diferencial relevante.

**Meta ETROS:** ≤0,50 VA/klx. Atingível com LEDs de maior eficiência luminosa (lm/W) e driver com potência fatorada.

#### Sistemas de emergência (backup de energia)

A análise revelou diferença tecnológica significativa entre fabricantes:

| Tecnologia | Fabricantes | Vantagens | Desvantagens |
|------------|-------------|-----------|--------------|
| Chumbo-ácido VRLA | KSS, OQTIS, MEDLIGHT | Barato, maduro | Peso, degradação, vida 3–5 anos |
| Li-FePO4 | **MEDPEJ (único)** | Vida >2000 ciclos, 1/3 do peso, sem efeito memória | Custo maior |
| Integrada declarada | MENDEL | Determinístico para licitações (8h/6h) | Dados de tecnologia não declarados |

**Oportunidade:** ETROS como 2º fabricante a oferecer Li-FePO4 posiciona a linha como tecnologicamente superior. O custo adicional do Li-FePO4 é recuperado em 3–4 anos pela menor taxa de substituição de bateria.

#### Controle sem fio — análise técnica

| Fabricante | Protocolo | Distância | Peso manopla | Specs licitação |
|------------|:---------:|:---------:|:------------:|:---------------:|
| KSS | **433MHz** | 0,4–4m | 170g | ✓ Completas |
| OQTIS | Sim | n/e | n/e | Parcial |
| MENDEL | A confirmar | n/e | n/e | — |

**Insight:** KSS detalha o controle sem fio com especificações completas (frequência, alcance, peso) — o que viabiliza inclusão como item técnico em editais de licitação pública. ETROS deve seguir este padrão de documentação.

#### Proteção e construção

Todos os fabricantes utilizam **IP54** na cúpula — proteção equivalente. A diferença está na manopla:
- KSS e OQTIS: manopla de **alumínio** (>500 ciclos autoclave) — diferencial de durabilidade
- MENDEL, MEDPEJ: apenas polímero/silicone (~300 ciclos)
- ETROS: oferecer alumínio como opção premium é melhoria de percepção de qualidade imediata

---

## 4. PERSPECTIVA: PRODUTO E ESTRATÉGIA

### Análise de Posicionamento Competitivo

#### Mapa de posicionamento atual

```
              ALTA EFICIÊNCIA TÉRMICA (Ee/Ec baixo)
                         ↑
                    [OQTIS]
                      ●●●●●
                         |
 BAIXA     ─────────────────────────── ALTA
 COLORIMETRIA             |        COLORIMETRIA
 (Ra/R9)   [KSS]  [MENDEL]  [MEDPEJ]
              ●     ●●●●     ●●●●●
                    |ETROS?|
                    ↓
              BAIXA EFICIÊNCIA TÉRMICA
```

**Posição estratégica recomendada para ETROS:**
Ocupar o quadrante **Alta Colorimetria + Alta Eficiência Térmica** — posição hoje vaga no mercado nacional.

#### Análise de segmentos de cliente

| Segmento | Critério principal | Vantagem atual | Oportunidade ETROS |
|----------|------------------:|:--------------:|:------------------:|
| Hospitais privados de alta complexidade | Ra/R9, câmera, TCO | MEDPEJ/MEDLIGHT | Combinar colorimetria + vida útil 10 anos |
| Hospitais públicos (licitação) | TCO, conformidade ANVISA, specs técnicas | KSS | Superar em eficiência energética + specs detalhadas |
| Clínicas e hospitais médios | Custo, robustez, suporte | MENDEL atual | Linha ETROS entrada a preço competitivo |
| Centros de cirurgia robótica/laparoscópica | Diluição sombra, câmera UHD, conforto térmico | OQTIS | Meta de longo prazo: igualar eficiência térmica |

#### Análise de TCO (5 anos) — exemplo ilustrativo

| Item de custo | MENDEL atual | ETROS (meta) | Economia |
|---------------|:------------:|:------------:|:--------:|
| Consumo elétrico (0,67 vs 0,50 VA/klx) | Base 100% | ~75% | -25% |
| Reposição de bateria (VRLA 3–5 anos vs Li-FePO4) | 2× troca | 1× troca | -50% bateria |
| Reposição de manopla (polímero vs Al) | Frequente | Reduzida | -30% manopla |
| Vida útil LEDs (226kh vs 300kh) | Troca em ~15 anos | Troca em ~20 anos | TCO favorável |

**Argumento de venda:** "A ETROS custa X% a mais que a linha MENDEL atual, mas o TCO em 5 anos é Y% menor" — argumento poderoso em licitações.

---

## 5. ROADMAP INTEGRADO MENDEL (CURTO PRAZO) + ETROS (MÉDIO PRAZO)

### Fase 1: Ações Imediatas na Linha MENDEL — Q1/Q2 2026

Antes do lançamento da ETROS, há correções urgentes que podem ser feitas na linha MENDEL existente:

| Ação | Impacto | Esforço | Prazo |
|------|:-------:|:-------:|:-----:|
| Investigar R9=91 da MENDEL 3LEV (firmware ou hardware?) | Alto | Baixo | 30 dias |
| Levantar e documentar specs da câmera MENDEL | Alto | Baixo | 15 dias |
| Documentar controle sem fio MENDEL (protocolo, distância, peso) | Alto | Baixo | 15 dias |
| Preencher dados de emergência (autonomia, tecnologia bateria) | Médio | Baixo | 15 dias |
| Declarar Ee/Ec da linha MENDEL nos documentos técnicos | Médio | Baixo | 30 dias |
| Avaliar manopla de alumínio como acessório opcional | Médio | Médio | 60 dias |

> **Nota:** As ações de documentação (specs câmera, controle sem fio, emergência) têm custo próximo de zero e eliminam imediatamente lacunas em licitações.

### Fase 2: Desenvolvimento ETROS — Q3/Q4 2026

#### Módulo 1: Óptica (must-have para lançamento)
- [ ] Redesenhar distribuição de LEDs para diluição de sombra ≥60%
- [ ] Validar d50/d10 ≥65% (meta: 75%)
- [ ] Garantir profundidade de campo ≥1.800mm a 20% de Ec
- [ ] Atingir e homologar Ra≥99 + R9≥97 em todos os modelos

#### Módulo 2: Eficiência energética e térmica (must-have)
- [ ] Driver LED com eficiência ≤0,50 VA/klx (meta: 0,45)
- [ ] Dissipação térmica para Ee/Ec ≤2,0 mW/m²lx
- [ ] Documentar e publicar Ee/Ec no manual técnico

#### Módulo 3: Sistemas integrados (diferencial competitivo)
- [ ] Câmera Full HD integrada padrão (meta: UHD no topo de linha)
- [ ] Zoom óptico ≥20x (meta: 30x para paridade com OQTIS)
- [ ] Controle sem fio com specs completas para licitação
- [ ] Temperatura de cor ajustável 3000–6700K

#### Módulo 4: Durabilidade e TCO (diferencial de licitação)
- [ ] LEDs ≥300.000h (homologados)
- [ ] Garantia equipamento 10 anos
- [ ] Bateria de emergência ≥8h com opção Li-FePO4
- [ ] Manopla de alumínio como opção (meta: padrão no topo de linha)

### Fase 3: Go-to-Market ETROS — Q1 2027

| Segmento-alvo inicial | Argumento principal | Concorrente a deslocar |
|-----------------------|--------------------:|:----------------------:|
| Hospitais privados SP/RJ | Ra/R9=99 + vida útil 10 anos + câmera UHD | MEDPEJ (sem câmera) |
| Licitações públicas | TCO + specs detalhadas + ANVISA | KSS (Ra=96) |
| Cirurgias robóticas | Diluição sombra ≥65% + câmera UHD | OQTIS (Ra=98) |

---

## 6. MATRIZ DE PRIORIZAÇÃO — IMPACTO × ESFORÇO

### Para a linha MENDEL (ações imediatas)

| Ação | Impacto | Esforço | Quadrante | Prioridade |
|------|:-------:|:-------:|:---------:|:----------:|
| Documentar specs câmera MENDEL | Alto | **Baixo** | Quick Win | **P1** |
| Documentar controle sem fio MENDEL | Alto | **Baixo** | Quick Win | **P1** |
| Investigar R9=91 (firmware?) | Alto | Baixo | Quick Win | **P1** |
| Declarar Ee/Ec nos docs técnicos | Médio | **Baixo** | Quick Win | **P1** |
| Incluir BARRFAB na análise | Baixo | Baixo | Preencher | P3 |
| Manopla alumínio MENDEL opcional | Médio | Médio | Considerar | P2 |

### Para a linha ETROS (desenvolvimento)

| Feature | Impacto | Esforço | Quadrante | Prioridade |
|---------|:-------:|:-------:|:---------:|:----------:|
| R9≥97 todos os modelos | **Crítico** | Médio | Estratégico | **P1** |
| Diluição de sombra ≥60% | **Crítico** | Alto | Estratégico | **P1** |
| Câmera Full HD integrada | Alto | Médio | Must-have | **P1** |
| Eficiência energética ≤0,50 VA/klx | Alto | Médio | Must-have | **P1** |
| Ee/Ec ≤2,0 mW/m²lx | Alto | Alto | Estratégico | **P2** |
| LEDs ≥300.000h | Alto | Médio | Must-have | **P2** |
| Controle sem fio documentado | Médio | Baixo | Quick Win | **P1** |
| Bateria Li-FePO4 (opção) | Médio | Médio | Diferencial | **P2** |
| Câmera UHD 30x zoom | Médio | Alto | Premium | **P3** |
| Manopla alumínio padrão | Baixo | Baixo | Quick Win | **P2** |

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

## 7. CONCLUSÃO — SÍNTESE DOS ESPECIALISTAS

### O que a ETROS precisa ser no dia 1 do lançamento:

> Uma cúpula cirúrgica que corrija **todas** as fraquezas da linha MENDEL atual e iguale os líderes técnicos em cada dimensão crítica — sem ser inferior a nenhum concorrente em nenhuma dimensão relevante.

**Checklist mínimo para lançamento competitivo:**

- [ ] Ra=99 + R9≥97 em todos os modelos (sem exceção)
- [ ] Diluição de sombra ≥60% (supera MENDEL atual que tem 14%)
- [ ] Eficiência energética ≤0,50 VA/klx (supera MENDEL: 0,63–0,67)
- [ ] Ee/Ec declarado e ≤2,5 (posiciona vs OQTIS com argumento técnico)
- [ ] Câmera integrada Full HD com specs documentadas
- [ ] Controle sem fio com protocolo, distância e peso declarados
- [ ] LEDs ≥300.000h documentados
- [ ] Vida útil equipamento 10 anos
- [ ] Bateria ≥8h de autonomia declarada

**Posicionamento de mercado recomendado:**

> _"ETROS — Tecnologia Cirúrgica Completa: máxima fidelidade de cor, mínimo calor, visibilidade irrestrita"_

---

## APÊNDICE — DADOS TÉCNICOS DE REFERÊNCIA

### Comparativo rápido — todos os fabricantes

| Dimensão | KSS | MEDLIGHT | OQTIS | MEDPEJ | MENDEL | **ETROS meta** |
|----------|:---:|:--------:|:-----:|:------:|:------:|:--------------:|
| Ec máx (klx) | 160 | 160 | 160 | 160 | 160 | **160** |
| Ra | 96 | 98–99 | 98 | 99 | 99 | **≥99** |
| R9 | 96–97 | 97–99 | 97 | 99 | 91–97 | **≥97** |
| Ee/Ec (mW/m²lx) | 3,1–3,4 | ~3,0–3,2 | **1,38–1,73** | ≤3,8 | 2,19–3,12 | **≤2,0** |
| Diluição sombra | 0–78% | 58% | **88%** | 58% | 14–15% | **≥65%** |
| Prof campo @20% | 1.332–2.850mm | ~1.800mm | **2.500mm** | 500–1.500mm | 1.360–1.930mm | **≥1.800mm** |
| Vida LEDs | >300kh | 200kh | >300kh | ≥100kh | >226kh | **≥300kh** |
| Vida equip. | 10 anos | 5 anos | 10 anos | 5 anos | 10 anos | **10 anos** |
| Câmera | UHD | 4K opt. | UHD | ✗ | ? | **Full HD/UHD** |
| Bateria moderna | VRLA | VRLA | VRLA | **Li-FePO4** | — | **Li-FePO4 opt.** |
| VA/klx | 0,44–0,58 | **0,33–0,50** | ~0,34–0,45 | 0,60–0,87 | 0,63–0,67 | **≤0,50** |

---

*Documento gerado em 2026-02-25 | Projeto: Inteligência Competitiva Mendel Medical / ETROS | Roadmap Estratégico — Direção e Engenharia*
