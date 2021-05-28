n = int(input())

all_guests = set()

for _ in range(n):
    all_guests.add(input())

ticket = input()
arrived = set()
while not ticket == "END":
    arrived.add(ticket)
    ticket = input()

print(len(all_guests.difference(arrived)))
sorted_difference = sorted(all_guests.difference(arrived))

print("\n".join(sorted_difference))