rows, cols = [int(el) for el in input().split()]

matrix = []

for row in range(rows):
    matrix.append([el for el in input().split()])

command = None


def coordinates_are_valid(row1, col1, row2, col2):
    if 0 <= row1 <= len(matrix) and 0 <= row2 <= len(matrix) and 0 <= col1 <= len(matrix) and 0 <= col2 <= len(matrix):
        return True
    return False


while not command == "END":
    command = input()
    if command.startswith("swap") and len(command.split()) == 5:
        command, row_1, col_1, row_2, col_2 = command.split()
        row_1, col_1, row_2, col_2 = int(row_1), int(col_1), int(row_2), int(col_2)
        if coordinates_are_valid(row_1, col_1, row_2, col_2):
            matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
            for i in matrix:
                for j in i:
                    print(j, end=" ")
                print()
        else:
            print("Invalid input!")
    elif not command == "END":
        print("Invalid input!")