#!/usr/bin/python3

"""python file that contains the class definition of a City\
        and an instance Base = declarative_base():
"""

import sys
from sqlalchemy import String, Integer, Column, create_engine, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    """Implementing"""
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
