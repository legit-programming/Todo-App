from todoData import getTodoData, setTodoData

def uncompleteTask(id):
    todoData = getTodoData()
    
    for i, o in enumerate(todoData.completed):
        if o.id == id:
            todoData.completed[i].done = False
            todoData.tasks.append(todoData.completed[i])
            del todoData.completed[i]
            break

    setTodoData(todoData)