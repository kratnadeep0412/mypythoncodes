# Python Program: Deleting Elements from a List
# Initial IPL Team List
IPL_List = ["CSK", "MI", "RCB", "SRH", "GT", "PBKS"]
print("Original IPL List:", IPL_List)
# Deleting an element at index 1 ("MI")
print("After Deletion of Element at Index 1:")
del IPL_List[1]
print(IPL_List)
# Deleting the entire list
print("Deleting the Entire List:")
del IPL_List
# Trying to print the list after deletion will cause an error
print(IPL_List)  # This will raise a NameError
