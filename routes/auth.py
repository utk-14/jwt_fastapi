from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db import get_db
from models import User
from schemas import UserCreate, UserLogin, TokenResponse
from utils.password import secure_pwd, verify_pwd
from utils.auth import create_access_token, create_refresh_token, JWTBearer

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="User exists")

    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=secure_pwd(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"msg": "User created"}

@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_pwd(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "access_token": create_access_token(db_user.id),
        "refresh_token": create_refresh_token(db_user.id),
    }

@router.get("/protected", dependencies=[Depends(JWTBearer())])
def protected():
    return {"msg": "JWT is valid"}



# This is the FastAPI router for authentication endpoints like register and login. It connects schemas, utils, and DB.