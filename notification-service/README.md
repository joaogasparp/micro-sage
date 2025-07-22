# Notification Service – MicroSage

Este microserviço simula o envio de notificações (email, sms, eventos).

## Endpoints

- `POST /notify/email` – Simula envio de email
- `POST /notify/sms`   – Simula envio de SMS
- `POST /notify/event` – Notificação genérica

## Como rodar localmente

1. **Build e start:**
   ```bash
   docker compose up --build
   ```
2. Acesse a API em: [http://localhost:8003/docs](http://localhost:8003/docs)

## Estrutura

- `app/api/`      – Rotas FastAPI
- `app/core/`     – Configuração
- `app/services/` – Lógica de notificação

---

> Microserviço de notificações do projeto MicroSage.
