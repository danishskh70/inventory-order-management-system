from sqlalchemy import Column, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.model.order import Order
from app.model.product import Product


class OrderItem(Base):
    __tablename__="order_items"
    id=Column(Integer,primary_key=True,index=True)
    order_id=Column(Integer,ForeignKey(Order.id))
    product_id=Column(Integer,ForeignKey(Product.id))
    quantity=Column(Integer)
    price_at_order=Column(Numeric(10,2))
    order = relationship("Order", back_populates="order_items")