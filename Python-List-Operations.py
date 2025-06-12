# Working with List Operations in Python
Front_End = ['HTML', 'CSS', 'JavaScript', 'React Js']
print("Initial Front-End List:", Front_End)
Front_End.append('Angular Js')
print("After Appending Angular Js:", Front_End)
Front_End.insert(3, 'Bootstrap')
print("After Inserting Bootstrap at index 3:", Front_End)
Front_End.insert(1, 'Tailwind')
print("After Inserting Tailwind at index 1:", Front_End)
Front_End.pop()
print("After Popping Last Item:", Front_End)
Front_End.pop(3)
print("After Popping Item at index 3:", Front_End)
Front_End.remove('HTML')
print("After Removing 'HTML':", Front_End)
print("Index of 'Bootstrap':", Front_End.index('Bootstrap'))
print("\n----- List Reversal -----")
Num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original Num List:", Num)
Num.reverse()
print("Reversed Num List:", Num)
print("\n----- List Extension -----")
# Extend: Adding elements of Num2 to Num1
Num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Num1 Before Extend:", Num1)
Num2 = [11, 22, 33, 44, 55, 66]
print("Num2:", Num2)
Num1.extend(Num2)
print("Num1 After Extend:", Num1)
print("\n----- List Sorting -----")
# Sort: Sorting the extended Num1 list
Num1.sort()
print("Sorted Num1 List:", Num1)
