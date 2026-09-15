from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_current_user, require_permission
from app.crud.order import create_order, get_order, get_orders
from app.db.session import get_db
from app.model.user import User
from app.schema.order import OrderCreate, OrderResponse


router=APIRouter(prefix="/orders",tags=["Order"])

@router.post("/",response_model=OrderResponse)
def add_order(order:OrderCreate,db:Session=Depends(get_db),current_user:User=Depends(require_permission("orders:create"))):
    return create_order(db=db,order=order)

@router.get("/{order_id}",response_model=OrderResponse)
def read_order(order_id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_order(order_id=order_id,db=db)

@router.get("/",response_model=list[OrderResponse])
def read_orders(db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_orders(db)