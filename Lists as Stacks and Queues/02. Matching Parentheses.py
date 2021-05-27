# text = input()
#
# stack = []
#
# for i in range(len(text)):
#     char = text[i]
#     if char == "(":
#         stack.append(i)
#     elif char == ")":
#         j = stack.pop()
#         print(text[j:i + 1])

expression = input()

stack = []


for index in range(len(expression)):
    if expression[index] == "(":
        stack.append(index)
    elif expression[index] == ")":
        start_index = stack.pop()
        print(expression[start_index: index +1])
