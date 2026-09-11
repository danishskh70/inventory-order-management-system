from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.db.session import get_db
from app.model.user import User


oauth2_scheme=OAuth2PasswordBearer(tokenUrl="auth/login")


def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
    try:
        payload=decode_access_token(token=token)
        username=payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401,detail="Invalid token")
    except InvalidTokenError:
        raise HTTPException(status_code=401,detail="Invalid token")
    db_user=db.query(User).filter(User.username==username).first()
    if not db_user:
        raise HTTPException(status_code=404,detail="User not Found / Exist")
    return db_user

def require_permission(permission_name: str):
    def dependency(current_user: User = Depends(get_current_user)):
        if current_user.role_id is None:
            raise HTTPException(status_code=403, detail="No role assigned")

        role = current_user.role
        if not role:
            raise HTTPException(status_code=403, detail="Role not found")

        permission_names = [perm.name for perm in role.permissions]

        if permission_name not in permission_names:
            raise HTTPException(status_code=403, detail="Not enough permissions")

        return current_user

    return dependency