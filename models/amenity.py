#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
        Class: Amenity

        Info: represents an Amenity for a MySQL database.

        Attributes:
            __tablename__ (str): The name of the MySQL table to
                                    store Amenities.
            name (sqlalchemy String) : The amenity name.
            place_amenities (sqlalchemy relationship): Place-Amenity
                                        relationship.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
