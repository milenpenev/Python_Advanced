import re

index = 0
with open("input.txt") as file:
    for line in file.readlines():
        if index % 2 == 0:
            line = re.sub(r'[-,.!?]',"@", line)
            print(" ".join(reversed(line.split())))
        index += 1