from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.model.customer import Customer
from app.schema.customer import CustomerCreate


def create_customer(db:Session,customer:CustomerCreate):
    db_customer=Customer(name=customer.name,email=customer.email,phone=customer.phone)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customer(db:Session,customer_id:int):
    db_customer=db.query(Customer).filter(Customer.id==customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404,detail="Customer not found")
    return db_customer

def get_customers(db:Session):
    return db.query(Customer).all()
