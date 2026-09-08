



from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.user import create_user, delete_user, get_user, get_users, update_user
from app.db.session import get_db
from app.schema.user import UserCreate, UserResponse


router=APIRouter(prefix="/users",tags=["Users"])

@router.post("/",response_model=UserResponse)
def register_user(user:UserCreate,db:Session=Depends(get_db)):
    return create_user(db=db,user=user)


@router.get("/{user_id}",response_model=UserResponse)
def read_user(user_id:int,db:Session=Depends(get_db)):
    return get_user(db,user_id)

@router.get("/",response_model=list[UserResponse])
def read_users(db:Session=Depends(get_db)):
    return get_users(db)

@router.put("/{user_id}",response_model=UserResponse)
def update_user_info(user_id:int,user:UserCreate,db:Session=Depends(get_db)):
    return update_user(db,user_id,user)

@router.delete("/{user_id}",response_model=UserResponse)
def remove_user(user_id:int,db:Session=Depends(get_db)):
    return delete_user(db,user_id)