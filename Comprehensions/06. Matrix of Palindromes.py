rows, cols = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        first_letter = chr(row + 97)
        middle_letter = chr(row + col+ 97)
        matrix[-1].append(f"{first_letter}{middle_letter}{first_letter}")
print("\n".join(" ".join([str(el) for el in row]) for row in matrix))
