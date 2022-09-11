from pkg.interfaces.repository import Repository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pkg.application.core.config import settings



class TeamWorkDB(Repository):
    def __init__(self):
        """initializes a new teamwork database instance that meets all the precondition checks"""
        SQLALCHEMY_DATABASE_URL =  f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        print("Connected to BD")
        SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)