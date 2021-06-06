n = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

first_diag = [matrix[i][i] for i in range(n)]
second_diag = [matrix[i][n-1-i] for i in range(n)]
print(f'First diagonal: {", ".join(str(el) for el in first_diag)}. Sum: {sum(first_diag)}')
print(f'Second diagonal: {", ".join(str(el) for el in second_diag)}. Sum: {sum(second_diag)}')