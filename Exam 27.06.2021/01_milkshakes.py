chocolates = [int(el) for el in input().split(", ")]
cups_of_milk = [int(el) for el in input().split(", ")]
chocolates_copy = chocolates.copy()
cups_of_milk_copy = cups_of_milk.copy()

milkshakes = 0

for chocolate in range(len(chocolates_copy) - 1, -1, -1):
    if len(chocolates) == 0 or len(cups_of_milk) == 0:
        break
    if milkshakes >= 5:
        break
    while not len(chocolates) == 0 or not len(cups_of_milk) == 0:
        if len(chocolates) == 0 or len(cups_of_milk) == 0:
            break
        if milkshakes >= 5:
            break
        cup = 0
        current_chocolate = chocolates[chocolate]
        current_cup = cups_of_milk[cup]
        if current_chocolate <= 0:
            chocolates.remove(current_chocolate)
            if current_cup <= 0:
                cups_of_milk.remove(current_cup)
            if len(chocolates) == 0:
                break
            break
        if current_cup <= 0:
            cups_of_milk.remove(current_cup)
            continue
        if current_chocolate == current_cup:
            milkshakes += 1
            chocolates.pop(chocolate)
            cups_of_milk.remove(current_cup)
            break
        else:
            cups_of_milk.append(current_cup)
            cups_of_milk.remove(current_cup)
            chocolates[-1] -= 5
            continue


if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
    if chocolates:
        print(f"Chocolate: {', '.join([str(el) for el in chocolates])}")
    else:
        print("Chocolate: empty")
    if cups_of_milk:
        print(f"Milk: {', '.join([str(el) for el in cups_of_milk])}")
    else:
        print("Milk: empty")
else:
    print("Not enough milkshakes.")
    if chocolates:
        print(f"Chocolate: {', '.join([str(el) for el in chocolates])}")
    else:
        print("Chocolate: empty")
    if cups_of_milk:
        print(f"Milk: {', '.join([str(el) for el in cups_of_milk])}")
    else:
        print("Milk: empty")