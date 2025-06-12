# Question 1: Basic String Transformations
Input_Str = input("Enter the string: ")
print(f"User entered string: {Input_Str}")
print("Lowercase:", Input_Str.lower())
print("Uppercase:", Input_Str.upper())
print("Swapcase:", Input_Str.swapcase())
print("Title Case:", Input_Str.title())
print("Capitalized:", Input_Str.capitalize())
print("Reversed:", Input_Str[::-1])
# Question 2: String Methods
Input_Str = input("\nEnter the string: ")
print(f"User entered string: {Input_Str}")
print("Starts with 'p':", Input_Str.startswith('p'))
print("Ends with 'ing':", Input_Str.endswith('ing'))
print("Index of 'a':", Input_Str.index('a') if 'a' in Input_Str else "Not found")
print("Count of 'm':", Input_Str.count('m'))
print("Replace 'p' with 'j':", Input_Str.replace('p', 'j'))
print("Is Digit:", Input_Str.isdigit())
# Question 3: Count Digits, Vowels, and Special Characters
Input_Str = input("\nEnter a string: ")
Digit_count = 0
Vowel_count = 0
Special_char = 0

for ch in Input_Str.lower():
    if ch.isdigit():
        Digit_count += 1
    elif ch.isalpha():
        if ch in 'aeiou':
            Vowel_count += 1
    else:
        Special_char += 1

print(f"Digit Count: {Digit_count}")
print(f"Vowel Count: {Vowel_count}")
print(f"Special Character Count: {Special_char}")

# Question 4: Vowel and Consonant Cases Count
Input_Str = input("\nEnter a string: ")
Lower_Vowels = 0
Upper_Vowels = 0
Lower_Consonants = 0
Upper_Consonants = 0

for ch in Input_Str:
    if ch.isalpha():
        if ch in 'AEIOU':
            Upper_Vowels += 1
        elif ch in 'aeiou':
            Lower_Vowels += 1
        elif ch.isupper():
            Upper_Consonants += 1
        elif ch.islower():
            Lower_Consonants += 1

print(f"Lower Vowels Count: {Lower_Vowels}")
print(f"Upper Vowels Count: {Upper_Vowels}")
print(f"Lower Consonants Count: {Lower_Consonants}")
print(f"Upper Consonants Count: {Upper_Consonants}")

# Question 5: Email Parsing
Email = input("\nEnter the email: ")
if '@' in Email:
    user = Email.split('@')[0]
    organisation = Email.split('@')[1]
    print("User Name:", user)
    print("Organisation Name:", organisation)
else:
    print("Invalid email format")
# Question 6: Password Validation
password = input("\nEnter your password: ")
alpha_count = 0
digit_count = 0
special_count = 0
for ch in password:
    if ch.isalpha():
        alpha_count += 1
    elif ch.isdigit():
        digit_count += 1
    else:
        special_count += 1
if alpha_count > 0 and digit_count > 0 and special_count > 0:
    print("Valid Password")
else:
    print("Invalid Password")
