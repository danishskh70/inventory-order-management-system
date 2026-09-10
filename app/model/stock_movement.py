from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func

from app.db.base import Base
from app.model.product import Product


class StockMovement(Base):
    __tablename__="stock_movements"
    id=Column(Integer,primary_key=True,index=True)
    product_id=Column(Integer,ForeignKey(Product.id))
    change_quantity=Column(Integer)
    reason=Column(String)
    moved_at=Column(DateTime(timezone=True),server_default=func.now())

