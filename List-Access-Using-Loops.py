# Python Program: Accessing Elements in a List
IPL_List = ["CSK", "MI", "RCB", "SRH", "GT", "KKR"]
# Accessing elements without index (for-each loop)
print("Accessing the List Elements Without Index:")
for team in IPL_List:
    print(team)
# Accessing elements with index using for loop
print("\nAccessing the List Elements With Index:")
for i in range(len(IPL_List)):
    print(IPL_List[i])
# Accessing elements with index using while loop
print("\nAccessing the List Elements With Index using while loop:")
i = 0
while i < len(IPL_List):
    print(IPL_List[i])
    i += 1
