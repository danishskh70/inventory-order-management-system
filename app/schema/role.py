from pydantic import BaseModel


class RoleCreate(BaseModel):
    name:str

class RoleResponse(BaseModel):
    id:int
    name:str

    class Config:
        from_attributes:True # type: ignore