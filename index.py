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
        self.id = getTodoData().id
        self.createDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def addTask(task):
    todoData = getTodoData()
    todoData.tasks.append(Todo(task))
    todoData.id += 1
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
    print("(a)dd Todo, (v)iew Todos, (m)ark Todo, (u)pdate Todo\n")
    
    while (True):
        command = input("> ")
        if command == "help":
            print("(a)dd Todo, (v)iew Todos, (m)ark Todo, (u)pdate Todo\n")
        elif command == "a":
            task = input("Task: ")
            addTask(task)
        elif command == "r":
            id = int(input("ID: "))
            removeTask(id)
        elif command == "exit":
            print("Exiting...")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()