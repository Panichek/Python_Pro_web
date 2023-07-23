'''
Створити таблицю
Користувач поля username password
Категорія поля name description
Замітка поля title text
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///tasks19.db")

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(100), nullable=False)

class Note(Base):
    __tablename__ = 'note'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    text = Column(String(100), nullable=False)

engine = create_engine("sqlite:///tasks19.db")

Base.metadata.create_all(engine)

Session = sessionmaker(engine)
'''
with Session() as session:
    users = User(username="username 3",
                 password="password",
                 )
    session.add(users)
    session.commit()

with Session() as session:
    category = Category(name="name 2",
                 description="description",
                 )
    session.add(category)
    session.commit()

with Session() as session:
    note = Note(title="title 2",
                 text="text",
                 )
    session.add(note)
    session.commit()
'''