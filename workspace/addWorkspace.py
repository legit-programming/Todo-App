from workspaceData import *
from openWorkspace import openWorkspace

def addWorkspace(name, open):
    data = getTodoData()
    data.append(workspace(name))
    setTodoData(data)

    print(f"[CREATED] {name}")

    if open != "n" or open != "no":
        openWorkspace(name)