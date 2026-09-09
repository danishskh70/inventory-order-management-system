


from sqlalchemy import Column, ForeignKey, Integer

from app.db.base import Base


class RolePermission(Base):
    __tablename__="role_permissions"
    role_id=Column(Integer,ForeignKey("roles.id"),primary_key=True)
    permission_id=Column(Integer,ForeignKey("permissions.id"),primary_key=True)
    