"""base model"""
from sqlalchemy.ext.declarative import declarative_base

from pkg.application.core.postgresdb import Engine

# Base Entity Model Schema
EntityMeta = declarative_base()


def init():
    """creates table records in the database"""
    EntityMeta.metadata.create_all(bind=Engine)
