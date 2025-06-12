# Python Program: Print Natural Numbers and Their Squares
# Input: Read the value of n
n = int(input("Enter the value of n: "))
# Print natural numbers from 1 to n
print(f"\nNatural numbers from 1 to {n}:")
for i in range(1, n + 1):
    print(i, end=' ')
# Print squares of natural numbers from 1 to n
print(f"\n\nSquares of natural numbers from 1 to {n}:")
for i in range(1, n + 1):
    print(f"{i}^2 = {i * i}")
