sequences = input().split("|")

numbers = [[int(el) for el in seq.split()] for seq in sequences ]
numbers.reverse()
numbers = [str(number) for seq in numbers for number in seq]

print(" ".join(numbers))