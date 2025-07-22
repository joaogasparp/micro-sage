# Order Service – MicroSage

Este microserviço é responsável pela criação e gestão de pedidos.

## Endpoints

- `POST   /orders/`     – Criar novo pedido
- `GET    /orders/`     – Listar todos os pedidos
- `GET    /orders/{id}` – Obter pedido por ID
- `PUT    /orders/{id}` – Atualizar status do pedido
- `DELETE /orders/{id}` – Remover pedido

## Como rodar localmente

1. **Build e start:**
   ```bash
   docker-compose up --build
   ```
2. Acesse a API em: [http://localhost:8000/docs](http://localhost:8000/docs)

## Migrações

1. Entre no container:
   ```bash
   docker-compose exec order-service bash
   ```
2. Rode as migrações:
   ```bash
   alembic upgrade head
   ```

## Estrutura

- `app/api/`      – Rotas FastAPI
- `app/models/`   – Modelos SQLAlchemy
- `app/schemas/`  – Schemas Pydantic
- `app/services/` – Lógica de negócio
- `app/db/`       – Sessão e base ORM

---

> Projeto inicial da arquitetura MicroSage. Para dúvidas, consulte a documentação ou abra uma issue.
