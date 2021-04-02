from collections import deque

end_command = "End"
paid_command = "Paid"

command = input()
names_queue = deque()


while not command == end_command:
    if command == "Paid":
        while names_queue:
            print(names_queue.popleft())
    else:
        names_queue.append(command)
    command = input()

print(f"{len(names_queue)} people remaining.")