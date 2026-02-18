def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

string = input("Enter a string: ")

if is_palindrome(string):
    print("Palindrome")
else:
    print("Not a palindrome")
