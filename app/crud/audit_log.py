
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.model.audit_log import AuditLog
from app.schema.audit_log import AuditLogCreate


def create_audit_log(audit_log:AuditLogCreate,db:Session):
    db_audit_log=AuditLog(user_id=audit_log.user_id,action=audit_log.action,table_name=audit_log.table_name,record_id=audit_log.record_id)
    db.add(db_audit_log)
    db.commit()
    db.refresh(db_audit_log)
    return db_audit_log

def get_audit_log(audit_log_id:int,db:Session):
    db_audit_log=db.query(AuditLog).filter(AuditLog.id==audit_log_id).first()
    if not db_audit_log:
        raise HTTPException(status_code=404,detail="Audit Log not Found")
    return db_audit_log

def get_audit_logs(db:Session):
    return db.query(AuditLog).all()