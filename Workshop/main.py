from Workshop.core.logic import play

def print_initial_board_positions():
    print("This is the numeration of the board:")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")


def create_empty_board():
    return [[" "]*3 for _ in range(3)]


def setup():
    player_one = input("Player one name: ")
    player_two = input("Player two name: ")
    player_one_sign = input(f"{player_one}, choose your sign (X or O): ").upper()
    while not player_one_sign in ["X","O"]:
        player_one_sign = input(f"{player_one}, choose your sign (X or O): ").upper()
    player_two_sign = "O" if player_one_sign == "X" else "X"
    print_initial_board_positions()
    print(f"{player_one} starts first!")
    board = create_empty_board()
    turns_mapper = {0: player_two, 1: player_one}
    players = {player_one: player_one_sign, player_two: player_two_sign}
    play(players, board, turns_mapper)

def start_game():
    setup()


if __name__ == "__main__":
    start_game()