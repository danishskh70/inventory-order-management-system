from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String, func

from app.db.base import Base
from app.model.customer import Customer  


class Order(Base):
    __tablename__="orders"
    id=Column(Integer,primary_key=True,index=True)
    customer_id=Column(Integer,ForeignKey(Customer.id))
    status=Column(String)
    order_date=Column(DateTime(timezone=True),server_default=func.now())
    total_amount=Column(Numeric(10,2))