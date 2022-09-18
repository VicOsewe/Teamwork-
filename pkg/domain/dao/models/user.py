"""models related to users"""
from sqlalchemy import Column,  Integer, String
from pkg.domain.dao.models.base_model import EntityMeta



class User(EntityMeta): # pylint: disable=too-few-public-methods
    """represents the user model"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    job_role = Column(String, nullable=False)
    department = Column(String, nullable=False)
    address = Column(String)
