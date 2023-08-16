from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from database import SessionLocal,Base,engine
from models import Item
from schemas import ItemView

app = FastAPI()

def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()
    
Base.metadata.create_all(bind=engine)

router = SQLAlchemyCRUDRouter(
    schema=ItemView,
    create_schema=ItemView,
    db_model=Item,
    db=get_db,
    prefix='item'
)

app.include_router(router)
