import sys
import os
sys.path.append('./task')
sys.path.append('./workspace')
import taskManager
import workspaceManager

os.environ["workspace"] = ""

def main():
    print("\nLegit Programming Todo-App\n\n(q) exit: exit the app\n(h) Help information")
    for i in workspaceManager.commands + taskManager.commands:
        print(f"({i['alias'][0] if len(i['alias']) and len(i['alias'][0]) == 1 else ' '}) {i['name']}: {i['description']}")

    while True:
        print("")
        args = input("> ").split(" ")
        command = args.pop(0).lower()
        print("")

        # Check for command.

        if os.environ["workspace"]:
            for i in taskManager.commands:
                if command in i["alias"] or command == i["name"]:
                    i["function"]()
                    break

        for i in workspaceManager.commands:
            if command in i["alias"] or command == i["name"]:
                i["function"]()
                break
        
        # Check for help and exit.
        if command == "help" or command == "h":
            if len(args):
                for i, o in enumerate(workspaceManager.commands + taskManager.commands):
                    if o["name"] == args[0]:
                        print(f"{o['name']}:\n{o['help']}")
                        break
            else:
                print("(q) exit: exit the app\n(h) Help information")
                for i in workspaceManager.commands + taskManager.commands:
                    print(f"({i['alias'][0] if len(i['alias']) and len(i['alias'][0]) == 1 else ' '}) {i['name']}: {i['description']}")
        elif command == "exit" or command == "q":
            print("Exiting...")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()
    except EOFError:
        print("\nExiting...")
        exit()