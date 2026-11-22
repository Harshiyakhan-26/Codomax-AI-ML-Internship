def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]
for w in ["madam", "python", "level"]:
    print(w, "->", is_palindrome(w))

