from fastapi import FastAPI, HTTPException
from app.models import TaskCreate
from app.storage import get_all_tasks, create_task, update_task, delete_task

app = FastAPI()


@app.get("/tasks")
def read_tasks():
    return get_all_tasks()


@app.post("/tasks")
def add_task(task: TaskCreate):
    return create_task(task)


@app.put("/tasks/{task_id}")
def edit_task(task_id: int, task: TaskCreate):
    updated = update_task(task_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated


@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    success = delete_task(task_id=task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
