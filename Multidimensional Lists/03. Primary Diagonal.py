n = int(input())

matrix = []
result = 0
for row in range(n):
    col = input().split()
    matrix.append(col)
    for el in range(len(col)):
        if el == row:
            result += int(matrix[row][el])

print(result)