text = input()

stack = []

for i in range(len(text)):
    char = text[i]
    if char == "(":
        stack.append(i)
    elif char == ")":
        j = stack.pop()
        print(text[j:i + 1])
