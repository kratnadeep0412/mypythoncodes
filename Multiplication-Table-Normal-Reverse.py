# Python Program: Multiplication Table (Normal and Reverse Order)
# Printing multiplication table of a specific number
Table = int(input("Enter a number: "))
print(f"\nMultiplication Table of {Table}:")
for i in range(1, 11):
    print(f"{Table} x {i} = {Table * i}")
# Printing multiplication tables from 1 to entered number in reverse order
Table2 = int(input("\nEnter a number to print tables from 1 to that number in reverse order: "))
for num in range(1, Table2 + 1):
    print(f"\nTable of {num} (in reverse order):")
    for i in range(10, 0, -1):
        print(f"{num} x {i} = {num * i}")
    print("-" * 25)
