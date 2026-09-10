from datetime import datetime

from pydantic import BaseModel


class StockMovementCreate(BaseModel):
    product_id:int
    change_quantity:int
    reason:str

class StockMovementResponse(BaseModel):
    id:int
    product_id:int
    change_quantity:int
    reason:str
    moved_at:datetime

    class Config:
        from_attributes=True