
# MicroSage - Backend Microservices Architecture

MicroSage is a backend project that simulates a distributed microservices architecture, ideal for enterprise environments, e-commerce, or scalable systems. Each service is independent, containerized with Docker, and communicates via RESTful APIs.

## Purpose

Demonstrate practices in DevOps, scalability, modularity, and service integration, using technologies like FastAPI, PostgreSQL, Docker, and API Gateway.

## Technologies
- Python (FastAPI)
- PostgreSQL
- SQLAlchemy & Alembic
- Docker & Docker Compose
- httpx (proxy/gateway)

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/joaogasparp/micro-sage.git
   cd micro-sage
   ```
2. Build and start all services:
   ```bash
   docker compose up --build
   ```
3. Access the services on the indicated ports or via the API Gateway (`localhost:8080`).

## Service Structure

- **order-service** (8001): Order management
- **inventory-service** (8002): Inventory management
- **billing-service** (8003): Payments and invoices
- **notification-service** (8004): System notifications
- **logger-service** (8005): Centralized logging
- **api-gateway** (8080): Single entry point, proxy, and authentication

Each service has its own folder, database (when necessary), and automatic documentation via Swagger (`/docs`).
