from math import floor

n = int(input())

result = 0
game_over = False
path = []


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


matrix = []
for row in range(n):
    matrix.append(input().split())


def movement_is_valid(movement):
    if movement == "up" or movement == "down" or movement == "right" or movement == "left":
        return True
    return False


def check_if_new_position_is_valid(matrix, new_row, new_col):
    if not 0 <= new_row < n or not 0 <= new_col < n:
        return False
    if matrix[new_row][new_col] == "X":
        return False
    return True


def finding_the_player(matrix):
    for row in range(n):
        for col in range(n):
            current_el = matrix[row][col]
            if current_el == "P":
                return row, col


while not game_over:
    movement = input()
    if movement_is_valid(movement):
        pass
    else:
        continue
    current_player_position = finding_the_player(matrix)
    new_row, new_col = directions[movement]
    old_row, old_col = current_player_position
    new_row += old_row
    new_col += old_col

    if check_if_new_position_is_valid(matrix, new_row, new_col):
        if movement == "up":
            result += int(matrix[new_row][new_col])
            path.append([new_row, new_col])
            matrix[new_row][new_col] = "P"
            matrix[old_row][old_col] = "-"
        if movement == "down":
            result += int(matrix[new_row][new_col])
            path.append([new_row, new_col])
            matrix[new_row][new_col] = "P"
            matrix[old_row][old_col] = "-"
        if movement == "right":
            result += int(matrix[new_row][new_col])
            path.append([new_row, new_col])
            matrix[new_row][new_col] = "P"
            matrix[old_row][old_col] = "-"
        if movement == "left":
            result += int(matrix[new_row][new_col])
            path.append([new_row, new_col])
            matrix[new_row][new_col] = "P"
            matrix[old_row][old_col] = "-"
    else:
        game_over = True
        result /= 2
        print(f"Game over! You've collected {floor(result)} coins.")
        print("Your path:")
        [print(el) for el in path]
        break
    if result >= 100:
        print(f"You won! You've collected {result} coins.")
        print("Your path:")
        [print(el) for el in path]
        break
