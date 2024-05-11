
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

input_word = "civic"


if is_palindrome(input_word):
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")