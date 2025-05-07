from routes.task_routes import create_task, list_tasks, delete_task

def test_create_task():
    create_task("Test task", "low")
    assert any(task["name"] == "Test task" for task in list_tasks())

def test_delete_task():
    create_task("Temp", "medium")
    delete_task("Temp")
    assert not any(task["name"] == "Temp" for task in list_tasks())
