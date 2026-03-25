# Task: Atomizar Peça-Mãe em Derivados Cross-Platform

**Agent:** Nova (content-atomizer)
**Command:** `*atomize-master-piece`
**Type:** recurring
**PRD:** FR-005
**Depends on:** `create-visual-delivery-pack.md` (visual pronta)

---

## Objetivo

Transformar uma peça-mãe (master piece) em 10-20 derivados nativos para cada plataforma ativa da marca. Cada derivado é ADAPTADO (nunca copiado) — copy, formato, tom, dimensão e CTA são nativos da plataforma destino.

## Pre-Conditions

- [ ] Peça-mãe finalizada (copy + visual aprovados)
- [ ] `data/platform-specs.yaml` disponível
- [ ] `data/claims-bank.yaml` disponível (mesmos claims em derivados)
- [ ] `data/hashtag-bank.yaml` disponível

## Inputs

| Input | Fonte | Obrigatório |
|-------|-------|:-----------:|
| Peça-mãe (copy + visual) | Helix + Apex | Sim |
| Brief original | Atlas | Sim |
| Platform specs | `data/platform-specs.yaml` | Sim |

## Steps

1. **Analisar peça-mãe:**
   - Identificar tipo (carousel, post, reel, vídeo, etc.)
   - Listar claims utilizados (IDs)
   - Identificar mensagem-core e elementos reutilizáveis

2. **Mapear derivados por plataforma:**

   Exemplo para carousel Instagram (peça-mãe):
   | # | Plataforma | Formato | Adaptação |
   |---|-----------|---------|-----------|
   | 1 | LinkedIn | PDF Carousel | Versão técnica expandida (8/10) |
   | 2 | LinkedIn | Texto longo | 1 insight por claim principal |
   | 3 | LinkedIn | Post + imagem | Highlight de 1 spec |
   | 4 | Instagram Reels | Reel 15-30s | Hook visual + benefício principal |
   | 5 | Instagram Stories | Story enquete | Pergunta sobre o tema |
   | 6 | Instagram Stories | Story quiz | Quiz com spec do produto |
   | 7 | YouTube Shorts | Short 30-60s | Demo condensada |
   | 8 | Facebook | Post + imagem | Versão conversacional |
   | 9 | Facebook | Vídeo curto | Adaptação do Reel |
   | 10 | Email | Newsletter snippet | Resumo + CTA |

3. **Para cada derivado, adaptar:**
   - **Copy:** Reescrever no tom da plataforma (LI=técnico 8/10, IG=visual 5/10, FB=conversacional 4/10)
   - **Dimensões:** Conforme `platform-specs.yaml`
   - **CTA:** Nativo da plataforma (IG: link na bio, LI: comente FICHA, YT: inscreva-se)
   - **Hashtags:** Do `hashtag-bank.yaml`, quantidade por plataforma
   - **Claims:** Mesmos IDs da peça-mãe (consistência)

4. **Gerar instruções visuais para cada derivado:**
   - Resize/crop necessário
   - Texto overlay a ajustar
   - Template Canva a usar

5. **Validação:**
   - [ ] ≥ 10 derivados planejados?
   - [ ] Cada plataforma ativa da marca tem ≥ 1 derivado?
   - [ ] Nenhum derivado é cópia idêntica de outro?
   - [ ] Claims consistentes (mesmos IDs)?
   - [ ] CTAs diferenciados por plataforma?
   - [ ] Dimensões corretas?

## Output

```
=== ATOMIZATION MAP — {Brief ID} ===

Peça-mãe: {tipo} — {plataforma original}
Claims: [{IDs}]
Total derivados: {N}

| # | Plataforma | Formato | Dimensão | Tom | CTA | Status |
|---|-----------|---------|----------|-----|-----|--------|
| 1 | LinkedIn | PDF Carousel | 1080x1080 | Técnico 8/10 | Comente FICHA | Pendente |
...

--- Derivado 1: LinkedIn PDF Carousel ---
Copy: "..."
Slides: [título por slide]
Instruções visuais: "Exportar carousel original em 1:1, adicionar dados técnicos detalhados"
```

## Post-Conditions

- Mapa de atomização completo
- Derivados prontos para execução pelo usuário (Canva resize + adaptação)
- Prontos para `*review-batch-editorial` (Lens) → `*review-batch-compliance` (Shield)

## Error Handling

- Se peça-mãe é muito simples para 10+ derivados → Mínimo 5 derivados aceito para posts simples
- Se plataforma não está ativa para a marca → Pular (ex: Dayho não tem YouTube)
