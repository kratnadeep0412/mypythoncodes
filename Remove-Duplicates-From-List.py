# Python Program: Remove Duplicates from a List
# Read list size from the user
size = int(input("Enter the size of the list: "))
#Initialize empty lists
List = []
Unique_list = []
#Take list elements from user input
for i in range(size):
    Temp = int(input(f"Enter the integer value at index {i}: "))
    List.append(Temp)
#Display the original list
print(f"\nUser Entered List: {List}")
#Remove duplicates by adding only unique elements to Unique_list
for i in List:
    if i not in Unique_list:
        Unique_list.append(i)
#Display the list with unique elements
print(f"Unique List: {Unique_list}")
