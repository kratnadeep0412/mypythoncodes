# Python Program: Replace Negative Numbers with Zero and Print Numbers Divisible by 3

# Taking list size input
Size = int(input("Enter the range of the list: "))
# List creation
Num = []
for i in range(Size):
    Value = int(input(f"Enter the value at index {i}: "))
    Num.append(Value)
# Printing the original list
print(f"Original list: {Num}")
# Replacing negative numbers with zero
for i in range(Size):
    if Num[i] < 0:
        Num[i] = 0
# Printing numbers divisible by 3
print("Numbers divisible by 3:")
for i in range(Size):
    if Num[i] % 3 == 0:
        print(Num[i])
