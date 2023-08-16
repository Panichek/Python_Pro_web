'''
Створити таблицю item (Товари)
реалізувати api для роботи з нею через
fast api
'''
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Text
from sqlalchemy.orm import relationship

from database import Base

class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True)
    title = Column(String(150))
    text = Column(Text)
