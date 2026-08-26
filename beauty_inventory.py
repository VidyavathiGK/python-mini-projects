def add_product(inventory):
    """Adds a new beauty product to the inventory."""
    name = input("Enter product name: ").strip()
    brand = input("Enter brand: ").strip()
    category = input("Enter category (Skincare/Makeup/Haircare): ").strip()
    status = input("Status (In Stash / Wishlist): ").strip()
    
    inventory[name] = {
        'brand': brand,
        'category': category,
        'status': status
    }
    print(f"Successfully added {brand} {name} to your {status}!")

def view_inventory(inventory):
    """Displays all saved beauty products."""
    print("\n--- Beauty Inventory & Wishlist ---")
    if not inventory:
        print("Your inventory is currently empty.")
        return
    for name, details in inventory.items():
        print(f"[{details['status']}] {details['brand']} - {name} ({details['category']})")
    print("-----------------------------------")

def main():
    inventory = {}
    print("--- Welcome to your Beauty Tracker ---")
    while True:
        print("\n1. Add Product\n2. View Inventory\n3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_product(inventory)
        elif choice == '2':
            view_inventory(inventory)
        elif choice == '3':
            print("Happy glowing! Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
