

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.security import create_access_token
from app.crud.user import authenticate_user
from app.db.session import get_db
from app.schema.auth import LoginRequest, TokenResponse


router=APIRouter(prefix="/auth",tags=["Auth"])

@router.post("/login",response_model=TokenResponse)
def login(credential:LoginRequest,db:Session=Depends(get_db)):
    user=authenticate_user(db=db,username=credential.username,password=credential.password)
    if not user :
        raise HTTPException(status_code=401,detail="Incorrect username and password")
    token=create_access_token(data={"sub":user.username})
    return TokenResponse(access_token=token,token_type="bearer")