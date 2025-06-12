# Basic Tuple examples
Tuple = (10, 20, 30)
print(Tuple)
print(type(Tuple))
# Tuple with a complex number
Tuple1 = (20 + 5j)
print(Tuple1)
print(type(Tuple1))
# Tuple without parenthesis (tuple packing)
Num = 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
print(Num)
print(type(Num))
# Tuple unpacking
a, b, c, d, e, f, g, h, i, j = Num
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
print(h, type(h))
print(i, type(i))
print(j, type(j))
# Tuple with mixed data types
Tuple = (10, 25.5, 1+5j, 'Hello', 'We', 'are', 'Learning', 'Python', [10, 20, 30])
print(Tuple)
print(Tuple[5])  # Accessing 6th element
# Tuple slicing
Tuple = (5, 10, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100)
print(Tuple[0:5])
print(Tuple[0:10])
print(Tuple[-5:])
print(Tuple[-20:])  # Prints entire tuple because it has only 19 elements
print(Tuple[10:15])
print(Tuple[0::3])
print(Tuple[0::4])
print(Tuple[::-2])
# Tuple deletion
Tuple = (5, 10, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100)
print(Tuple)
del Tuple
# print(Tuple)  # This will give an error because the tuple is deleted
# Tuple repetition
b = (1, 2, 3)
result = b * 3
print(result)
# Nested Tuple
Nested_Tuple = ((10, 20, 30), (40, 50, 60), (70, 80, 90))
print(Nested_Tuple)
print(Nested_Tuple[0])
print(Nested_Tuple[1])
print(Nested_Tuple[2])

# Creating tuple from user input
length = int(input("Enter the length of tuple: "))
numbers = []
for i in range(length):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

user_tuple = tuple(numbers)
print("Your tuple:", user_tuple)
