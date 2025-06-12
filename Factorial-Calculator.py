# Python Program: Calculate the Factorial of a Number
# Input: Read the number from the user
n = int(input("Enter a number: "))
# Initialize factorial result
factorial = 1
# Calculate factorial using loop
for i in range(1, n + 1):
    factorial *= i
# Display the result
print(f"\nFactorial of {n} is {factorial}")
