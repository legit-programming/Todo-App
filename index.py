from json import load, dump
from types import SimpleNamespace
from datetime import datetime

def getTodoData():
    # Read the todo data
    with open("todo.json") as file:
        data = load(file, object_hook=lambda d: SimpleNamespace(**d))
    return data

def setTodoData(data):
    with open("todo.json", "w") as file:
        dump(data, file, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)

class Todo:
    def __init__(self, task):
        self.task = task
        self.done = False
        self.id = getTodoData().id + 1
        self.createDate = datetime.now()

def addTask(task):
    todoData = getTodoData()
    todoData.tasks.append(Todo(task))
    setTodoData(todoData)

def removeTask(id):
    todoData = getTodoData()
    for i, o in enumerate(todoData.tasks):
        if o.id == id:
            del todoData.tasks[i]
            break
    setTodoData(todoData)

def main():
    print("Legit Programming Todo-App!\n")
    print("(A)dd Todo, (V)iew Todos, (M)ark Todo, (U)pdate Todo\n")
    print("Enter a command: ")

if __name__ == "__main__":
    main()