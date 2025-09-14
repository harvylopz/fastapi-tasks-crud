from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from . import models, schemas

async def get_task(db: AsyncSession, task_id: int):
    result = await db.get(models.Task, task_id)
    return result

async def get_tasks(db: AsyncSession, skip: int = 0, limit: int = 100):
    query = select(models.Task).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

async def create_task(db: AsyncSession, task: schemas.TaskCreate):
    db_task = models.Task(**task.model_dump())
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def update_task(db: AsyncSession, db_task: models.Task, task_in: schemas.TaskUpdate):
    update_data = task_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def delete_task(db: AsyncSession, db_task: models.Task):
    await db.delete(db_task)
    await db.commit()
    return db_task