from collections import deque

names = input().split()
steps = int(input())

circle = deque(names)

counter = 0

while len(circle) > 1:
    counter += 1
    current_name = circle.popleft()
    if counter == steps:
        print(f"Removed {current_name}")
        counter = 0
    else:
        circle.append(current_name)
print(f"Last is {circle.popleft()}")