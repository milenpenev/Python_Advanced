from pprint import pprint
number_of_rows = 6
number_of_cols = 7

down = right = 1
left = up = -1
stay = 0


def find_empty_space(board, column):
    for row in range(0, number_of_rows):
        if not board[row][column] == 0:
            return row -1
    return number_of_rows -1


def is_stalemate(board):
    for row in board:
        for col in row:
            if col == 0:
                return False
    return True


def get_positions_in_directions(board, last_position, direction):
    start_row, start_col = last_position
    move_by_row, move_by_col = direction
    positions = []

    current_row, current_col = start_row, start_col

    for _ in range(3):
        current_row += move_by_row
        current_col += move_by_col
        if not 0 <= current_row < len(board):
            return positions
        if not 0 <= current_col < len(board[current_row]):
            return positions

        positions.append(board[current_row][current_col])

    return positions


def has_four_consecutive(target_line, target):
    count = 0
    for el in target_line:
        if el == target:
            count += 1
        else:
            count = 0
        if count == 4:
            return True
    return False


def has_player_won(board, last_position):
    left_horizont = (stay, left)
    right_horizont = (stay, right)
    up_vertical = (up, stay)
    down_vertical = (down, stay)
    up_right_vertical = (up, right)
    up_left_vertical = (up, left)
    down_left_vertical = (down, left)
    down_right_vertical = (down, right)

    start_row, start_col = last_position

    directions = [
        (left_horizont, right_horizont),
        (up_vertical, down_vertical),
        (down_left_vertical, up_right_vertical),
        (up_left_vertical, down_right_vertical)
    ]

    for backward_direction, forward_direction in directions:
        backwards_positions = get_positions_in_directions(board, last_position, backward_direction)
        forward_positions = get_positions_in_directions(board, last_position, forward_direction)

        target_line = list(reversed(backwards_positions)) + [board[start_row][start_col]] + forward_positions

        if has_four_consecutive(target_line, target= board[start_row][start_col]):
            return True
    return False



# def has_player_won(board, last_position):
#     directions = [
#         (stay, right),
#         (down, right),
#         (down, stay),
#         (down, left),
#         (stay, left),
#         (up, left),
#         (up, right)
#
#     ]
#     last_row, last_col = last_position
#     for direction in directions:
#         positions = get_positions_in_directions(board, last_position, direction)
#         if len(positions) == 4 and all([pos == board[last_row][last_col] for pos in positions ]):
#             return True
#     return False


def main():
    board = [[0] * number_of_cols for _ in range(number_of_rows)]
    pprint(board)
    current_player, opponent = 1, 2
    while True:
        try:
            column = int(input())
        except ValueError:
            continue
        column -= 1

        if not 0 <= column < number_of_cols:
            continue
        row = find_empty_space(board, column)

        if row == -1:
            continue

        board[row][column] = current_player
        if is_stalemate(board):
            print("Stalemate - no empty spots")
            break
        if has_player_won(board, (row, column)):
            print(f"Player {current_player} has won!")
            break
        pprint(board)
        current_player, opponent = opponent, current_player


main()