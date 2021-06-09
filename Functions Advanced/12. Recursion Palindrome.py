def palindrome(word, index):
    left = index
    right = len(word) - 1 - index

    if left >= right:
        return f"{word} is a palindrome"

    right_letter = word[len(word)-1-index]
    left_letter = word[index]
    if left_letter != right_letter:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)

print(palindrome("abcba", 0))
print((palindrome("peter", 0)))