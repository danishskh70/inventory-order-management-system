from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.model.department import Department
from app.schema.department import DepartmentCreate


def create_department(department:DepartmentCreate,db:Session):
    db_department=Department(name=department.name,parent_id=department.parent_id)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department

def get_department(department_id:int,db:Session):
    db_department=db.query(Department).filter(Department.id==department_id).first()
    if not db_department:
        raise HTTPException(status_code=404,detail="department not found")
    return db_department

def get_departments(db:Session):
    return db.query(Department).all()