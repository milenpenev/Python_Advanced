words = input().split()

output = [el for el in words if len(el) % 2 == 0]
print("\n".join(output))