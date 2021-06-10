matrix = []


for row in range(8):
    matrix.append(input().split())

def finding_the_king(matrix):
    for row in range(8):
        for col in range(8):
            current_el = matrix[row][col]
            if current_el == "K":
                return row, col

# def get_capturint_queens(matrix, king):
#
#     (pos_row, pos_col) = king
#     queens = []
#     for col in range(pos_row +1, 8):
#         if matrix[pos_row][col] == "Q":
#             queens.append((pos_row, col))
#             break
#     for col in range(pos_row -1, -1, -1):
#         if matrix[pos_row][col] == "Q":
#             queens.append((pos_row, col))
#             break
#     for col in range(pos_row -1, -1, -1):
#         if matrix[pos_row][col] == "Q":
#             queens.append((pos_row, col))
#             break
#     return queens

def in_range(value, max_value):
    return  0<=value<max_value


def search_with_deltas(matrix,king,deltas):
    (pos_row, pos_col) = king
    (delta_row, delta_col) = deltas
    while in_range(pos_row, 8) and in_range(pos_col, 8):
        if matrix[pos_row][pos_col] == "Q":
            return pos_row,pos_col
        pos_row += delta_row
        pos_col += delta_col


def get_capturint_queens(matrix, king):



    deltas = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, +1),
        (0, +1),
        (+1, +1),
        (+1, 0),
        (+1, -1)
    ]
    queens = [
        search_with_deltas(matrix,king, delta)
        for delta in deltas
    ]
    return  [queen for queen in queens if queen]


def print_result(queens):
    if queens:
        for queen in queens:
            print(list(queen))
    else:
        print("The king is safe!")


king = finding_the_king(matrix)
queens = get_capturint_queens(matrix,finding_the_king(matrix))
print_result(queens)