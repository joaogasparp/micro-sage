# Logger Service – MicroSage

Este microserviço centraliza e armazena logs enviados pelos outros serviços.

## Endpoints

- `POST /logs/`       – Registar novo log
- `GET /logs/`        – Listar logs (paginação)
- `GET /logs/search`  – Filtrar logs por nível, origem, data

## Como rodar localmente

1. **Build e start:**
   ```bash
   docker compose up --build
   ```
2. Acesse a API em: [http://localhost:8004/docs](http://localhost:8004/docs)

## Estrutura

- `app/api/`      – Rotas FastAPI e schemas
- `app/core/`     – Configuração
- `app/logs/`     – Manipulação de logs
- `logs_storage/` – Armazenamento local dos logs

---

> Microserviço de logging centralizado do projeto MicroSage.
