from datetime import datetime, timedelta
from typing import Union, Any, Optional
from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError, ExpiredSignatureError
from config import setting

def create_access_token(subject: Union[str, Any]):
    expire = datetime.utcnow() + timedelta(minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"exp": expire, "sub": str(subject)}
    return jwt.encode(payload, setting.secret_key, algorithm=setting.algorithm)

def create_refresh_token(subject: Union[str, Any]):
    expire = datetime.utcnow() + timedelta(minutes=setting.REFRESH_TOKEN_EXPIRE_MINUTES)
    payload = {"exp": expire, "sub": str(subject)}
    return jwt.encode(payload, setting.refresh_secret_key, algorithm=setting.algorithm)

def decode_jwt(token: str):
    try:
        return jwt.decode(token, setting.secret_key, algorithms=[setting.algorithm])
    except JWTError:
        return None

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request) -> Optional[str]:
        creds: HTTPAuthorizationCredentials = await super().__call__(request)
        if creds.scheme != "Bearer":
            raise HTTPException(status_code=403, detail="Invalid scheme")
        if not decode_jwt(creds.credentials):
            raise HTTPException(status_code=403, detail="Invalid or expired token")
        return creds.credentials



# Handles JWT token creation, decoding, and authentication.

# Generates access and refresh tokens.

# Decodes JWT to validate it.

# Provides JWTBearer class to protect routes.