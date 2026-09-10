

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.model.stock_movement import StockMovement
from app.schema.stock_movement import StockMovementCreate


def create_stock_movement(stock_movement:StockMovementCreate,db:Session):
    db_stock_movement=StockMovement(product_id=stock_movement.product_id,change_quantity=stock_movement.change_quantity,reason=stock_movement.reason)
    db.add(db_stock_movement)
    db.commit()
    db.refresh(db_stock_movement)
    return db_stock_movement

def get_stock_movement(stock_movement_id:int,db:Session):
    db_stock_movement=db.query(StockMovement).filter(StockMovement.id==stock_movement_id).first()
    if not db_stock_movement:
        raise HTTPException(status_code=404,detail="Not Fpond Stock Movement")
    return db_stock_movement

def get_stock_movements(db:Session):
    return db.query(StockMovement).all()