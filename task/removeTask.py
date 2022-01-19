from todoData import getTodoData, setTodoData, os

def removeTask(id):
    if "-" not in id and "." not in id and id.isdigit():
        id = int(id)
    else:
        print("Invalid id.")
        return

    index, todoData = getTodoData(os.environ["workspace"])

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
    
    setTodoData(todoData, index)