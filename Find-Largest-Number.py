# Python Program: Find the Largest Number Using Two Methods
#Read the total number of elements
n = int(input("How many numbers? "))
#Read the numbers from the user and store them in a list
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
#Using a Function
def find_largest(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

#Without Using a Function (Direct in Main Code)
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num

# Display Results
print("\nLargest Number Using Function:", find_largest(numbers))
print("Largest Number Without Function:", max_num)
