#!/usr/bin/python3
"""A class that defines all common attributes/methods for other classes"""
import uuid
import models
from datetime import datetime, timedelta

class BaseModel:
    """The base class that other classes inherits from"""

    def __init__(self):
        """Initialization of the insatnce attributes
        
        Arguments:
            id: the unique id of each user
            created_at: the time the user was created
            updated_at: the time the user was updated
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """The formated string method to overide printing to the stdoutput"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        dictn = self.__dict__.copy()
        dictn["__class__"] = self.__class__.__name__
        dictn["created_at"] = self.created_at.isoformat()
        dictn["updated_at"] = self.updated_at.isoformat()

        return dictn
