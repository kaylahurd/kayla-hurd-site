from routes.task_routes import create_task, list_tasks, delete_task

print("🟢 TaskHQ App Running...")

# Create some tasks
create_task("Submit report", "high", "in progress")
create_task("Fix login bug", "medium", "pending")

# Print all tasks
print("\n📋 All Tasks:")
print(list_tasks())

# Delete one task
delete_task("Submit report")

# Print tasks again
print("\n📋 Updated Tasks:")
print(list_tasks())
