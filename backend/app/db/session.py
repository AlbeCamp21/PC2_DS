from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL_LOCAL")

class DatabaseSingleton:
    _instance = None

    def __new__(cls):
        # Instancia patron de diseño singleton
        if cls._instance is None:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
            cls._instance._engine = create_engine(DATABASE_URL)
            cls._instance._SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=cls._instance._engine)
        return cls._instance

    @property
    def engine(self):
        # Retorna motor de base datos
        return self._engine

    @property
    def SessionLocal(self):
        # Retorna fabricante de sesiones
        return self._SessionLocal

db_instance = DatabaseSingleton()
SessionLocal = db_instance.SessionLocal
engine = db_instance.engine

def get_db():
    # Retorna sesion de base datos
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()