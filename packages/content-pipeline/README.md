# Salk Content Studio v2.0

Sistema de producao de conteudo para redes sociais do Manager Grupo.

## Requisitos

- Python 3.11+
- pip

## Instalacao Local

```bash
cd packages/content-pipeline
pip install -r requirements.txt
```

## Execucao

```bash
# Desenvolvimento
python -m uvicorn content_pipeline.web.app:app --reload --host 0.0.0.0 --port 8000

# Producao
python -m uvicorn content_pipeline.web.app:app --host 0.0.0.0 --port 8000 --workers 2
```

Acesse: http://localhost:8000

## Docker

```bash
# Build e run
docker-compose up -d

# Ver logs
docker-compose logs -f

# Parar
docker-compose down
```

## Configuracao

Apos iniciar, acesse **Configuracoes** no menu lateral para definir:

1. **OPENROUTER_API_KEY** — Geracao de copy (obrigatorio)
2. **FAL_API_KEY** — Geracao de imagens NB2 (obrigatorio)
3. **ELEVENLABS_API_KEY** — Narracao de video (opcional)
4. **MINIMAX_API_KEY** — Animacao de video (opcional)

## Health Check

```bash
curl http://localhost:8000/api/health
```

## Estrutura

```
src/content_pipeline/
├── web/           # FastAPI app, auth, database, static files
├── automation/    # Auto-briefing, copywriter, NB2 prompts, image gen
├── api/           # Gemini client
├── nb2/           # NB2 engine, prompt builder
├── llm/           # OpenRouter client, budget tracker
├── video/         # Kling, Minimax, Veo3, TTS, FFmpeg
├── publishers/    # Instagram, LinkedIn, Facebook, YouTube
└── pipeline/      # Orchestration
```

## Marcas

| Marca | Tema | Foco |
|-------|------|------|
| Salk Medical | Azul | Comercial, vendas |
| Mendel Medical | Verde | Autoridade tecnica |
| Manager Grupo | Roxo | Institucional |
| Dayho | Laranja | Industrial |

## Licenca

Proprietario — Manager Grupo / Synkra Consultoria
