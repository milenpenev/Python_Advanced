number_of_commands = int(input())

stack = []

for i in range(number_of_commands):
    command = input().split()
    if command[0] == "1":
        stack.append(int(command[1]))
    elif command[0] == "2":
        if len(stack) > 0:
            stack.pop()
    elif command[0] == "3":
        if len(stack) > 0:
            print(max(stack))
    elif command[0] == "4":
        if len(stack) > 0:
            print(min(stack))

reversed_numbers = []

for i in range(len(stack)):
    reversed_numbers.append(str(stack.pop()))

print(", ".join(reversed_numbers))