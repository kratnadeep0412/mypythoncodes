# String Problem 1: Index Access with Validation
Str = input("Enter the string: ")
i = int(input("Enter the index value: "))
print(Str)
if i < len(Str):
    print(f"Character at index {i} is: {Str[i]}")
else:
    print("Invalid Index Number")
# String Problem 3: Remove Spaces Using Split and Join
Str = input("\nEnter the string to remove spaces using split and join: ")
print("Original String:", Str)
# Splitting string into words
List = Str.split()
print("List after splitting:", List)
# Joining words without spaces
Res = "".join(List)
print("String after removing spaces:", Res)
# String Problem 4: Remove Spaces Character by Character
input_string = input("\nEnter a string to remove spaces using character iteration: ")
Char_list = []
for char in input_string:
    if char != ' ':  # Ignore spaces
        Char_list.append(char)
        print(Char_list)  # Print intermediate list after each addition (optional)
# Final result without spaces
final_string = ''.join(Char_list)
print("Final string without spaces:", final_string)
