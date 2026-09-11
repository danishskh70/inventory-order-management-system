
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.model.warehouse import WareHouse
from app.schema.warehouse import WareHouseCreate


def create_warehouse(db:Session,warehouse:WareHouseCreate):
    db_warehouse=WareHouse(name=warehouse.name,location=warehouse.location)
    db.add(db_warehouse)
    db.commit()
    db.refresh(db_warehouse)
    return db_warehouse

def get_warehouse(db:Session,warehouse_id:int):
    db_warehouse=db.query(WareHouse).filter(WareHouse.id==warehouse_id).first()
    if not db_warehouse:
        raise HTTPException(status_code=404,detail="WareHouse not found")
    return db_warehouse

def get_warehouses(db:Session):
    return db.query(WareHouse).all()
    