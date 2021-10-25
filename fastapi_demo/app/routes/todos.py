from .. import crud
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, models, crud
from app.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/todos")
def list_todos(offset: int = 0, limit: int = 100, session: Session = Depends(get_db)):
    return crud.get_todos(offset=offset, limit=limit, session=session)


@router.post("/todos")
def create_todo(todo: schemas.TodoCreate, session: Session = Depends(get_db)):
    return crud.create_todo(todo=todo, session=session)


@router.put("/todos/{id}")
def update_todo(id: int, done: bool = True, session: Session = Depends(get_db)):
    return crud.update_todo(id=id, done=done, session=session)
