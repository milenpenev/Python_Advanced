rows, cols = [int(el) for el in input().split(", ")]

matrix = []
result = 0

for i in range(rows):
    matrix.append([int(el) for el in input().split(", ")])
    result += sum(matrix[i])

print(result)
print(matrix)