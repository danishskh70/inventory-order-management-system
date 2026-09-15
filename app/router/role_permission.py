




from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import require_permission
from app.crud.role_permission import assign_permission
from app.db.session import get_db
from app.model.user import User
from app.schema.role import RoleResponse
from app.schema.role_permission import AssignPermission


router=APIRouter(prefix="/roles",tags=["Role Permission"])

@router.post("/{role_id}",response_model=RoleResponse)
def add_permission_to_role(role_id:int,payload:AssignPermission,db:Session=Depends(get_db),current_user:User=Depends(require_permission("roles:manage"))):
    return assign_permission(db,role_id,payload.permission_id)