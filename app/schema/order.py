from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel


class OrderCreate(BaseModel):
    customer_id:int
    status:str
    total_amount:Decimal

class OrderResponse(BaseModel):
    id:int
    customer_id:int
    status:str
    order_date:datetime
    total_amount:Decimal
    class Config:
        from_attributes=True