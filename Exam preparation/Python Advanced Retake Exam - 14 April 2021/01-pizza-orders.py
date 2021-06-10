from collections import deque

pizza_orders = [int(el) for el in input().split(", ")]
employees = [int(el) for el in input().split(", ")]
completed_orders = []
pizza_orders = deque(pizza_orders)
orders_left = 0
removed = True
employee_sum = 0

while pizza_orders:
    if employees:
        if removed:
            current_pizza = pizza_orders.popleft()
            orders_left = current_pizza
        if current_pizza > 10 or current_pizza <= 0:
            orders_left = 0
            continue
        current_employee = employees.pop()
        employee_sum += current_employee
        if current_pizza <= employee_sum:
            completed_orders.append(current_pizza)
            employee_sum = 0
            orders_left = 0
            removed = True
            continue
        elif orders_left > employee_sum:
            orders_left -= employee_sum
            removed = False
            continue
    else:
        pizza_orders.appendleft(orders_left)
        break


if employees:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {sum(completed_orders)}")
    print("Employees: ", end="")
    print(*employees, sep=", ")
else:
    print("Not all orders are completed.")
    print("Orders left: ", end="")
    print(*pizza_orders, sep=", ")
