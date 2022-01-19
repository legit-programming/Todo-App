from workspaceData import getTodoData
import os

def openWorkspace(workspaceName):
    if not workspaceName:
        print("Workspace name can not be empty")
    
    todoData = getTodoData()
    for i, o in enumerate(todoData):
        if o.name == workspaceName:
            print(f"\n[OPENED] {o.name}")
            os.environ["workspace"] = o.name
            return
    
    print(f"\n[ERROR] Workspace {workspaceName} not found.")