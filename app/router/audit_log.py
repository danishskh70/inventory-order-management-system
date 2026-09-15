from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.crud.audit_log import create_audit_log, get_audit_log, get_audit_logs
from app.db.session import get_db
from app.model.user import User
from app.schema.audit_log import AuditLogCreate, AuditLogResponse


router=APIRouter(prefix="/audit_logs",tags=["Audit Logs"])

@router.post("/",response_model=AuditLogResponse)
def add_audit_log(audit_log:AuditLogCreate,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    return create_audit_log(audit_log=audit_log,db=db)

@router.get("/{audit_log_id}",response_model=AuditLogResponse)
def read_audit_log(audit_log_id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_audit_log(audit_log_id=audit_log_id,db=db)

@router.get("/",response_model=list[AuditLogResponse])
def read_audit_logs(db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_audit_logs(db=db)