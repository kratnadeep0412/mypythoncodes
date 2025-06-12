# Python Program: Currency Denomination Calculator

# Input: Total amount from the user
amount = int(input("Enter the amount: "))
# Calculating the number of 2000 notes
print("2000 ->", amount // 2000)
amount = amount % 2000
# Calculating the number of 500 notes
print("500 ->", amount // 500)
amount = amount % 500
# Calculating the number of 200 notes
print("200 ->", amount // 200)
amount = amount % 200
# Calculating the number of 100 notes
print("100 ->", amount // 100)
amount = amount % 100
# Calculating the number of 50 notes
print("50 ->", amount // 50)
amount = amount % 50
# Calculating the number of 20 notes
print("20 ->", amount // 20)
amount = amount % 20
# Calculating the number of 10 coins
print("10 ->", amount // 10)
amount = amount % 10
# Calculating the number of 5 coins
print("5 ->", amount // 5)
amount = amount % 5
# Calculating the number of 2 coins
print("2 ->", amount // 2)
amount = amount % 2
# Calculating the number of 1 coins
print("1 ->", amount // 1)
amount = amount % 1
