import os
os.environ["DATABASE_URL"] = "sqlite:///./test.db"  # isolate tests

from fastapi.testclient import TestClient
from services.users.app.main import app
from services.users.app.db import init_db

client = TestClient(app)
init_db()

def test_register_and_login_and_me():
    # register
    r = client.post("/api/v1/users/register", json={
        "username": "ajith",
        "email": "ajith@example.com",
        "password": "Secret123!"
    })
    assert r.status_code == 201
    data = r.json()
    assert data["username"] == "ajith"
    assert data["email"] == "ajith@example.com"

    # duplicate
    r2 = client.post("/api/v1/users/register", json={
        "username": "ajith",
        "email": "ajith@example.com",
        "password": "Secret123!"
    })
    assert r2.status_code == 400

    # login
    r3 = client.post("/api/v1/users/login?username=ajith&password=Secret123!")
    assert r3.status_code == 200
    token = r3.json()["access_token"]

    # me
    r4 = client.get("/api/v1/users/me", headers={"Authorization": f"Bearer {token}"})
    assert r4.status_code == 200
    me = r4.json()
    assert me["username"] == "ajith"
    assert me["email"] == "ajith@example.com"
