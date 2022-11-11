#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
# Packages
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Declare a Base Model from sqlalchemy
Base = declarative_base()


class BaseModel:
    """
        Class: BaseModel

        Info: A base class for all hbnb models.

        Attributes:
            _id (sqlalchemy String): The BaseModel id.
            _created_at(sqlalchemy DateTime): The datatime at creation
            _updated_at (sqlalchemy DateTime): The datetime of last update
    """

    fmt = '%Y-%m-%dT%H:%M:%S.%f'

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(),
                        nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(),
                        nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new BaseModel.

            Args:
                *args (any): Unused.
                **kwargs (dict): Key/value pairs of attributes.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            del kwargs['__class__']
            for key, value in kwargs.items():
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                        self.fmt)
                elif key == 'created_at':
                    self.created_at = datetime.strptime(kwargs['created_at'],
                                                        self.fmt)
                else:
                    setattr(self, key, value)


    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """ Delete the current instance from the storage """
        models.storage.delete(self)
