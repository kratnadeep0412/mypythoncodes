# Type Conversion Example
# Taking input from the user
int_value = int(input("Enter the integer value: "))
float_value = float(input("Enter the float value: "))
string_value = input("Enter the string: ")
# Conversions from integer
int_to_str = str(int_value)
int_to_float = float(int_value)
int_to_complex = complex(int_value)
# Displaying the conversions
print(f"\nOriginal Integer: {int_value}")
print(f"Integer to String: {int_to_str} (Type: {type(int_to_str)})")
print(f"Integer to Float: {int_to_float} (Type: {type(int_to_float)})")
print(f"Integer to Complex: {int_to_complex} (Type: {type(int_to_complex)})")
# Additional Conversions
# Float to Integer
float_to_int = int(float_value)
float_to_str = str(float_value)
print(f"\nOriginal Float: {float_value}")
print(f"Float to Integer: {float_to_int} (Type: {type(float_to_int)})")
print(f"Float to String: {float_to_str} (Type: {type(float_to_str)})")
# String to Integer (if numeric)
if string_value.isdigit():
    string_to_int = int(string_value)
    print(f"\nOriginal String: {string_value}")
    print(f"String to Integer: {string_to_int} (Type: {type(string_to_int)})")
else:
    print(f"\nOriginal String: {string_value}")
    print("String is not convertible to integer.")
