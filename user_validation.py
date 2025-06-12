# Password Validation
password = input("Enter your password: ")
alphabet_count = 0
digit_count = 0
special_count = 0
for ch in password:
    if ch.isalpha():
        alphabet_count += 1
    elif ch.isdigit():
        digit_count += 1
    else:
        special_count += 1
if alphabet_count >= 1 and digit_count >= 1 and special_count >= 1:
    print("Valid Password")
else:
    print("Invalid Password")
print("\n-------------------------\n")
# User Details Validation
username = input("Enter your username: ")
contact_number = input("Enter your contact number: ")
mail_id = input("Enter your mail ID: ")
password = input("Enter your password: ")

# Username validation: only alphabets
if not username.isalpha():
    print("Invalid username. It should contain only alphabets.")
# Contact number validation: exactly 10 digits
elif not (contact_number.isdigit() and len(contact_number) == 10):
    print("Invalid contact number. It should be exactly 10 digits.")
# Mail ID validation: format name@organisation.com
elif '@' not in mail_id or '.' not in mail_id.split('@')[-1]:
    print("Invalid mail ID. Format should be name@organisation.com")
# Password validation: should have alphabets, digits and special characters
else:
    alphabet_count = 0
    digit_count = 0
    special_count = 0

    for ch in password:
        if ch.isalpha():
            alphabet_count += 1
        elif ch.isdigit():
            digit_count += 1
        else:
            special_count += 1
    if alphabet_count >= 1 and digit_count >= 1 and special_count >= 1:
        print("\n--- Validated Details ---")
        print(f"Username: {username}")
        print(f"Contact Number: {contact_number}")
        print(f"Mail ID: {mail_id}")
        print("Password is valid.")
    else:
        print("Invalid Password. It must contain alphabets, digits, and special characters.")
