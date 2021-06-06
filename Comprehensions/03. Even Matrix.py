n = int(input())

matrix = []

for row in range(n):
    matrix.append([int(el) for el in input().split(", ")])

even_matrix = [[el for el in substring if el % 2 == 0] for substring in matrix]

print(even_matrix)