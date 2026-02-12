#Your task is to find the largest and smallest numbers in a list without using Python's built-in min() or max() functions.

nums = list(map(int, input("Enter numbers separated by space: ").split()))

largest = nums[0]
smallest = nums[0]

for n in nums:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print("Largest:", largest)
print("Smallest:", smallest)
