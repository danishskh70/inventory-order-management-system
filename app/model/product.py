from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.model.category import Category


class Product(Base):
    __tablename__="products"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False,unique=True)
    sku=Column(String,unique=True,nullable=False)
    price=Column(Numeric(10,2))
    quantity=Column(Integer)
    category_id=Column(Integer,ForeignKey(Category.id))
    category=relationship("Category",back_populates="products")
    