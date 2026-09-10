from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.model.supplier import Supplier
from app.schema.supplier import SupplierCreate


def create_supplier(db:Session,supplier:SupplierCreate):
    db_supplier=Supplier(name=supplier.name,email=supplier.email,phone=supplier.phone,address=supplier.address)
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

def get_supplier(db:Session,supplier_id:int):
    db_supplier=db.query(Supplier).filter(Supplier.id==supplier_id).first()
    if not db_supplier:
        raise HTTPException(status_code=404,detail="Supplier not found")
    return db_supplier

def get_suppliers(db:Session):
    return db.query(Supplier).all()