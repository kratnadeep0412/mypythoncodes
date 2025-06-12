# Month Validation Program
# Input from user
month = int(input("Enter the number: "))
# Using if-else
if 1 <= month <= 12:
    print(f"{month} is a valid month.")
else:
    print(f"{month} is an invalid month.")
# Using ternary operator
Res = "a valid month" if (1 <= month <= 12) else "an invalid month"
print(f"{month} is {Res}.")
