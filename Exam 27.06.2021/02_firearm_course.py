all_targets = []
shot_targets = []
matrix = []

for row in range(5):
    matrix.append(input().split())


def check_if_new_position_is_valid(matrix, new_row, new_col):
    if not 0 <= new_row < 5 or not 0 <= new_col < 5:
        return False
    if matrix[new_row][new_col] == ".":
        return True
    return False

def finding_the_player(matrix):
    for row in range(5):
        for col in range(5):
            current_el = matrix[row][col]
            if current_el == "A":
                return row, col

def finding_all_targets(matrix):
    for row in range(5):
        for col in range(5):
            current_el = matrix[row][col]
            if current_el == "x":
                all_targets.append([row, col])
    return all_targets

finding_all_targets(matrix)
n = int(input())
for commands in range(n):
    if len(all_targets) == len(shot_targets):
        break
    command = input().split()
    action, direction = command[0], command[1]
    current_player_position = finding_the_player(matrix)
    if action == 'move':
        steps = int(command[2])
        if direction == "up":
            new_row, new_col = -steps, 0
        elif direction == "down":
            new_row, new_col = steps, 0
        elif direction == "right":
            new_row, new_col = 0, steps
        elif direction == "left":
            new_row, new_col = 0, -steps
        old_row, old_col = current_player_position
        new_row += old_row
        new_col += old_col
        if check_if_new_position_is_valid(matrix, new_row, new_col):
            matrix[new_row][new_col] = "A"
            matrix[old_row][old_col] = "."
    if action == "shoot":
        row, col = current_player_position
        if direction == "up":
            for target in range(row+1):
                current_row = row - target
                if matrix[current_row][col] == 'x':
                    matrix[current_row][col] = '.'
                    shot_targets.append([current_row, col])
                    break
        elif direction == "down":
            possible_targets = 5 - row
            for target in range(possible_targets):
                current_row = row + target
                if matrix[current_row][col] == 'x':
                    matrix[current_row][col] = '.'
                    shot_targets.append([current_row, col])
                    break
        elif direction == "right":
            possible_targets = 5 + col
            for target in range(possible_targets):
                current_col = col + target
                if matrix[row][current_col] == 'x':
                    matrix[row][current_col] = '.'
                    shot_targets.append([row, current_col])
                    break
        elif direction == "left":
            for target in range(col, -1, -1):
                current_col = target
                if matrix[row][current_col] == 'x':
                    matrix[row][current_col] = '.'
                    shot_targets.append([row, current_col])
                    break

if len(all_targets) == len(shot_targets):
    print(f"Training completed! All {len(all_targets)} targets hit.")
    if shot_targets:
        [print(el) for el in shot_targets]
else:
    print(f'Training not completed! {len(all_targets) - len(shot_targets)} targets left.')
    if shot_targets:
        [print(el) for el in shot_targets]