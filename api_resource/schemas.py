from pydantic import BaseModel

class ItemView(BaseModel):
    title:str = ""
    text:str = ""

    class Config:
        orm_mode = True
