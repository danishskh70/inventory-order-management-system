from typing import Optional

from pydantic import BaseModel


class DepartmentCreate(BaseModel):
    name:str
    parent_id: Optional[int] = None

class DepartmentResponse(BaseModel):
    id:int
    name:str
    parent_id:int
    class Config:
        from_attributes=True
