from pydantic import BaseModel, EmailStr
from encryption_decoding import *

class Caesar(BaseModel):
    text: str
    offset: int
    mode: str

class Fence(BaseModel):
    text: str
