from todoData import getTodoData, setTodoData

def removeTask(id):
    if "-" not in id and "." not in id and id.isdigit():
        id = int(id)
        
        if id < 0 or id > 4:
            print("ID must be between 0 and 4.")
            return
    else:
        print("Invalid id.")
        return

    todoData = getTodoData()

    for i, o in enumerate(todoData.tasks):
        if o.id == id:
            print(f"[DELETED] <{o.createDate}> ({o.priority}) {o.task} {o.description}")
            del todoData.tasks[i]
            break
    
    for i, o in enumerate(todoData.completed):
        if o.id == id:
            print(f"[DELETED] <{o.createDate}> ({o.priority}) {o.task} {o.description}")
            del todoData.tasks[i]
            break
    
    setTodoData(todoData)