from fastapi import APIRouter, HTTPException
from asgiref.sync import sync_to_async
from typing import List
from tasks.models import Task
from api.schemas.task_schema import TaskCreate, TaskRead

router = APIRouter()

@router.get("/", response_model=List[TaskRead])
async def list_tasks():
    # sync_to_async(list) iterates over the queryset in a sync thread
    tasks = await sync_to_async(list)(Task.objects.all())
    return tasks

@router.post("/", response_model=TaskRead)
async def create_task(task_in: TaskCreate):
    task = await sync_to_async(Task.objects.create)(
        title=task_in.title,
        description=task_in.description or "",
        priority=task_in.priority,
        deadline=task_in.deadline
    )
    return task
