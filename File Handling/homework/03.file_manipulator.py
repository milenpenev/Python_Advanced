import os

line = input()
while not line == "End":
    command, *rest = line.split("-")
    if command == "Add":
        filename, line = rest
        with open(filename, "a") as file:
            file.write(line + "\n")
    elif command == "Replace":
        filename, old, new = rest
        try:
            with open(filename, "r") as file:
                content = file.read()
            with open(filename, "w") as file:
                content = content.replace(old, new)
                file.write(content)
        except:
            print("An error occurred")
            line = input()
            continue
    elif command == "Create":
        with open(rest[0], 'w'):
            pass
    elif command == "Delete":
        try:
            os.remove(rest[0])
        except FileNotFoundError:
            print("An error occurred")
    line = input()