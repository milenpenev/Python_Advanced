from collections import deque

start_command = "Start"
end_command = "End"
refill_command = "refill"

amount_of_water = int(input())

people_queue = deque()

while True:
    command = input()
    if command == start_command:
        break
    people_queue.append(command)

while True:
    command = input()
    if command == end_command:
        print(f"{amount_of_water} liters left")
        break
    if command.startswith(refill_command):
        amount_of_refill = command.split()
        refill_liters = int(amount_of_refill[1])
        amount_of_water += refill_liters
    else:
        person = people_queue.popleft()
        person_liters = int(command)
        if person_liters <= amount_of_water:
            print(f"{person} got water")
            amount_of_water -= person_liters
        else:
            print(f"{person} must wait")
# from collections import deque
#
# liters = int(input())
#
# name = input()
# queue = deque()
#
#
# command = input()
# while not name == "Start":
#     if command.startswith("refill"):
#         liters += int(command.split()[-1])
#     else:
#         liters_wanted = int(command)
#         name = queue.popleft()
#         if liters >= liters_wanted:
#             liters -= liters_wanted
#             print(f"{name} got water")
#         else:
#             print(f"{name} must wait")
#     queue.append(name)
#     name = input()