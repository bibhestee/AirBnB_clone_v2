#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
        Class: City.

        Info: The city class, contains state ID and name.

        Attributes:
            __tablename__ (str): The name of the MySQL table cities.
            name (sqlalchemy String): The name of the City.
            state_id (sqlalchemy String): The state id of the City.
     """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', backref='cities', cascade='delete')
