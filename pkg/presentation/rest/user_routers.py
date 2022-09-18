"""rest endpoints"""
from fastapi import APIRouter, Depends, status

from pkg.domain.dto.schema.user import UserProfile
from pkg.usecase.users import UserUsecase


user_router = APIRouter(prefix="/auth", tags=["auth"])


@user_router.post("/create-user", status_code=status.HTTP_201_CREATED)
def create(user: UserProfile, user_usecase: UserUsecase = Depends()):
    """creates a new user record"""
    return user_usecase.create(user)
