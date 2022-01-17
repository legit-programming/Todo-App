from json import load, dump
from types import SimpleNamespace

def getTodoData():
    # Read the todo data
    with open("todo.json") as file:
        data = load(file, object_hook=lambda d: SimpleNamespace(**d))
    
    return data

def setTodoData(data):
    with open("todo.json", "w") as file:
        dump(data, file, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)

def main():
    print("Legit Programming Todo-App!\n")
    print("(A)dd Todo, (V)iew Todos, (M)ark Todo, (U)pdate Todo")
    print("Enter a command: ")

if __name__ == "__main__":
    main()