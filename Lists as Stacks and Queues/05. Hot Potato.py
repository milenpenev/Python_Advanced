# from collections import deque
#
# names = input().split()
# steps = int(input())
#
# circle = deque(names)
#
# counter = 0
#
# while len(circle) > 1:
#     counter += 1
#     current_name = circle.popleft()
#     if counter == steps:
#         print(f"Removed {current_name}")
#         counter = 0
#     else:
#         circle.append(current_name)
# print(f"Last is {circle.popleft()}")
from collections import deque
children = deque(input().split())
count = int(input())
while len(children) > 1:
    children.rotate(-count)
    print(f"Removed {children.pop()}")

print(f"Last is {children.pop()}")