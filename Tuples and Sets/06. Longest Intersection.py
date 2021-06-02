n = int(input())

max_intersection = set()

for _ in range(n):
    first_range, second_range = input().split("-")
    first_lower, first_bigger = [int(_) for _ in first_range.split(",")]
    second_lower, second_bigger = [int(_) for _ in second_range.split(",")]

    first_range = set(range(first_lower, first_bigger + 1))
    second_range = set(range(second_lower, second_bigger + 1))
    if len(first_range.intersection(second_range)) > len(max_intersection):
        max_intersection = first_range.intersection(second_range)
        max_intersection = list(max_intersection)
print(f"Longest intersection is {max_intersection} with length {len(max_intersection)}")
