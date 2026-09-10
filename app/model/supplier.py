from sqlalchemy import Column, Integer, String

from app.db.base import Base


class Supplier(Base):
    __tablename__="suppliers"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    email=Column(String,unique=True,nullable=False)
    phone=Column(String)
    address=Column(String)