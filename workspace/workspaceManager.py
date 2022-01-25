from openWorkspace import openWorkspace
from closeWorkspace import closeWorkspace
from addWorkspace import addWorkspace
import os

commands = [
    {
        "name": "open",
        "description": "Open a workspace",
        "alias": ["o"],
        "help": "",
        "function": lambda: openWorkspace(input("Workspace name: ")),
        "source": openWorkspace
    },
    {
        "name": "close",
        "description": "Close a workspace",
        "alias": [],
        "help": "",
        "function": lambda: closeWorkspace(),
        "source": closeWorkspace
    },
    {
        "name": "create",
        "description": "Add a new workspace",
        "alias": [],
        "help": "(string) Workspace name: [the name of the workspace]\n(yes, no) Open: [(y) yes | (n) no]",
        "function": lambda: addWorkspace(input("Workspace name: "), input("Open: ")),
        "source": addWorkspace
    },
    {
        "name": "current",
        "description": "Show the current workspace",
        "alias": ["opened"],
        "help": "",
        "function": lambda: print(os.environ["workspace"] or "No workspace opened"),
        "source": print
    }
]