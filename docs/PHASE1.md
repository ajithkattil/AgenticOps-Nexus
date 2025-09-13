### This is the README file for Phase 1

# AgenticOps Nexus — Phase 1: User Management (FastAPI)

## 🔹 Overview
**AgenticOps Nexus** begins with a **User Management microservice** built in **FastAPI**.  

Phase 1 focuses on learning and applying:
- FastAPI fundamentals (routing, validation, auto-docs).
- Pydantic models (input/output validation).
- SQLModel (database models with Postgres).
- Authentication (secure password hashing + JWT).
- Testing with `pytest` and FastAPI’s TestClient.
- Tooling (Makefile, Docker Compose, Ruff, MyPy).

Later phases will extend this into log ingestion, agentic workflows, and DevOps/AI insights.

---

## 🔹 Features
- Register a new user (`POST /api/v1/users/register`).
- Login with username/password to get a JWT (`POST /api/v1/users/login`).
- Get current user info via JWT (`GET /api/v1/users/me`).
- Health check (`GET /healthz`).
- Password hashing with bcrypt.
- JWT authentication for protected endpoints.
- Auto-generated API docs (Swagger/OpenAPI).

---

## 🔹 Project Structure
```
agenticops-nexus/
├─ README.md
├─ requirements.txt
├─ docker-compose.yml
├─ .env.example
├─ .gitignore
├─ Makefile
├─ pyproject.toml
├─ services/
│  └─ users/
│     └─ app/
│        ├─ main.py       # FastAPI app
│        ├─ models.py     # SQLModel User table
│        ├─ schemas.py    # Pydantic request/response schemas
│        ├─ auth.py       # Hashing + JWT helpers
│        ├─ db.py         # DB session + init
│        └─ __init__.py
└─ tests/
   └─ test_users.py
```

---

## 🔹 Requirements
- Python 3.11+
- Docker & Docker Compose
- Virtual environment (venv or conda)

---

## 🔹 Setup

### 1. Clone & create virtual environment
```bash
git clone https://github.com/<your-org>/agenticops-nexus.git
cd agenticops-nexus
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment
```bash
cp .env.example .env
```

`.env` example:
```env
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/agenticops
JWT_SECRET=change-me-in-prod
JWT_ALG=HS256
JWT_EXPIRE_MIN=60
```

### 4. Start Postgres with Docker
```bash
docker compose up -d db
```

### 5. Initialize database
```bash
make db-init
```

### 6. Run the service
```bash
make run-users
```

Visit:
- Swagger UI → http://127.0.0.1:8001/docs
- Health check → http://127.0.0.1:8001/healthz

---

## 🔹 Example Usage

### Register a new user
```bash
curl -X POST http://127.0.0.1:8001/api/v1/users/register   -H "Content-Type: application/json"   -d '{"username":"ajith","email":"ajith@example.com","password":"Secret123!"}'
```

### Login to get JWT
```bash
curl -X POST "http://127.0.0.1:8001/api/v1/users/login?username=ajith&password=Secret123!"
# => {"access_token":"<JWT>","token_type":"bearer"}
```

### Access current user info
```bash
TOKEN=<paste_JWT_here>
curl http://127.0.0.1:8001/api/v1/users/me -H "Authorization: Bearer $TOKEN"
```

---

## 🔹 Running Tests

### Run with Make
```bash
make test
```

### Or directly with pytest
```bash
PYTHONPATH=. pytest -q
```

Tests cover:
- Successful registration
- Duplicate username error
- Successful login
- Invalid credentials
- Protected `/me` endpoint with JWT

---

## 🔹 Tooling

- **Linting**
  ```bash
  make lint
  ```
- **Type checks**
  ```bash
  mypy services/
  ```

---

## 🔹 Learning Notes
- FastAPI routes use decorators like `@app.post("/path")`.
- Pydantic validates request data automatically (e.g., `EmailStr` rejects invalid emails).
- SQLModel defines tables and auto-creates schema.
- Passwords are stored only as bcrypt hashes.
- JWT tokens are issued on login and passed as `Authorization: Bearer <token>`.
- Swagger/OpenAPI docs are auto-generated at `/docs`.
- Tests use FastAPI’s `TestClient` to simulate requests without running a server.

---

## 🔹 Roadmap
- **Phase 1 (now):** User Management microservice.
- **Phase 2:** Log ingestion service (file uploads, metadata storage).
- **Phase 3:** Agent Orchestrator (LangGraph agentic flows).
- **Phase 4:** Insights service (reports, dashboards).
- **Phase 5:** Full Ops Nexus (multi-service hub with RBAC & observability).

---

✅ You’ve completed **Phase 1**: a working FastAPI service with secure user management, tests, and CI/CD-ready structure.

