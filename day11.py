def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

nums = list(map(float, input("Enter numbers separated by space: ").split()))
print("Largest number:", find_largest(nums))
