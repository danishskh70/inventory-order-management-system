


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.permission import create_permission, get_permission, get_permissions
from app.db.session import get_db
from app.schema.permission import PermissionCreate, PermissionResponse



router = APIRouter(prefix="/permissions", tags=["Permissions"])


@router.post("/",response_model=PermissionResponse)
def add_permissions(permit:PermissionCreate,db:Session=Depends(get_db)):
    return create_permission(db=db,permit=permit)


@router.get("/{id}",response_model=PermissionResponse)
def read_permission(id:int,db:Session=Depends(get_db)):
    return get_permission(db=db,id=id)


@router.get("/",response_model=list[PermissionResponse])
def read_permissions(db:Session=Depends(get_db)):
    return get_permissions(db=db)
