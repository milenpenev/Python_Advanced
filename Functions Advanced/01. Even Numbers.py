def is_even(num):
    return num % 2 == 0

nums = [int(el) for el in input().split()]


print(list(filter(is_even, nums)))