n = int(input())

matrix = []

for row in range(n):
    matrix.append([int(el) for el in input().split(", ")])

print([int(el) for submatrix in matrix for el in submatrix])