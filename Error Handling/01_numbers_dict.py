numbers_dictionary = {}

key = ''

while True:
    key = input()
    if key == "Search":
        break
    value = input()
    if value == "Search":
        break
    number = int(value)
    numbers_dictionary[key] = number

searched = input()

while searched != "Remove":
    print(numbers_dictionary.get(searched, 'Number does not exist in dictionary'))
    searched = input()

line = input()

while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except:
        print("Number does not exist in dictionary")
    print(numbers_dictionary)
    line = input()


