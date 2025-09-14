from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, AsyncGenerator
from contextlib import asynccontextmanager

from . import crud, models, schemas
from .database import engine, AsyncSessionLocal


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    yield

app = FastAPI(
    title="Tasks API",
    description="An API to manage a task list.",
    lifespan=lifespan
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

@app.post("/tasks/", response_model=schemas.Task, status_code=status.HTTP_201_CREATED, tags=["Tasks"])
async def create_task(task: schemas.TaskCreate, db: AsyncSession = Depends(get_db)):

    return await crud.create_task(db=db, task=task)

@app.get("/tasks/", response_model=List[schemas.Task], tags=["Tasks"])
async def read_tasks(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    tasks = await crud.get_tasks(db, skip=skip, limit=limit)
    return tasks

@app.get("/tasks/{task_id}", response_model=schemas.Task, tags=["Tasks"])
async def read_task(task_id: int, db: AsyncSession = Depends(get_db)):
    db_task = await crud.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.put("/tasks/{task_id}", response_model=schemas.Task, tags=["Tasks"])
async def update_task(task_id: int, task_update: schemas.TaskUpdate, db: AsyncSession = Depends(get_db)):
    db_task = await crud.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return await crud.update_task(db=db, db_task=db_task, task_in=task_update)

@app.delete("/tasks/{task_id}", response_model=schemas.Task, tags=["Tasks"])
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    db_task = await crud.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return await crud.delete_task(db=db, db_task=db_task)