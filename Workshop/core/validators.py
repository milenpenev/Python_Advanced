from Workshop.core.helpers import get_row_col

def is_position_in_range(position):
    if 1<= position <= 9:
        return True
    else:
        return False


def is_place_available(board, position):
    row, col = get_row_col(position)
    if not board[row][col] == " ":
        return False
    else:
        return True