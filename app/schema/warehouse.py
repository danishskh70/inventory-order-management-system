from pydantic import BaseModel


class WareHouseCreate(BaseModel):
    name:str
    location:str

class WareHouseResponse(BaseModel):
    id:int
    name:str
    location:str
    class Config:
        from_attributes=True