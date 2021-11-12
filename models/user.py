#!/usr/bin/python3
""" holds class User"""
from models.base_model import Base_model

<<<<<<< HEAD

class User(BaseModel):
    """Representation of a user """
=======
class User(Base_model):
    """User Representation """
>>>>>>> 766e2014780af0744234d6324fa214ea30bbc39b
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
