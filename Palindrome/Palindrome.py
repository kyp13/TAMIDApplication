#See whether an inputted word is a palindrome

def isPalindrome(word):
    if word == word[::-1]:
        return word, "is a palindrome!"
    else:
        return word, "is not a palindrome!"

word = input("Enter a word in lowercase: ")

print(isPalindrome(word))