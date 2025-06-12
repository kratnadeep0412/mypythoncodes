Guest_List = []
print(" Welcome to the Party Project ")
command_count = 0
while True:
    print("\n******** Menu ***********")
    print("1. Enter 1 to add a guest")
    print("2. Enter 2 to remove a guest who cancels")
    print("3. Enter 3 to check if a friend is on the list or not")
    print("4. Enter 4 to print the final guest list")
    print("5. Enter 5 to exit")
    Choice = int(input("Enter your choice: "))
    if 1 <= Choice <= 5:
        command_count += 1
        if Choice == 1:
            Name = input("Enter the name of the guest: ")
            Guest_List.append(Name)
            print(f"{Name} is added to the guest list!")
        elif Choice == 2:
            Cancelled_Name = input("Enter the guest who cancelled: ")
            if Cancelled_Name in Guest_List:
                Guest_List.remove(Cancelled_Name)
                print(f"{Cancelled_Name} is removed from the guest list.")
            else:
                print(f"{Cancelled_Name} is not present in the list!")
        elif Choice == 3:
            Check_Guest = input("Enter the name of the guest to check: ")
            if Check_Guest in Guest_List:
                print(f"{Check_Guest} is attending the party!")
            else:
                print(f"{Check_Guest} is not attending the party.")
        elif Choice == 4:
            print("\nFinal Guest List:")
            print(Guest_List)
        elif Choice == 5:
            print("\n Thanks for helping manage the party guest list!")
            print(f"Total Commands Executed: {command_count}")
            break
    else:
        print("Invalid choice. Please select from 1 to 5.")
