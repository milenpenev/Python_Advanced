player_one = 501
player_two = 501
player_one_name, player_two_name = input().split(", ")
round = 0

player_one_tries = 0
player_two_tries = 0
valid_coordinates = True


matrix = []
for row in range(7):
    matrix.append(input().split())


while player_one > 0 and player_two > 0:
    coordinates = input()
    if "-" in coordinates:
        if round % 2 == 0:
            player_one_tries += 1
            round += 1
        else:
            player_two_tries += 1
            round += 1
        continue
    x, y = [int(el) for el in coordinates[1:-1].split(", ")]
    if x >= 7 or y >= 7 or x < 0 or y < 0:
        if round % 2 == 0:
            player_one_tries += 1
            round += 1
        else:
            player_two_tries += 1
            round += 1
        continue
    if round % 2 == 0:
        player_one_tries += 1
        player_one_current_score = matrix[x][y]
        if player_one_current_score == "B":
            player_one = -1
        elif player_one_current_score == "T":
            player_one_current_score = (int(matrix[x][0]) + int(matrix[0][y]) + int(matrix[x][6]) + int(matrix[6][y])) * 3
            player_one -= player_one_current_score
            player_one_current_score = 0
        elif player_one_current_score == "D":
            player_one_current_score = (int(matrix[x][0]) + int(matrix[0][y]) + int(matrix[x][6]) + int(matrix[6][y])) * 2
            player_one -= player_one_current_score
            player_one_current_score = 0
        elif player_one_current_score.isdigit():
            player_one_current_score = int(player_one_current_score)
            player_one -= player_one_current_score
            player_one_current_score = 0
    else:
        player_two_tries += 1
        player_two_current_score = matrix[x][y]
        if player_two_current_score == "B":
            player_two = -1
        elif player_two_current_score == "T":
            player_two_current_score = (int(matrix[x][0]) + int(matrix[0][y]) + int(matrix[x][6]) + int(
                matrix[6][y])) * 3
            player_two -= player_two_current_score
            player_two_current_score = 0
        elif player_two_current_score == "D":
            player_two_current_score = (int(matrix[x][0]) + int(matrix[0][y]) + int(matrix[x][6]) + int(
                matrix[6][y])) * 2
            player_two -= player_two_current_score
            player_two_current_score = 0
        elif player_two_current_score.isdigit():
            player_two_current_score = int(player_two_current_score)
            player_two -= player_two_current_score
            player_two_current_score = 0
    round += 1


if player_one <= 0:
    print(f"{player_one_name} won the game with {player_one_tries} throws!")
else:
    print(f"{player_two_name} won the game with {player_two_tries} throws!")