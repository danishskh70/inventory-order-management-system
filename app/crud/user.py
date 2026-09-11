

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.security import hash_password, verify_password
from app.model.role import Role
from app.model.user import User
from app.schema.user import UserCreate

def authenticate_user(db:Session,username:str,password:str):
    user=db.query(User).filter(User.username==username).first()
    if not user:
        return None
    if not verify_password(password,user.password):
        return None
    return user

def create_user(db:Session,user:UserCreate):
    hash_pass=hash_password(password=user.password)
    db_user=User(name=user.name,username=user.username,password=hash_pass)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def assign_role_to_user(db: Session, user_id: int, role_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_role = db.query(Role).filter(Role.id == role_id).first()
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")

    db_user.role_id = role_id
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db:Session,user_id:int):
    return db.query(User).filter(User.id==user_id).first()

def get_users(db:Session):
    return db.query(User).all()

def update_user(db:Session,user_id:int,user:UserCreate):
    db_user=db.query(User).filter(User.id==user_id).first()
    if not db_user:
        raise HTTPException(status_code=404,detail="User Not Found")
    if db_user:
        db_user.name=user.name 
        db_user.username=user.username 
        db_user.password=hash_password(user.password)
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db:Session,user_id:int):
    db_user=db.query(User).filter(User.id==user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()

    return db_user


