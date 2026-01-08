from fastapi import FastAPI
from db import Base, engine
from routes.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Reusable JWT Auth")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])



#main.py is the entry point of your FastAPI app — it:

# Creates the FastAPI instance (app = FastAPI()).

# Connects and registers routes (like /auth/register and /auth/login).

# Optionally includes middleware, event handlers, or startup/shutdown logic.