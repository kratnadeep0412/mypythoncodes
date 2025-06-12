# String slicing practice
word = "BIO TECHNOLOGY"
print(word[0:5])    # BIO T
print(word[2::-1])  # OIB (reverse slice)
print(word[4:8])    # TECH
print(word[:4:-1])  # YGOLONHCET (reverse from end to index 4)
print(word[7:3:-1]) # HCET
print(word[2::-1])  # OIB
print(word[9:13])   # LOGY
print(word[8:3:-1]) # NOHCET
print(word[4:10])   # TECHNO
print(word[0::3])   # BTHLY
print(word[0::2])   # BOTEHOGY
# Iterating through the string using a for loop
Str = "Vignan University"
for i in Str:
    print(i, end=' ')
print()
for i in range(len(Str)):
    print(Str[i], end=' ')
print()
# String multiplication
print("$" * 7)
str1 = "Students"
print(str1 * 5)           # Repeat the string 5 times
print(str1[0:4]
