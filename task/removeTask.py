from todoData import getTodoData, setTodoData

def removeTask(id):
    todoData = getTodoData()

    for i, o in enumerate(todoData.tasks):
        if o.id == id:
            del todoData.tasks[i]
            break
    
    for i, o in enumerate(todoData.completed):
        if o.id == id:
            del todoData.tasks[i]
            break
    
    setTodoData(todoData)