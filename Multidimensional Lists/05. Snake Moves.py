rows, cols = [int(el) for el in input().split()]

matrix = []
string = list(input())
current_pos = 0

for row in range(rows):
    matrix.append([0 for el in range(cols)])

for row in range(rows):
    for col in range(cols):
        matrix.append([])
        matrix[row][col] = string[current_pos]
        current_pos += 1
        if current_pos == len(string):
            current_pos = 0
for row in range(rows):
    if row % 2 == 1:
        matrix[row].reverse()
    print("".join(matrix[row]))