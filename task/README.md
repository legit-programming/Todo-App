# Task
#### Files for functions for manageing the tasks.
* `index.py` - The main file.
* `task/` - The folder for the task functions.
    * `taskManager.py` - All the funtions get imported here.
* `todo.json` - The json format data for the tasks.
##### Import functions for getting and setting the `todo.json` file:
```python
from todoData import getTodoData, setTodoData, Todo
```
##### Adding a command in `./taskManager.py`:
```python
import FUNCTION from FILE # Import the commands function.

commands = [
    # ...Other commands
    {"name": "NAME", "description": "DESCRIPTION", "alias": ["ALIAS"], "function": lambda: FUNCTION(ARGUMENTS)}
]