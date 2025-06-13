# multiplication table of n using functions
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
num = int(input("Enter the multiplication table: "))
multiplication_table(num)
