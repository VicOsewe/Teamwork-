"""user"""
from typing import Optional
from pydantic import BaseModel # pylint: disable=no-name-in-module


class UserProfile(BaseModel):  # pylint: disable=too-few-public-methods
    """user profile model"""
    first_name: str
    last_name: str
    email: str
    password: str
    gender: str
    job_role: str
    department: str
    address: Optional[str]


class UserResponse(BaseModel): # pylint: disable=too-few-public-methods
    """user response model"""
    id: int
