from json import load, dump
import os
from types import SimpleNamespace
from datetime import datetime

def getTodoData():
    # Read the todo data
    with open(os.path.dirname(os.path.realpath(__file__)) + "\\todo.json") as file:
        data = load(file, object_hook=lambda d: SimpleNamespace(**d))
    return data

def setTodoData(data):
    with open(os.path.dirname(os.path.realpath(__file__)) + "\\todo.json", "w") as file:
        dump(data, file, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)

class Todo:
    def __init__(self, task, description, priority):
        self.task = task
        self.description = description
        self.priority = priority
        self.done = False
        self.id = getTodoData().id
        self.createDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def addTask(task, description, priority):
    todoData = getTodoData()
    todoData.tasks.append(Todo(task, description, priority))
    todoData.id += 1
    setTodoData(todoData)

def removeTask(id):
    todoData = getTodoData()
    for i, o in enumerate(todoData.tasks):
        if o.id == id:
            del todoData.tasks[i]
            break
    for i, o in enumerate(todoData.completed):
        if o.id == id:
            del todoData.tasks[i]
            break
    setTodoData(todoData)

def completeTask(id):
    todoData = getTodoData()
    for i, o in enumerate(todoData.tasks):
        if o.id == id:
            todoData.tasks[i].done = True
            todoData.completed.append(todoData.tasks[i])
            del todoData.tasks[i]
            break
    setTodoData(todoData)

def uncompleteTask(id):
    todoData = getTodoData()
    for i, o in enumerate(todoData.completed):
        if o.id == id:
            todoData.completed[i].done = False
            todoData.tasks.append(todoData.completed[i])
            del todoData.completed[i]
            break
    setTodoData(todoData)

def listTasks():
    todoData = getTodoData()
    for i, o in enumerate(todoData.tasks):
        print(f"{i}: [{o.id}] <{o.createDate}> {o.task}")

def main():
    print("Legit Programming Todo-App!\n")
    commands = [
        {"name": "add", "description": "Add a task", "alias": ["a"], "function": lambda: addTask(input("Task: "), input("Description: "), int(input("Priority: ")))},
        {"name": "remove", "description": "Remove a task", "alias": ["r"], "function": lambda: removeTask(int(input("ID: ")))},
        {"name": "complete", "description": "Complete a task", "alias": ["c", "resolve"], "function": lambda: completeTask(int(input("ID: ")))},
        {"name": "uncomplete", "description": "Uncomplete a task", "alias": ["u", "incomplete"], "function": lambda: uncompleteTask(int(input("ID: ")))},
        {"name": "list", "description": "List the active tasks", "alias": ["l"], "function": lambda: listTasks()}
    ]
    
    while (True):
        command = input("> ")

        # Check for command.
        for i in commands:
            if command in i["alias"] or command == i["name"]:
                i["function"]()
                break
        
        # Check for help and exit.
        if command == "help":
            for i in commands:
                print(f"{i['name']}: {i['description']}")
        elif command == "exit":
            print("Exiting...")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()