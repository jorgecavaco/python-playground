from pydantic import BaseModel, Field
from datetime import datetime


class TodoBase(BaseModel):
    content: str = Field(..., example="Todo Item")
    due: datetime


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id: int
    done: bool = False

    class Config:
        orm_mode = True
        schema_extra = {
                  "content": "Todo Item",
                  "due": "2021-10-06T17:44:20.814Z"
        }
