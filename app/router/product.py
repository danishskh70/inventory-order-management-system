




from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.product import create_product, get_product, get_products
from app.db.session import get_db
from app.schema.product import ProductCreate, ProductResponse


router=APIRouter(prefix="/products",tags=["Product"])


@router.post("/",response_model=ProductResponse)
def add_product(product:ProductCreate,db:Session=Depends(get_db)):
    return create_product(db=db,product=product)


@router.get("/{product_id}",response_model=ProductResponse)
def read_product(product_id:int,db:Session=Depends(get_db)):
    return get_product(product_id=product_id,db=db)

@router.get("/",response_model=list[ProductResponse])
def read_products(db:Session=Depends(get_db)):
    return get_products(db=db)