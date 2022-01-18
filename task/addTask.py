from todoData import getTodoData, setTodoData, Todo

def addTask(task, description, priority):
    todoData = getTodoData()
    todoData.tasks.append(Todo(task, description, priority))
    todoData.id += 1
    setTodoData(todoData)