from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import setting

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{setting.db_usr}:{setting.db_pwd}"
    f"@{setting.db_host}:{setting.db_port}/{setting.db_name}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# db.py is responsible for database connection and session management. It:

# Builds the database URL using credentials from config.py.

# Creates the SQLAlchemy engine to connect to PostgreSQL.

# Sets up a session factory (SessionLocal) to interact with the DB.

# Provides a dependency (get_db) to get a session in your routes.

# Exposes Base so tables in models.py can be created