


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.role import create_role, get_role, get_roles
from app.db.session import get_db
from app.schema.role import RoleCreate, RoleResponse


router=APIRouter(prefix="/roles",tags=["Roles"])

@router.post("/",response_model=RoleResponse)
def add_roles(role:RoleCreate,db:Session=Depends(get_db)):
    return create_role(db,role)

@router.get("/{role_id}",response_model=RoleResponse)
def read_role(role_id:int,db:Session=Depends(get_db)):
    return get_role(db,role_id)

@router.get("/",response_model=list[RoleResponse])
def read_roles(db:Session=Depends(get_db)):
    return get_roles(db)