n = int(input())

even_ones = set()
odd_ones = set()
index = 0
sum_of_chars = 0

for _ in range(n):
    name = input()
    index += 1
    for char in name:
        sum_of_chars += int(ord(char))
    sum_of_chars //= index
    if sum_of_chars % 2 == 0:
        even_ones.add(sum_of_chars)
    else:
        odd_ones.add(sum_of_chars)

    sum_of_chars = 0

if sum(even_ones) == sum(odd_ones):
    result = odd_ones.union(even_ones)
elif sum(odd_ones) > sum(even_ones):
    result = odd_ones.difference(even_ones)
elif sum(even_ones) > sum(odd_ones):
    result = odd_ones.symmetric_difference(even_ones)

print(', '.join([str(x) for x in result]))