from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel


class OrderCreate(BaseModel):
    customer_id:int
    status:str


class OrderResponse(BaseModel):
    id:int
    customer_id:int
    status:str
    order_date:datetime
    total_amount:Decimal
    class Config:
        from_attributes=True