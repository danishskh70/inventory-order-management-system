from sqlalchemy import Column, Integer, String

from app.db.base import Base


class WareHouse(Base):
    __tablename__="warehouses"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    location=Column(String)
    