from todoData import getTodoData

def listTasks(sortBy, direction):
    if direction == "up":
        direction = True
    elif direction == "down":
        direction = False
    else:
        print("Sort defaulting to up.")
        direction = True

    todoData = getTodoData()
    if sortBy == "priority":
        todoData.tasks.sort(key=lambda x: x.priority, reverse=direction)
    elif sortBy == "date":
        todoData.tasks.sort(key=lambda x: x.createDate, reverse=direction)
    elif sortBy == "id":
        todoData.tasks.sort(key=lambda x: x.id, reverse=direction)
    else:
        print("Invalid sortBy value.")
        return

    for i, o in enumerate(todoData.tasks):
        print(f"{i}: [{o.id}] <{o.createDate}> ({o.priority}) {o.task} {o.description}")