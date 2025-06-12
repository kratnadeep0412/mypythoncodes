# Python Program: Separate Even and Odd Numbers into Two Lists
Num=int(input("Enter the Value of Num :"))
Even_List=[]
Odd_List=[]
for i in range(1,Num+1,2):
    Odd_List.append(i)
for i in range(2,Num+1,2):
    Even_List.append(i)
print("Even_List :",Even_List)
print("Odd_List :",Odd_List)
