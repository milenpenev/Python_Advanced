string = input()

stack = []

for ch in string:
    stack.append(ch)

result = ""

while stack:
    result += stack.pop()
print(result)