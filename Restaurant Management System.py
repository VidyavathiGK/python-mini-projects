menu = {
    1: {"name": "Idli", "price": 40},
    2: {"name": "Dosa", "price": 60},
    3: {"name": "Fried Rice", "price": 120},
    4: {"name": "Paneer Butter Masala", "price": 180},
    5: {"name": "Veg Biryani", "price": 150},
    6: {"name": "Coffee", "price": 30}
}

order = {}


def view_menu():
    print("\n========== MENU ==========")

    for number, item in menu.items():
        print(f"{number}. {item['name']} - ₹{item['price']}")


def add_food():
    view_menu()

    try:
        choice = int(input("\nEnter food number: "))

        if choice not in menu:
            print("Invalid food number.")
            return

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        if choice in order:
            order[choice] += quantity
        else:
            order[choice] = quantity

        print("Food added to order successfully!")

    except ValueError:
        print("Please enter a valid number.")


def view_order():
    if not order:
        print("\nYour order is empty.")
        return

    print("\n========== YOUR ORDER ==========")

    total = 0

    for choice, quantity in order.items():
        item = menu[choice]
        amount = item["price"] * quantity
        total += amount

        print(
            f"{item['name']} x {quantity} = ₹{amount}"
        )

    print("-------------------------------")
    print(f"Total: ₹{total}")


def calculate_bill():
    if not order:
        print("\nNo items in the order.")
        return

    total = 0

    for choice, quantity in order.items():
        total += menu[choice]["price"] * quantity

    gst = total * 0.05
    final_amount = total + gst

    print("\n========== BILL ==========")
    print(f"Food Total : ₹{total:.2f}")
    print(f"GST (5%)   : ₹{gst:.2f}")
    print(f"Final Bill : ₹{final_amount:.2f}")


def remove_food():
    view_order()

    if not order:
        return

    try:
        choice = int(input("\nEnter food number to remove: "))

        if choice in order:
            del order[choice]
            print("Food removed successfully!")
        else:
            print("Food is not in your order.")

    except ValueError:
        print("Please enter a valid number.")


def clear_order():
    order.clear()
    print("Order cleared successfully!")


def main():
    while True:
        print("\n================================")
        print("   RESTAURANT MANAGEMENT SYSTEM")
        print("================================")
        print("1. View Menu")
        print("2. Add Food Item")
        print("3. View Current Order")
        print("4. Calculate Total Bill")
        print("5. Remove Food Item")
        print("6. Clear Order")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_menu()

        elif choice == "2":
            add_food()

        elif choice == "3":
            view_order()

        elif choice == "4":
            calculate_bill()

        elif choice == "5":
            remove_food()

        elif choice == "6":
            clear_order()

        elif choice == "7":
            print("\nThank you! Visit again. 😊")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
