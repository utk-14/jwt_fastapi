#config.py
from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    # database related
    db_host: str
    db_port: int
    db_name: str
    db_pwd: str
    db_usr: str
    port: str
    
    # JWT Token Related
    secret_key: str
    refresh_secret_key : str
    algorithm: str
    timeout: int
    ACCESS_TOKEN_EXPIRE_MINUTES : int
    REFRESH_TOKEN_EXPIRE_MINUTES : int

    # internal env
    adminapikey: str

    SERVER: str

    class Config:
        env_file = Path(Path(__file__).resolve().parent) / ".env"
        print(f'environment created - {Path(Path(__file__).resolve().name)}')



setting = Settings()



# config.py is responsible for loading environment variables and providing a centralized settings object for the project.

# It reads all sensitive info (DB credentials, JWT secrets, token expiry times, server info) from a .env file.

# Makes it easy to access these settings anywhere via setting.

# Helps avoid hardcoding secrets in your code