# 1. String without spaces
input_string = input("Enter a string: ")
Char_list = []

for char in input_string:
    if char != ' ':  # Ignore spaces
        Char_list.append(char)

print("String without spaces:", "".join(Char_list))

print("\n-------------------------\n")

# 2. Substring of size N (Subsets difference)
input_string = input("Enter a string for substring operation: ")
n = int(input("Enter the size of each substring: "))

print("Substrings of size", n, ":")
for i in range(0, len(input_string), n):
    print(input_string[i:i+n])

print("\n-------------------------\n")

# 3. User-defined split into three parts
s = input("Enter a string to split into three parts: ")
print("Original String:", s)

# Find the length of each part
n = len(s) // 3
print("First part:", s[0:n])
print("Second part:", s[n:2*n])
print("Third part:", s[2*n:])
