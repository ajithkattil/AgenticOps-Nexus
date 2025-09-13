from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import Session, select
from .db import get_session
from .models import User
from .schemas import UserCreate, UserRead, Token, LoginRequest
from .auth import hash_password, verify_password, create_token, get_subject

app = FastAPI(title="AgenticOps Nexus - User Service")

# ---- Root & health ----
@app.get("/")
def root():
    return {"message": "AgenticOps Nexus - User Service is running", "docs": "/docs"}

@app.get("/healthz")
def health():
    return {"status": "ok"}

# ---- Auth & users ----
@app.post("/api/v1/users/register", response_model=UserRead, status_code=201)
def register(payload: UserCreate, session: Session = Depends(get_session)):
    exists = session.exec(select(User).where(User.username == payload.username)).first()
    if exists:
        raise HTTPException(status_code=400, detail="Username already exists")
    user = User(
        username=payload.username,
        email=payload.email,
        password_hash=hash_password(payload.password),
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@app.post("/api/v1/users/login", response_model=Token)
def login(payload: LoginRequest, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.username == payload.username)).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return {"access_token": create_token(user.username), "token_type": "bearer"}

@app.get("/api/v1/users/me", response_model=UserRead)
def me(sub: str = Depends(get_subject), session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.username == sub)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
