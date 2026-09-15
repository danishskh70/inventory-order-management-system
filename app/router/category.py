


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.crud.category import create_category, get_categories, get_category
from app.db.session import get_db
from app.model.user import User
from app.schema.category import CategoryCreate, CategoryResponse


router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/",response_model=CategoryResponse)
def add_category(category:CategoryCreate,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    return create_category(db=db,category=category)

@router.get("/{category_id}",response_model=CategoryResponse)
def read_category(category_id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_category(category_id=category_id,db=db)

@router.get("/",response_model=list[CategoryResponse])
def read_categories(db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_categories(db=db)