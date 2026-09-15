from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.crud.supplier import create_supplier, get_supplier, get_suppliers
from app.db.session import get_db
from app.model.user import User
from app.schema.supplier import SupplierCreate, SupplierResponse


router=APIRouter(prefix="/suppliers",tags=["Suppliers"])
@router.post("/",response_model=SupplierResponse)
def add_supplier(supplier:SupplierCreate,db:Session=Depends(get_db)):
    return create_supplier(db=db,supplier=supplier)

@router.get("/{supplier_id}",response_model=SupplierResponse)
def read_supplier(supplier_id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_supplier(supplier_id=supplier_id,db=db)

@router.get("/",response_model=list[SupplierResponse])
def read_suppliers(db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_suppliers(db=db)