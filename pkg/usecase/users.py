"""
Handles all the business logic related to a user which include:
1. Create a user account
2. User sign in
3.

"""
from fastapi import Depends

from pkg.domain.dto.schema.user import UserProfile
from pkg.infrastructure.database.postgres.user import UserRepository
from pkg.domain.dao.models.user import User


class UserUsecase:
    """
    This is a representation of a user's contract
    """

    user_repository: UserRepository

    def __init__(self, user_repository: UserRepository = Depends()) -> None:
        self.user_repository = user_repository

    def create(self, user_body: UserProfile) -> User:
        """
        Handles the creation of a user's account
        """
        return self.user_repository.create(
            User(
                first_name=user_body.first_name,
                last_name=user_body.last_name,
                email=user_body.email,
                password=user_body.password,
                gender=user_body.gender,
                job_role=user_body.job_role,
                department=user_body.department,
                address=user_body.address,
            )
        )

    def log_in_user(self) -> None:
        """log in user"""
        return None
