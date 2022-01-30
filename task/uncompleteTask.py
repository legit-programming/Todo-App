from todoData import getTodoData, setTodoData, os

def uncompleteTask(id):
    if not os.environ["workspace"]:
        return print("No workspace opened.")
        
    if "-" not in id and "." not in id and id.isdigit():
        id = int(id)
    else:
        return print("Invalid id.")

    index, todoData = getTodoData(os.environ["workspace"])
    
    for i, o in enumerate(todoData.completed):
        if o.id == id:
            todoData.completed[i].done = False
            todoData.tasks.append(todoData.completed[i])
            del todoData.completed[i]
            break

    setTodoData(todoData, index)