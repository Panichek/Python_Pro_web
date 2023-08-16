from pydantic import BaseModel

class ItemCreateView(BaseModel):
    title:str = ""
    text:str = ""

    class Config:
        orm_mode = True


class ItemView(ItemCreateView):
    id: int
