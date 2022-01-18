print("Initializing checks")

import numpy
import sys
sys.path.append('./task')
from taskManager import commands
from todoData import getTodoData

# Check for duplicate commands.
print("Checking for duplicate commands\n")
for i in commands:
    print(i)

    for j, o in enumerate(commands):
        print("comparing " + i["name"] + " and " + o["name"])
        if o["name"] != i["name"]:
            if numpy.array_equal(i["alias"], o["alias"]):
                raise Exception(f"Duplicate alias: {i['alias']} in {i['name']} and {o['name']}")

# Check for bad json.
print("Checking todo.json for unnecessary data\n")
todoData = getTodoData()
print(todoData)

print("Checking id\n")
if todoData.id != 0:
    raise Exception(f"ID is not 0 (todo.json): {todoData.id}")

print("Checking tasks\n")
if len(todoData.tasks):
    raise Exception(f"Tasks is not empty (todo.json): {todoData.tasks}")

print("Checking completed\n")
if len(todoData.completed):
    raise Exception(f"Completed is not empty (todo.json): {todoData.completedTasks}")

print("todo.json is clean\n")

print("Checks completed")