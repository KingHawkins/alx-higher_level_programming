#!/usr/bin/python3

"""ython file that contains the class definition of a State\
        and an instance Base = declarative_base():
            """
from sqlalchemy import String, Integer, Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys


Base = declarative_base()
class State(Base):
    """Implementing"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
