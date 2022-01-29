import sys, os

for i in ["/task", "/workspace", "/program"]:
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + i)

import taskManager, workspaceManager, programManager

commands = workspaceManager.commands + taskManager.commands + programManager.commands

os.environ["workspace"] = ""

def main():
    print("\nLegit Programming Todo-App\n\n")
    for i in commands:
        print(f"({i['alias'][0] if len(i['alias']) and len(i['alias'][0]) == 1 else ' '}) {i['name']}: {i['description']}")

    while True:
        print("")
        args = input("> ").split(" ")
        command = args.pop(0).lower()
        print("")

        for i in commands:
            if command in i["alias"] or command == i["name"]:
                i["function"]()
                break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt or EOFError:
        print("\nExiting...")
        exit()