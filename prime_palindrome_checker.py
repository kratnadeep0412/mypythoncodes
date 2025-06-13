# Function to check if the number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

# Function to check if the number is palindrome
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# Main function
def check_prime_palindrome(n):
    if is_prime(n) and is_palindrome(n):
        print(f"{n} is a Prime Palindrome number.")
    elif is_prime(n):
        print(f"{n} is Prime but not a Palindrome.")
    elif is_palindrome(n):
        print(f"{n} is Palindrome but not Prime.")
    else:
        print(f"{n} is neither Prime nor Palindrome.")

# User input
num = int(input("Enter a number: "))
check_prime_palindrome(num)
