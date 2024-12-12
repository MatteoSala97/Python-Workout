menu = {
    "Burger": 8,
    "Pizza": 12,
    "Salad": 7,
    "Pasta": 10,
    "Soda": 2,
    "Coffee": 3,
    "Ice Cream": 5
}

order = []

while True:
    order_list = input("What would you like to order? Type 'menu' to see the menu. Type 'confirm' to order\n")
    
    if order_list.lower() == 'menu':
        for item, price in menu.items():
            print(f"{item}: {price} dallah bills")
    elif order_list.lower() == 'confirm':
        break
    elif order_list.lower() not in [item.lower() for item in menu.keys()]:
        print(f"Sorry, we're out of {order_list}")
    else:
        order.append(order_list)
        print(f"{order_list} added to your order.")

print("Your order has been confirmed:")
print(f"{order} added to your order.")
