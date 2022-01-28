from help import help
from quit import quitApp

commands = [
    {
        "name": "help",
        "description": "Show the help information.",
        "alias": ["h"],
        "help": "",
        "function": lambda: help(input("command: ")),
        "source": help
    },
    {
        "name": "quit",
        "description": "Exit the app.",
        "alias": ["q"],
        "help": "",
        "function": lambda: quitApp(),
        "source": quitApp
    }
]