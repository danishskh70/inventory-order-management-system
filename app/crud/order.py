from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.model.order import Order
from app.schema.order import OrderCreate



def create_order(db:Session,order:OrderCreate):
    db_order=Order(customer_id=order.customer_id,status=order.status,total_amount=order.total_amount)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db:Session,order_id:int):
    db_order=db.query(Order).filter(Order.id==order_id).first()
    if not db_order:
        raise HTTPException(status_code=404,detail="Order not Found")
    return db_order

def get_orders(db:Session):
    return db.query(Order).all()