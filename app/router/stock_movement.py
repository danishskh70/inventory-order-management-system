from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.crud.stock_movement import create_stock_movement, get_stock_movement, get_stock_movements
from app.db.session import get_db
from app.model.user import User
from app.schema.stock_movement import StockMovementCreate, StockMovementResponse


router=APIRouter(prefix="/stock_movements",tags=["Stock Movement"])

@router.post("/",response_model=StockMovementResponse)
def add_stock_movement(stock_movement:StockMovementCreate,db:Session=Depends(get_db)):
    return create_stock_movement(stock_movement=stock_movement,db=db)

@router.get("/{stock_movement_id}",response_model=StockMovementResponse)
def read_stock_movement(stock_movement_id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_stock_movement(stock_movement_id=stock_movement_id,db=db)

@router.get("/",response_model=list[StockMovementResponse])
def read_stock_movements(db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_stock_movements(db=db)