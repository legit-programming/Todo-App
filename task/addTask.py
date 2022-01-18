from todoData import getTodoData, setTodoData, Todo

def addTask(task, description, priority):
    if "-" not in priority and "." not in priority and priority.isdigit():
        priority = int(priority)
        
        if priority < 0 or priority > 4:
            print("Priority must be between 0 and 4.")
            return
    else:
        print("Invalid priority.")
        return

    todoData = getTodoData()
    todoData.tasks.append(Todo(task, description, priority))
    todoData.id += 1

    setTodoData(todoData)