# Billing Service – MicroSage

Este microserviço simula o processamento de pagamentos e emissão de faturas.

## Endpoints

- `POST   /payments/`     – Criar pagamento
- `GET    /payments/`     – Listar pagamentos
- `GET    /payments/{id}` – Obter estado de pagamento
- `PUT    /payments/{id}` – Atualizar status
- `POST   /invoices/`     – Gerar fatura

## Como rodar localmente

1. **Build e start:**
   ```bash
   docker compose up --build
   ```
2. Acesse a API em: [http://localhost:8002/docs](http://localhost:8002/docs)

## Estrutura

- `app/api/`      – Rotas FastAPI e schemas
- `app/core/`     – Configuração
- `app/db/`       – Modelos, CRUD e sessão

---

> Microserviço de faturação do projeto MicroSage.
