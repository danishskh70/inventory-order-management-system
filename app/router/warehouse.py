
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.warehouse import create_warehouse, get_warehouse, get_warehouses
from app.db.session import get_db
from app.schema.warehouse import WareHouseCreate, WareHouseResponse


router=APIRouter(prefix="/warehouses",tags=["WareHouse"])

@router.post("/",response_model=WareHouseResponse)
def add_warehouse(warehouse:WareHouseCreate,db:Session=Depends(get_db)):
    return create_warehouse(warehouse=warehouse,db=db)

@router.get("/{warehouse_id}",response_model=WareHouseResponse)
def read_warehouse(warehouse_id:int,db:Session=Depends(get_db)):
    return get_warehouse(warehouse_id=warehouse_id,db=db)

@router.get("/",response_model=list[WareHouseResponse])
def read_warehouses(db:Session=Depends(get_db)):
    return get_warehouses(db=db)