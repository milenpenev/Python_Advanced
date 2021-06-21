from Workshop.core.constans import position_mapper


def print_current_board_state(board):
    [print(f"| {' | '.join(el)} |") for el in board]


def get_row_col(position):
    row, col = position_mapper[position]
    return row, col