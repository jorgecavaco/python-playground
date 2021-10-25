from sqlalchemy.orm import Session
from . import schemas, models


def get_todos(session: Session, offset: int = 0, limit: int = 100):
    return session.query(models.Todo) \
        .offset(offset) \
        .limit(limit) \
        .all()


def create_todo(session: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(content=todo.content, due=todo.due)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)

    return db_todo


def update_todo(session: Session, id: int, done: bool):
    db_todo = session.query(models.Todo).filter(models.Todo.id == id).first()
    db_todo.done = done
    session.commit()

    session.refresh(db_todo)

    return db_todo
