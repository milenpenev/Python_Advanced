words = input().split(", ")
output = [f"{el} -> {len(el)}" for el in words]
print(", ".join(output))