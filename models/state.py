#!/usr/bin/python3
""" holds class State"""
from models.base_model import Base_model


class State(Base_model):
    """Representation of state """
    name = ""

    def __init__(self, *args, **kwargs):
<<<<<<< HEAD
        """initializes state"""
        super().__init__(*args, **kwargs)
=======
         """initializes state"""
         super().__init__(*args, **kwargs)
>>>>>>> 766e2014780af0744234d6324fa214ea30bbc39b
