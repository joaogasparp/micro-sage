# API Gateway – MicroSage

Este serviço centraliza e encaminha requests para os microserviços internos.

## Endpoints

- `POST /orders/`             – Proxy para order-service
- `GET /inventory/{item_id}`  – Proxy para inventory-service
- `POST /billing/pay`         – Proxy para billing-service
- `POST /notify/email`        – Proxy para notification-service
- `POST /logs/`               – Proxy para logger-service

## Como rodar localmente

1. **Build e start:**
   ```bash
   docker compose up --build
   ```
2. Acesse a API em: [http://localhost:8080/docs](http://localhost:8080/docs)

## Estrutura

- `app/routes/` – Rotas de proxy
- `app/core/`   – Configuração

---

> API Gateway do projeto MicroSage.
