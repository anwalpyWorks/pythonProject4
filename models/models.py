from pydantic import BaseModel
from enum import Enum

class Choice_Name(str, Enum):
    one = "one"
    two = "two"
    three = "three"


class schema1(BaseModel):
    name: str
    Class: str
    roll_no: int
