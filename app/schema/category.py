


from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name:str

class CategoryResponse(BaseModel):
    id:int
    name:str

    class Config:
        from_attributes=True