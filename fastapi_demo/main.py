from fastapi import FastAPI
from app.routes import todos, users


app = FastAPI()
app.include_router(todos.router)
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


