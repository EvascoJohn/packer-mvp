from database import session
from sqlalchemy import Column, Integer, String, DateTime, VARCHAR
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Bag(Base):

    """  """

    __tablename__ = 'bags'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(100))



class Item(Base):

    """  """

    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(100))
    quantity = Column(Integer, default=0)


class Event(Base):

    """  """

    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(100))
    time_due = Column(DateTime, nullable=True)
