rows, cols = [int(el) for el in input().split(", ")]

matrix = []
result = 0

for row in range(rows):
    matrix.append([int(el) for el in input().split(" ")])

for col in range(cols):
    for row in range(rows):
        result += matrix[row][col]
    print(result)
    result = 0