from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(150))
    price = Column(Float)
    date_creation = Column(Date)


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(150))


class Price2(Base):
    __tablename__ = 'price2'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    prise = Column(String(150))
