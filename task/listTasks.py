from todoData import getTodoData

def listTasks():
    todoData = getTodoData()
    for i, o in enumerate(todoData.tasks):
        print(f"{i}: [{o.id}] <{o.createDate}> {o.task}")