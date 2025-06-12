# Python Program: Santa's Sleigh Packing Program

Toy_List = []
print(" Welcome to Santa's Sleigh Packing Program ")
while True:
    print("\n******** Menu ********")
    print("1. Enter 1 to add a toy to the list")
    print("2. Enter 2 to remove duplicates from the list")
    print("3. Enter 3 to sort and display the final toy list")
    print("4. Enter 4 to exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("❗ Please enter a valid number.")
        continue

    if choice == 1:
        toy = input("Enter the name of the toy: ")
        Toy_List.append(toy)
        print(f" {toy} has been added to the toy list!")

    elif choice == 2:
        Toy_List = list(set(Toy_List))
        print("Duplicates have been removed from the toy list.")

    elif choice == 3:
        Toy_List.sort()
        print("\n Here is Santa's Final Sorted Toy List :")
        for toy in Toy_List:
            print(f" {toy}")

    elif choice == 4:
        print(" Thanks for helping Santa pack his sleigh! See you next Christmas! ")
        break

    else:
        print("❗ Invalid choice. Please select from the menu options.")
