#!/usr/bin/python3

"""ython file that contains the class definition of a State\
        and an instance Base = declarative_base():
"""

import sys
from sqlalchemy import String, Integer, Column, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class State(Base):
    """Implementing"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
