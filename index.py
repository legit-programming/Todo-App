import sys
sys.path.append('./task')
from taskManager import commands

def main():
    print("Legit Programming Todo-App\n(q) exit: exit the app")
    for i in commands:
        print(f"({i['alias'][0]}) {i['name']}: {i['description']}")
    print("")

    while True:
        print("")
        args = input("> ").split(" ")
        command = args.pop(0).lower()
        print("")

        # Check for command.
        for i in commands:
            if command in i["alias"] or command == i["name"]:
                i["function"]()
                break
        
        # Check for help and exit.
        if command == "help" or command == "h":
            if len(args):
                for i, o in enumerate(commands):
                    if o["name"] == args[0]:
                        print(f"{o['name']}:\n{o['help']}")
                        break
            else:
                for i in commands:
                    print(f"({i['alias'][0]}) {i['name']}: {i['description']}")
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
        pass