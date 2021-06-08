nums = [int(el) for el in input().split()]


def is_positive(num):
    return num >= 0


def is_negative(num):
    return num < 0


positive = list(filter(is_positive, nums))
negative = list(filter(is_negative, nums))

sum_positive = sum(positive)
sum_negative = sum(negative)

print(sum_negative)
print(sum_positive)

if sum_positive < abs(sum_negative):
    print(f"The negatives are stronger than the positives")
else:
    print(f"The positives are stronger than the negatives")