#Create a program that prints the multiplication table for a number entered by the user.

n = int(input("Enter a number: "))
limit = int(input("Enter number of iterations: "))

for i in range(1, limit + 1):
    print(n, "x", i, "=", n * i)
