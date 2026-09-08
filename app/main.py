from fastapi import FastAPI

from app.router import role, user

app=FastAPI()

app.include_router(user.router)
app.include_router(role.router)

@app.get("/")
def root():
    return {"message":"root"}

