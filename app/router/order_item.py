from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.order_item import create_order_item, get_order_item, get_order_items
from app.db.session import get_db
from app.schema.order_item import OrderItemCreate, OrderItemResponse


router=APIRouter(prefix="/orderitems",tags=["Order Item"])

@router.post("/",response_model=OrderItemResponse)
def add_order_item(order_item:OrderItemCreate,db:Session=Depends(get_db)):
    return create_order_item(order_item=order_item,db=db)

@router.get("/{order_item_id}",response_model=OrderItemResponse)
def read_order_item(order_item_id:int,db:Session=Depends(get_db)):
    return get_order_item(order_item_id=order_item_id,db=db)

@router.get("/",response_model=list[OrderItemResponse])
def read_order_items(db:Session=Depends(get_db)):
    return get_order_items(db=db)