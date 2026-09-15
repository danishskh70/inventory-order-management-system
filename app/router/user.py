



from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_current_user, require_permission
from app.crud.user import create_user, delete_user, get_user, get_users, update_user
from app.db.session import get_db
from app.model.user import User
from app.schema.user import UserCreate, UserResponse
from app.schema.user import AssignRole
from app.crud.user import assign_role_to_user


router=APIRouter(prefix="/users",tags=["Users"])

@router.post("/",response_model=UserResponse)
def register_user(user:UserCreate,db:Session=Depends(get_db)):
    return create_user(db=db,user=user)


@router.post("/{user_id}/role", response_model=UserResponse)
def add_role_to_user(user_id: int, payload: AssignRole, db: Session = Depends(get_db)):
    return assign_role_to_user(db=db, user_id=user_id, role_id=payload.role_id)

@router.get("/{user_id}",response_model=UserResponse)
def read_user(user_id:int,db:Session=Depends(get_db)):
    return get_user(db,user_id)

@router.get("/",response_model=list[UserResponse])
def read_users(db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_users(db)

@router.put("/{user_id}",response_model=UserResponse)
def update_user_info(user_id:int,user:UserCreate,db:Session=Depends(get_db),current_user:User=Depends(require_permission("users:edit"))):
    return update_user(db,user_id,user)

@router.delete("/{user_id}",response_model=UserResponse)
def remove_user(user_id:int,db:Session=Depends(get_db),current_user:User=Depends(require_permission("users:delete"))):
    return delete_user(db,user_id)