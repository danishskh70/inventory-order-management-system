from decimal import Decimal

from pydantic import BaseModel


class ProductCreate(BaseModel):
    name:str
    sku:str
    price:Decimal
    quantity:int
    category_id:int 



class ProductResponse(BaseModel):
    id:int
    name:str
    sku:str
    price:Decimal
    quantity:int
    category_id:int 

    class Config:
        from_attributes=True
