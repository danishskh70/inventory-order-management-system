from fastapi import FastAPI

from app.router import category, permission, role, role_permission, user
from app.model import user as user_model
from app.model import role as role_model
from app.model import permission as permission_model
from app.model import role_permission as role_permission_model

app = FastAPI()

app.include_router(user.router)
app.include_router(role.router)
app.include_router(permission.router)
app.include_router(role_permission.router)
app.include_router(category.router)

@app.get("/")
def root():
    return {"message": "root"}