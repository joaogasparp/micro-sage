# Inventory Service – MicroSage

Este microserviço gere o inventário de produtos disponíveis.

## Endpoints

- `POST   /items/`     – Criar item novo
- `GET    /items/`     – Listar todos os produtos
- `GET    /items/{id}` – Obter detalhes de um item
- `PUT    /items/{id}` – Atualizar stock ou dados
- `DELETE /items/{id}` – Remover item

## Como rodar localmente

1. **Build e start:**
   ```bash
   docker compose up --build
   ```
2. Acesse a API em: [http://localhost:8001/docs](http://localhost:8001/docs)

## Estrutura

- `app/api/`      – Rotas FastAPI e schemas
- `app/core/`     – Configuração
- `app/db/`       – Modelos, CRUD e sessão

---

> Microserviço de inventário do projeto MicroSage.
