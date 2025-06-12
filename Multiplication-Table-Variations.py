# Python Program: Multiplication Table Variations
# Single multiplication table
number = int(input("Enter a number: "))
print(f"\nMultiplication table of {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
# Multiplication tables from 1 to n
n = int(input("\nEnter the value of n: "))
for num in range(1, n + 1):
    print(f"\nMultiplication table of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
# Reversed multiplication table of a number
n = int(input("\nEnter a number for reversed table: "))
print(f"\nReversed multiplication table of {n}:")
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * i}")
# Reversed multiplication tables from 1 to n
n = int(input("\nEnter the value of n for reversed tables: "))
for num in range(1, n + 1):
    print(f"\nReversed multiplication table of {num}:")
    for i in range(10, 0, -1):
        print(f"{num} x {i} = {num * i}")
