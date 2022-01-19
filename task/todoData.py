from types import SimpleNamespace
from datetime import datetime
import json
import os

def getTodoData(workspace):
    # Read the todo data
    with open(os.path.dirname(os.path.realpath(__file__)) + "\\..\\todo.json") as file:
        data = json.load(file, object_hook=lambda d: SimpleNamespace(**d))
    
    if workspace:
        for i, o in enumerate(data):
            if o.name == workspace:
                return (i, o)
        return None
    else:
        return data

def setTodoData(data, index):
    with open(os.path.dirname(os.path.realpath(__file__)) + "\\..\\todo.json", "w") as file:
        if index:
            todoData = getTodoData()
            todoData[index] = data
            data = todoData

        json.dump(data, file, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)

class Todo:
    def __init__(self, task, description, priority):
        self.task = task
        self.description = description
        self.priority = priority
        self.done = False
        self.id = getTodoData(os.environ["workspace"])[1].id
        self.createDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")