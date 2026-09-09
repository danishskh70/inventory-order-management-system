




from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.model.category import Category
from app.schema.category import CategoryCreate


def create_category(db:Session,category:CategoryCreate):
    db_category=Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_category(db:Session,category_id:int):
    db_category=db.query(Category).filter(Category.id==category_id).first()
    if not db_category:
        raise HTTPException(status_code=404,detail="Category Not Found")
    return db_category

def get_categories(db:Session):
    return db.query(Category).all()