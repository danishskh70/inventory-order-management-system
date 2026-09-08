



from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.model.role import Role
from app.schema.role import RoleCreate


def create_role(db:Session,role:RoleCreate):
    db_role=Role(name=role.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


def get_role(db:Session,role_id:int):
    db_role=db.query(Role).filter(Role.id==role_id).first()
    if not db_role:
        raise HTTPException(status_code=404,detail="Role Not Found")
    return db_role

def get_roles(db:Session):
    return db.query(Role).all()
