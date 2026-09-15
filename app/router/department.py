from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.crud.departments import create_department, get_department, get_departments
from app.db.session import get_db
from app.model.user import User
from app.schema.department import DepartmentCreate, DepartmentResponse


router=APIRouter(prefix="/departments",tags=["Department"])

@router.post("/",response_model=DepartmentResponse)
def add_department(department:DepartmentCreate,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    return create_department(department=department,db=db)

@router.get("/{department_id}",response_model=DepartmentResponse)
def read_department(department_id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_department(department_id=department_id,db=db)

@router.get("/",response_model=list[DepartmentResponse])
def read_departments(db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_departments(db)