with open("text.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    out = []
    for index, line in enumerate(lines):
        sum_char = sum([len(word) for word in line.split()])
        punctuation_sum = sum([1 for word in line.split() for letter in word if letter in r'-,\.!?\''])

        out.append(f"Line {index + 1}: {line} ({sum_char - punctuation_sum})({punctuation_sum})\n")

with open("output.txt", "w") as output_file:
    output_file.writelines(out)