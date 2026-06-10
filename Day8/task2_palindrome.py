word = input("Enter the word:")

word_lower = word.lower()
reversed_word =  word_lower[::1]
if word_lower == reversed_word:
    print(f"'{word}'is a palimdrome  ✓")
else:
    print(f"'{word}' is not a palimdrome ✗")