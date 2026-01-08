#schemas.py defines Pydantic models to validate and structure the data sent to or returned from the API (like user input or API responses).
#whenever a client sends data (like registration info) or your API sends a response (like a token), Pydantic schemas in schemas.py enforce the structure and type.
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
