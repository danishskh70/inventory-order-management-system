


from pydantic import BaseModel


class PermissionCreate(BaseModel):
    name:str


class PermissionResponse(BaseModel):
    id:int
    name:str

    class Config:
        from_attributes=True 
    