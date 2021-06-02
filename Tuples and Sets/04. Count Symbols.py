text = tuple(input())
sorted_text = {}

for char in text:
    count = text.count(char)
    sorted_text[char] = count
sorted_text = sorted(sorted_text.items(), key=lambda x: x[0])
[print(f"{key}: {value} time/s")for key, value in sorted_text]