from pydantic import BaseModel

class Bag(BaseModel):
    name: str

class Item(BaseModel):
    name: str
    quantity: int

class Event(BaseModel):
    name: str
    time_due: str