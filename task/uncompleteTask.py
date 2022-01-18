from todoData import getTodoData, setTodoData

def uncompleteTask(id):
    if "-" not in id and "." not in id and id.isdigit():
        id = int(id)
        
        if id < 0 or id > 4:
            print("ID must be between 0 and 4.")
            return
    else:
        print("Invalid id.")
        return

    todoData = getTodoData()
    
    for i, o in enumerate(todoData.completed):
        if o.id == id:
            todoData.completed[i].done = False
            todoData.tasks.append(todoData.completed[i])
            del todoData.completed[i]
            break

    setTodoData(todoData)