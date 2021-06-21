from Workshop.core.constans import position_mapper


def is_board_full(board):
    is_full = True
    for row in board:
        if " " in row:
            is_full = False
    return is_full

def print_current_board_state(board):
    [print(f"| {' | '.join(el)} |") for el in board]


def get_row_col(position):
    row, col = position_mapper[position]
    return row, col


def is_row_winner(board):
    is_found = False
    for row in board:
        if row.count("X") == len(row) or row.count("O") == len(row):
            is_found = True

    return is_found

def is_col_winner(board):
    is_found = False
    first_col = [board[0][0], board[1][0], board[2][0]]
    second_col = [board[0][1], board[1][1], board[2][1]]
    third_col = [board[0][2], board[1][2], board[2][2]]

    if first_col.count("X") == len(board) or first_col.count('O') == len(board):
        is_found = True
    elif second_col.count("X") == len(board) or second_col.count('O') == len(board):
        is_found = True
    elif third_col.count("X") == len(board) or third_col.count('O') == len(board):
        is_found = True
    return is_found


def is_primary_diagonal_winner(board):
    current_values = []
    for row in range(len(board)):
        current_values.append(board[row][row])
    if current_values.count('X') == len(board) or current_values.count('O') == len(board):
        return True
    return False


def is_secondary_diagonal_winner(board):
    current_values = []
    n = len(board)
    for index in range(n):
        current_values.append(board[n-index-1][index])
    if current_values.count('X') == len(board) or current_values.count('O') == len(board):
        return True
    return False


def is_winner(board):
    if is_row_winner(board):
        return True
    elif is_col_winner(board):
        return True
    elif is_primary_diagonal_winner(board):
        return True
    elif is_secondary_diagonal_winner(board):
        return True
    elif is_board_full(board):
        print("No winner!")
    return False