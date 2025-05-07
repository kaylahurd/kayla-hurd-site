class Task:
    def __init__(self, name, priority, status="pending"):
        self.name = name
        self.priority = priority
        self.status = status

    def to_dict(self):
        return {
            "name": self.name,
            "priority": self.priority,
            "status": self.status

        }
