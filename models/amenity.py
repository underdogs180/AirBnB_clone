#!/usr/bin/python3
""" holds class Amenity"""
from models.base_model import Base_model


class Amenity(Base_model):
    """Representation of Amenity """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes Amenity"""
        super().__init__(*args, **kwargs)
