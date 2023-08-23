from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Autor(Base):
    __tablename__ = 'autor'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(150))



class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(150))


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    note = Column(String(150))
