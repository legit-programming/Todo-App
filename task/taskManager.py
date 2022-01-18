from addTask import addTask
from removeTask import removeTask
from completeTask import completeTask
from uncompleteTask import uncompleteTask
from listTasks import listTasks

commands = [
    {
        "name": "add",
        "description": "Add a task",
        "alias": ["a"],
        "function": lambda: addTask(input("Task: "), input("Description: "), input("(0 <= integer <= 4) Priority: "))
    },
    {
        "name": "remove", "description": "Remove a task", "alias": ["r"], "function": lambda: removeTask(int(input("ID: ")))},
    {
        "name": "complete",
        "description": "Complete a task",
        "alias": ["c", "resolve"],
        "function": lambda: completeTask(int(input("ID: ")))
    },
    {
        "name": "uncomplete",
        "description": "Uncomplete a task",
        "alias": ["u", "incomplete"],
        "function": lambda: uncompleteTask(int(input("ID: ")))
    },
    {
        "name": "list",
        "description": "List the active tasks",
        "alias": ["l"],
        "function": lambda: listTasks(input("(priority | date | id) Sort by: "), input("(up | down) Direction: "))
    }
]