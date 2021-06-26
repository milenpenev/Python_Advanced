def stock_availability(*args):
    inventory, command = args[0], args[1]
    if command == "delivery":
        for el in range(len(args[2:])):
            inventory.append(args[el + 2])
        return inventory
    elif command == "sell":
        if len(args) == 2:
            inventory.pop(0)
            return inventory
        if isinstance(args[2], int):
            for el in range(args[2]):
                inventory.pop(0)
            return inventory
        else:
            for el in args[2:]:
                inventory = list(dict.fromkeys(inventory))
                if el in inventory:
                    inventory.remove(el)
            return inventory
print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
