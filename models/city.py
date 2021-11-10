#!/usr/bin/python3
""" holds class City"""
from models.base_model import Base_model


class City(Base_model):
    """Representation of city """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
