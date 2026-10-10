from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# PSqlite for development, but we will change this to PostgreSQL when we deploy to production
#TODO change this to PostgreSQL when we deploy to production
SQLALCHEMY_DATABASE_URL = "sqlite:///./growth.db"

# Si estuviéramos usando PostgreSQL, la línea sería algo así:
# SQLALCHEMY_DATABASE_URL = "postgresql://growth_user:growth_pass@localhost/growth_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} # Esto último es solo para SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependencia para inyectar la sesión de la base de datos en nuestras rutas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()