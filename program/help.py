import sys, os

for i in ["../task", "../workspace"]:
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + i)

import taskManager, workspaceManager
import programManager

def help(command=None):
    commands = workspaceManager.commands + taskManager.commands + programManager.commands
    
    if command:
        for i, o in enumerate(commands):
            if o["name"] == command:
                print(f"{'(' + (') ('.join(o['alias']) or ' ') + ')' } {o['name']}: {o['description']}\n{o['help']}")
                break
        else:
            print("Command not found.")
    else:
        for i in commands:
            print(f"({i['alias'][0] if len(i['alias']) and len(i['alias'][0]) == 1 else ' '}) {i['name']}: {i['description']}")