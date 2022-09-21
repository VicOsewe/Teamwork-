"""initializes a new database instance"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from pkg.application.core.environment import get_environment_variables

# Runtime Environment Configuration
env = get_environment_variables()

# Generate Database URL
DATABASE_URL = f"postgresql://{env.POSTGRES_USER}:{env.POSTGRES_PASSWORD}@{env.POSTGRES_SERVER}:{env.POSTGRES_PORT}/{env.POSTGRES_DB}"  # pylint: disable=line-too-long

# Create Database Engine
debug_mode = bool(env.DEBUG_MODE)
Engine = create_engine(DATABASE_URL, echo=debug_mode, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)


def get_db_connection():
    """retrieves a database connection"""
    database = scoped_session(SessionLocal)
    try:
        yield database
    finally:
        database.close()  # pylint: disable=no-member
