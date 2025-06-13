
# Zero parameter function
def Zero_Arg_Function():
    print("Hey....! I am a Zero Arg Function")
# One parameter function
def Para_Function(Name):
    print(f"Hey....! I'm a one-parameter function, {Name} has invoked this function")
Zero_Arg_Function()
Para_Function("Rahul")
# Check even or odd using a function
def Even_Odd(Num):
    if (Num % 2 == 0):
        print(f"{Num} is Even")
    else:
        print(f"{Num} is Odd")
Even_Odd(10)
Even_Odd(44)
Even_Odd(1)
Even_Odd(5)
Even_Odd(60)
# Check whether the number is positive, negative, or zero using a function
def Positive_Negative_Zero(Num):
    if Num > 0:
        print(f"{Num} is Positive")
    elif Num < 0:
        print(f"{Num} is Negative")
    else:
        print(f"{Num} is Zero")
Positive_Negative_Zero(77)
Positive_Negative_Zero(-88)
# Check prime number using method 1
def Is_primeone(Num):
    Count = 0
    for i in range(1, Num + 1):
        if (Num % i == 0):
            Count += 1
    if (Count == 2):
        print(f"{Num} is a prime number")
    else:
        print(f"{Num} is not a prime number")
Is_primeone(18)
Is_primeone(2)
# Check prime number using method 2 (optimized)
def Is_primetwo(Num):
    if Num <= 1:
        print(f"{Num} is not a prime number")
        return
    Count = 0
    for i in range(2, Num // 2 + 1):
        if Num % i == 0:
            Count += 1
    if Count == 0:
        print(f"{Num} is a prime number")
    else:
        print(f"{Num} is not a prime number")
Is_primetwo(18)
Is_primetwo(0)
Is_primetwo(1)
Is_primetwo(7)

# Return function
def Display():
    return "Hey I'm a Return Function"
Res = Display()
print(Res)
