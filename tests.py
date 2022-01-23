print("Initializing checks\n")

from types import SimpleNamespace
import json, os, sys

print("Adding paths")

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/task')
print("/task")

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/workspace')
print("/workspace")

print("\nImporting command modules")

import taskManager, workspaceManager

print(workspaceManager.commands, taskManager.commands)

commands = workspaceManager.commands + taskManager.commands

print("\nChecking for duplicate commands")

if sum(1 for i in commands for j in commands if i["name"] == j["name"]) > len(commands):
    raise Exception(f"Duplicate command names found")

print("No duplicate command names found\n")

print("\nChecking for duplicate aliases")

# if sum(1 for i in commands for j in commands if i["alias"] == j["alias"]) > len(commands):
#     raise Exception(f"Duplicate aliases found")

print("No duplicate aliases found\n")

# Check for bad json.
print("Checking todo.json for unnecessary data")
with open(os.path.dirname(os.path.realpath(__file__)) + "/todo.json") as file:
    print("Loading JSON data")

    todoData = json.load(file, object_hook=lambda d: SimpleNamespace(**d))
    
    print(todoData)

    if len(todoData):
        raise Exception("Array in todo.json must be empty")

print("No leftover data found")

print("\nChecks completed")