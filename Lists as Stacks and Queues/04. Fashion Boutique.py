box = []

for clothing in input().split():
    box.append((int(clothing)))
rack_capacity = int(input())

total_racks = 1
current_rack_weight = 0
for i in range(len(box)):
    current_clothing = box.pop()
    if current_rack_weight + current_clothing > rack_capacity:
        total_racks += 1
        current_rack_weight = 0
    else:
        total_racks += 0
    current_rack_weight += current_clothing


print(total_racks)