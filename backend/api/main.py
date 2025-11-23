from fastapi import FastAPI

app = FastAPI(title="AI Task Scheduler API")

from api.v1.endpoints import tasks

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

app.include_router(tasks.router, prefix="/v1/tasks", tags=["tasks"])
