#!/usr/bin/python3
"""
Contains class Base_model
"""

from datetime import datetime
import models
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"


class Base_model:
    """The Base Model class for the console. Other future classes will be derived from this class"""

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """String representation of the Base_model class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()


def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
<<<<<<< HEAD
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
=======
        newDict = self.__dict__.copy()
        if "created_at" in newDict:
            newDict["created_at"] = newDict["created_at"].strftime(time)
        if "updated_at" in newDict:
            newDict["updated_at"] = newDict["updated_at"].strftime(time)
        newDict["__class__"] = self.__class__.__name__
        return newDict


>>>>>>> 766e2014780af0744234d6324fa214ea30bbc39b
