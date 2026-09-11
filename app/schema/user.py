

from typing import Optional

from pydantic import BaseModel

class AssignRole(BaseModel):
    role_id: int

    
class UserCreate(BaseModel):
    name:str
    username:str
    password:str

class UserResponse(BaseModel):
    id:int
    name:str
    username:str 
    role_id: Optional[int] = None

    class Config:
        from_attributes =True