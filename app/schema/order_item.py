from decimal import Decimal

from pydantic import BaseModel


class OrderItemCreate(BaseModel):
    order_id:int
    product_id:int
    quantity:int


class OrderItemResponse(BaseModel):
    id:int
    order_id:int
    product_id:int
    quantity:int
    price_at_order:Decimal

    class Config:
        from_attributes=True
