print("Initializing checks")

from types import SimpleNamespace
import json
import os
import sys
sys.path.append('./task')
sys.path.append('./workspace')
import taskManager
import workspaceManager

# Check for duplicate commands.
print("Checking for duplicate commands\n")
for i in workspaceManager.commands + taskManager.commands:
    print(i)

    for j, o in enumerate(workspaceManager.commands + taskManager.commands):
        print("comparing: " + i["name"] + " and " + o["name"])
        
        if o["name"] != i["name"]:
            for k in i["alias"]:
                if i in o["alias"]:
                    raise Exception(f"Duplicate alias: {k} in {i['name']} and {o['name']}")

# Check for bad json.
print("Checking todo.json for unnecessary data\n")
with open(os.path.dirname(os.path.realpath(__file__)) + "/todo.json") as file:
    todoData = json.load(file, object_hook=lambda d: SimpleNamespace(**d))
    print(todoData)

    if len(todoData):
        raise Exception("Array in todo.json must be empty")

print("Checks completed")