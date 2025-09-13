# AgenticOps Nexus — User Management (FastAPI)

**AgenticOps Nexus** is a learning-first, production-lean scaffold to master **FastAPI** using a real **User Management** use case (register → login → JWT → `/me`).  
This Phase-1 service is the foundation we’ll later extend into Agentic AI microservices (ingestion, orchestrator, insights).

## What we will learn
- FastAPI app structure (routers, dependencies, responses).
- Pydantic (request/response models, validation).
- SQLModel/SQLAlchemy (models, sessions) with PostgreSQL.
- AuthN basics: password hashing (bcrypt) + JWT (OAuth2 Password flow).
- Swagger UI & OpenAPI.
- Testing endpoints with `pytest` + `httpx`.
- Running with Uvicorn, Dockering the service.

---

## Endpoints (Phase 1 – User Management)
- `GET /healthz` — liveness
- `POST /api/v1/users/register` — create user (body: `UserCreate`)
- `POST /api/v1/users/login` — issue JWT (query: `username`, `password`)
- `GET /api/v1/users/me` — current user (requires `Authorization: Bearer <JWT>`)

**Request/Response models**
- **UserCreate**: `{ username, email, password }`
- **UserRead**: `{ id, username, email }`
- **Token**: `{ access_token, token_type }`

---
We are maintaining the README for different phases under the folder docs