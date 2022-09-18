"""user"""

from fastapi import Depends
from sqlalchemy.orm import Session

from pkg.application.core.postgresdb import (
    get_db_connection,
)
from pkg.domain.dao.models.user import User


class UserRepository:
    """sets up users database layer"""
    database: Session

    def __init__(self, database: Session = Depends(get_db_connection)) -> None:
        """initializes a new database instance"""
        self.database = database

    def create(self, user: User) -> User:
        """creates a new user record in the database"""
        self.database.add(user)
        self.database.commit()
        self.database.refresh(user)
        return user

    def log_in_user(self) -> None:
        """" log in use"""
        return None
