rows = int(input())

matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split()])

first_sum = 0
second_sum = 0

for row in range(rows):
    for col in range(rows):
        if row == col:
            first_sum += matrix[row][col]

matrix_reverse = matrix.copy()
matrix_reverse.reverse()

for row in range(rows):
    for col in range(rows):
        if row == col:
            second_sum += matrix_reverse[row][col]
print(abs(second_sum - first_sum))