from sqlalchemy import Column, ForeignKey, Integer, String

from app.db.base import Base


class Department(Base):
    __tablename__="departments"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,unique=True,nullable=False)
    parent_id=Column(Integer,ForeignKey("departments.id"),nullable=True)