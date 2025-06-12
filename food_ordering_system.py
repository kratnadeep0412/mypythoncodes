# File name: food_ordering_system.py
# Predefined food items and their prices
Food_items = ['Pizza', 'Burger', 'Brownie', 'Pasta', 'Cupcake', 'French Fries']
Prices = [120, 250, 200, 150, 130, 100]
print("Welcome to the Food Ordering System!")
print("\n******** MENU ********")
for i in range(len(Food_items)):
    print(f"{Food_items[i]} - ₹{Prices[i]}")
Total = 0
while True:
    item = input('\nEnter food item (or type "exit" to finish your order): ').title()
    if item.lower() == 'exit':
        break
    if item in Food_items:
        Quantity = int(input('Quantity Required: '))
        index = Food_items.index(item)
        price = Prices[index]
        bill = Quantity * price
        Total += bill
        print(f"{item} added to your bill. Current total (excluding tax): ₹{Total}")
    else:
        print('Item does not exist. Please order something from the menu.')
# Adding 18% GST to the total bill
Total_with_tax = Total + (0.18 * Total)
print(f"\nFinal Bill (including 18% GST): ₹{Total_with_tax:.2f}")
print("\nThank you for ordering! Enjoy your meal 😋")
