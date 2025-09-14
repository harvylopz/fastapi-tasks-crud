from pydantic import BaseModel, ConfigDict
from typing import Optional


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool = False


class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    done: Optional[bool] = None


class Task(TaskBase):
    id: int
    model_config = ConfigDict(from_attributes=True)