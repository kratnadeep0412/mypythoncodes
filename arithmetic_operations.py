#all arithmetic operations using functions
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    if y == 0:
        return "Division by zero is not allowed"
    else:
        return x / y
print("Addition:", add(1, 2))
print("Subtraction:", sub(1, 2))
print("Multiplication:", mul(2, 2))
print("Division:", div(2, 2))
