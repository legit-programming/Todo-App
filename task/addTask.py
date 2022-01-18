from todoData import getTodoData, setTodoData, Todo

def addTask(task, description, priority):
    if not task:
        print("Task name can not be empty")
        return
    
    if not priority:
        priority = 0
    elif "-" not in priority and "." not in priority and priority.isdigit():
        priority = int(priority)
        
        if priority < 0 or priority > 4:
            print("Priority must be between 0 and 4.")
            return
    else:
        print("Invalid priority.")
        return

    todo = Todo(task, description, priority)

    todoData = getTodoData()
    todoData.tasks.append(todo)
    todoData.id += 1

    print(f"\n[CREATED] <{todo.createDate}> ({todo.priority}) {todo.task.capitalize()} {todo.description}")

    setTodoData(todoData)