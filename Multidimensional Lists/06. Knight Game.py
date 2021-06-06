def read_board():
    matrix = []
    n = int(input())

    for _ in range(n):
        matrix.append(list(input()))

    return matrix


def knights_are_attacking_each_other(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "K":
                positions_to_be_checked = [
                    (row-2, col+1),
                    (row-1, col+2),
                    (row+1, col+2),
                    (row+2, col+1),
                    (row+2, col-1),
                    (row+1, col-2),
                    (row-1, col-2),
                    (row-2, col-1),
                ]
                for position in positions_to_be_checked:
                    pos_row, pos_col = position
                    if not(0 <= pos_row <= len(matrix)-1):
                        continue
                    if not(0 <= pos_col <= len(matrix) - 1):
                        continue
                    if matrix[pos_row][pos_col] == "K":
                        return True
    return False


def find_all_knights(matrix):
    positions = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "K":
                positions.append((i, j))
    return positions


def calculate_aggression(matrix, knight_positions):
    aggression_scores = {}
    for pos in knight_positions:
        row, col = pos
        positions_to_be_checked = [
            (row - 2, col + 1),
            (row - 1, col + 2),
            (row + 1, col + 2),
            (row + 2, col + 1),
            (row + 2, col - 1),
            (row + 1, col - 2),
            (row - 1, col - 2),
            (row - 2, col - 1)
        ]
        attacked_count = 0
        for attacked_row, attacked_col in positions_to_be_checked:
            if not (0 <= attacked_row <= len(matrix) - 1):
                continue
            if not (0 <= attacked_col <= len(matrix) - 1):
                continue
            if matrix[attacked_row][attacked_col] == "K":
                attacked_count += 1
        aggression_scores[(row, col)] = attacked_count

    return aggression_scores


def find_max_aggression(aggression_score):
    max_so_far = None
    max_pos = None

    for pos, aggression in aggression_score.items():
        if max_so_far is None or max_so_far < aggression:
            max_so_far = aggression
            max_pos = pos

    return max_pos


def main():
    matrix = read_board()

    deleted_knights_count = 0
    while knights_are_attacking_each_other(matrix) is True:
        knight_positions = find_all_knights(matrix)
        aggression_score = calculate_aggression(matrix, knight_positions)

        row, col = find_max_aggression(aggression_score)

        matrix[row][col] = "0"
        deleted_knights_count += 1

    print(deleted_knights_count)


main()
