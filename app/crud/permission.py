from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.model.permission import Permission
from app.schema.permission import PermissionCreate


def create_permission(db:Session,permit:PermissionCreate):
    db_per=Permission(name=permit.name)
    db.add(db_per)
    db.commit()
    db.refresh(db_per)
    return db_per

def get_permission(db:Session,id:int):
    db_permit=db.query(Permission).filter(Permission.id==id).first()
    if not db_permit:
        raise HTTPException(status_code=404,detail="Permission Not Found")
    return db_permit

def get_permissions(db:Session):
    return db.query(Permission).all()