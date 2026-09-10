from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func

from app.db.base import Base
from app.model.user import User


class AuditLog(Base):
    __tablename__="audit_logs"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey(User.id))
    action=Column(String)
    table_name=Column(String)
    record_id=Column(Integer)
    timestamp=Column(DateTime(timezone=True),server_default=func.now())