from pydantic import BaseModel


class RoleCreate(BaseModel):
    name:str

class PermissionInRole(BaseModel):
    id:int
    name:str
    class Config:
        from_attributes=True

class RoleResponse(BaseModel):
    id:int
    name:str
    permissions:list[PermissionInRole]=[]

    class Config:
        from_attributes=True 


