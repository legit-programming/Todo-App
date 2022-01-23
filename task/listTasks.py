from todoData import getTodoData, os

def listTasks(sortBy, direction):
    if direction == "up":
        direction = True
    elif direction == "down":
        direction = False
    else:
        direction = True

    _, todoData = getTodoData(os.environ["workspace"])
    if sortBy == "priority":
        todoData.tasks.sort(key=lambda x: x.priority, reverse=direction)
    elif sortBy == "date":
        todoData.tasks.sort(key=lambda x: x.createDate, reverse=direction)
    elif sortBy == "id":
        todoData.tasks.sort(key=lambda x: x.id, reverse=direction)

    print("")
    for i, o in enumerate(todoData.tasks):
        print(f"{i}: [{o.id}] <{o.createDate}> ({o.priority}) {o.task} {o.description}")