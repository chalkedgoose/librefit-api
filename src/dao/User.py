from dataclasses import dataclass


@dataclass
class User:
    """ 
     Data Access Object for LibreFit Users
    """
    id: int
    name: str
    age: int
