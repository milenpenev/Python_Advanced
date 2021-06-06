rows, cols = [int(el) for el in input().split()]

matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split()])

current_sum = 0
max_sum = 0
max_row, max_col = 0, 0


for row in range(rows-2):
    for col in range(cols-2):
        current_sum = sum([matrix[row][col], matrix[row +1][col], matrix[row+2][col], matrix[row][col+1], \
                      matrix[row][col +2], matrix[row +1][col+1], matrix[row+1][col+2] \
                      , matrix[row+2][col+2], matrix[row +2][col +1]])
        if current_sum > max_sum:
            max_sum = current_sum
            max_row, max_col = row, col
print(f"Sum = {max_sum}")

for row in range(3):
    for col in range(3):
        print(matrix[max_row+row][max_col + col],end=" ")

    print("")
