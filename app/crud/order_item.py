


from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.model.order_item import OrderItem
from app.model.product import Product
from app.schema.order_item import OrderItemCreate


def create_order_item(db:Session,order_item:OrderItemCreate):
    db_product=db.query(Product).filter(Product.id==order_item.product_id).first()
    if not db_product:
        raise HTTPException(status_code=404,detail="product not found")
    
    if db_product.quantity < order_item.quantity: 
        raise HTTPException(status_code=400,detail="Insuffiecient Storage")
    db_product.quantity=db_product.quantity-order_item.quantity

    db_order_item=OrderItem(product_id=db_product.id,order_id=order_item.order_id,quantity=order_item.quantity,price_at_order=db_product.price)

    db.add(db_order_item)
    db.commit()
    db.refresh(db_order_item)
    return db_order_item


def get_order_item(db:Session,order_item_id:int):
    db_order_item=db.query(OrderItem).filter(OrderItem.id==order_item_id).first()
    if not db_order_item:
        raise HTTPException(status_code=404,detail="Order Item Not Found")
    return db_order_item

def get_order_items(db:Session):
    return db.query(OrderItem).all()

