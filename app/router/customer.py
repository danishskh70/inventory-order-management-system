from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.crud.customer import create_customer, get_customer, get_customers
from app.db.session import get_db
from app.model.user import User
from app.schema.customer import CustomerCreate, CustomerResponse


router=APIRouter(prefix="/customers",tags=["Customers"])

@router.post("/",response_model=CustomerResponse)
def add_customer(customer:CustomerCreate,db:Session=Depends(get_db)):
    return create_customer(db=db,customer=customer)

@router.get("/{customer_id}",response_model=CustomerResponse)
def read_customer(customer_id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_customer(customer_id=customer_id,db=db)

@router.get("/",response_model=list[CustomerResponse])
def read_customers(db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_customers(db=db)