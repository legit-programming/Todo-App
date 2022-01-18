from types import SimpleNamespace
from datetime import datetime
import json
import os

def getTodoData():
    # Read the todo data
    with open(os.path.dirname(os.path.realpath(__file__)) + "\\..\\todo.json") as file:
        data = json.load(file, object_hook=lambda d: SimpleNamespace(**d))
    return data

def setTodoData(data):
    with open(os.path.dirname(os.path.realpath(__file__)) + "\\..\\todo.json", "w") as file:
        json.dump(data, file, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)

class Todo:
    def __init__(self, task, description, priority):
        self.task = task
        self.description = description
        self.priority = priority
        self.done = False
        self.id = getTodoData().id
        self.createDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")