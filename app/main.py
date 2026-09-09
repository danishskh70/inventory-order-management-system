from fastapi import FastAPI

from app.router import permission, role, user

app=FastAPI()

app.include_router(user.router)
app.include_router(role.router)
app.include_router(permission.router)

@app.get("/")
def root():
    return {"message":"root"}

