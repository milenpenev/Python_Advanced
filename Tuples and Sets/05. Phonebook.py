
phonebook = {}
is_number = False
list_names = []

while not is_number:
    user = input()
    if user.isdigit():
        is_number = True
        break
    name, phone = user.split("-")
    phonebook[name] = phone
for _ in range(int(user)):
    names = input()
    list_names.append(names)
list_names = tuple(list_names)

for name in list_names:
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")