import sys
sys.path.append('./task')
from taskManager import commands

def main():
    print("Legit Programming Todo-App\n")
    
    while (True):
        command = input("> ")

        # Check for command.
        for i in commands:
            if command in i["alias"] or command == i["name"]:
                i["function"]()
                break
        
        # Check for help and exit.
        if command == "help" or command == "h":
            for i in commands:
                print(f"{i['name']}: {i['description']}")
        elif command == "exit" or command == "e":
            print("Exiting...")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()