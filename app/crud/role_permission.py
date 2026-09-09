



from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.model.permission import Permission
from app.model.role import Role


def assign_permission(db:Session,role_id:int,permission_id:int):
    role=db.query(Role).filter(Role.id==role_id).first()
    if not role:
        raise HTTPException(status_code=404,detail="Role not Found")
    permission=db.query(Permission).filter(Permission.id==permission_id).first()
    if not permission :
        raise HTTPException(status_code=404,detail="PErmission not found")
    role.permissions.append(permission)
    db.commit()
    db.refresh(role)
    return role


