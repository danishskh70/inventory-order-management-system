from pydantic import BaseModel


class SupplierCreate(BaseModel):
    name:str
    email:str
    phone:str
    address:str

class SupplierResponse(BaseModel):
    id:int
    name:str
    email:str
    phone:str
    address:str

    class Config:
        from_attributes=True