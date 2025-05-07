from database import tasks
from models.task import Task

def create_task(name, priority, status="pending"):
    task = Task(name, priority, status)
    tasks.append(task)
    return task.to_dict()
    

def list_tasks():
    return [task.to_dict() for task in tasks]

def delete_task(name):
    global tasks
    tasks = [task for task in tasks if task.name != name]
    return {"message": f"Deleted task '{name}'"}
