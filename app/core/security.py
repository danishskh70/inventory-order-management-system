from datetime import datetime, timedelta, timezone
from typing import Optional

import jwt
from pwdlib import PasswordHash

from app.core.config import settings

password_hash=PasswordHash.recommended()

def hash_password(password:str):
    return password_hash.hash(password=password)

def verify_password(plain_pass:str,hashed_pass:str):
    return password_hash.verify(plain_pass,hashed_pass)

def create_access_token(data:dict,expires_delta: Optional[timedelta] = None):
    to_encode=data.copy()
    if expires_delta:
        expire =datetime.now(timezone.utc)+expires_delta
    else:
        expire=datetime.now(timezone.utc)+timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,settings.secret_key,algorithm=settings.algorithm)
    return encoded_jwt

def decode_access_token(token:str):
    payload=jwt.decode(token,settings.secret_key,algorithms=[settings.algorithm])
    return payload