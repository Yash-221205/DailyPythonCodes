def is_armstrong(num):
    original = num
    power = len(str(num))
    total = 0

    while num > 0:
        digit = num % 10
        total += digit ** power
        num = num // 10

    return total == original


number = int(input("Enter a number: "))

if is_armstrong(number):
    print("Armstrong number")
else:
    print("Not an Armstrong number")
