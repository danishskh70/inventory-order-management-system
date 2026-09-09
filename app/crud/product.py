from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.model.product import Product
from app.schema.product import ProductCreate


def create_product(db:Session,product:ProductCreate):
    db_product=Product(name=product.name,sku=product.sku,price=product.price,quantity=product.quantity,category_id=product.category_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db:Session,product_id:int):
    db_product=db.query(Product).filter(Product.id==product_id).first()
    if not db_product:
        raise HTTPException(status_code=404,detail="Product Not Found")
    return db_product

def get_products(db:Session):
    return db.query(Product).all()
