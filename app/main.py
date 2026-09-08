from fastapi import FastAPI

from app.router import user

app=FastAPI()

app.include_router(user.router)

@app.get("/")
def root():
    return {"message":"root"}

