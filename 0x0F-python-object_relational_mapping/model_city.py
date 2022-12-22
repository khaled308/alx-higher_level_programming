#!/usr/bin/python3
"""
Python file to create class definition of a State and
an instance Base = declarative_base()
"""
""" Importing modules """
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

""" Creating class """


class City(Base):
    """ Class City """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship("State")

    def __str__(self):
        """__str__ attribute"""
        return "{}".format(self.name)
