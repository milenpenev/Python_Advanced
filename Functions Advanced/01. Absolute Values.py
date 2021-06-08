def make_absolute(seq):
    return [abs(el) for el in seq]

nums = [float(el) for el in input().split()]

print(make_absolute(nums))