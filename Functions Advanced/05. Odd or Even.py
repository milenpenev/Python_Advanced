command = input()
nums = [int(el) for el in input().split()]

if command == "Even":
    filtered = filter(lambda num: num % 2== 0, nums)
elif command == "Odd":
    filtered = filter(lambda num: num % 2 != 0, nums)

result = sum(filtered) * len(nums)
print(result)