#Display only those characters which are present at an even index number in given string

s = input("Enter a string: ")

for i in range(0, len(s), 2):
    print(s[i])
