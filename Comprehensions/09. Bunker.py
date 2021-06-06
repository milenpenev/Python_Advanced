categories = input().split(", ")
n = int(input())

inventory = {category: [] for category in categories}

for _ in range(n):
    category, item_name, quantity_quality = input().split(" - ")
    quantity, quality = quantity_quality.split(";")
    quantity, quality = quantity.split(":")[1], quality.split(":")[1]
    quantity, quality = int(quantity), int(quality)

    inventory[category].append({"name": item_name, "quantity": quantity, "quality": quality})

total_items = sum([item["quantity"] for items in inventory.values() for item in items])
avg_quality = sum([item["quality"] for items in inventory.values() for item in items])/ len(categories)
print(f"Count of items: {total_items}")
print(f"Average quality: {avg_quality:.2f}")

print('\n'.join(f'{category} -> {", ".join(item["name"] for item in inventory[category])}' for category in categories))
