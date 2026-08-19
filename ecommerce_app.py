import json

CART_FILE = "cart.json"

def save_cart_to_file(cart):
    """Saves the shopping cart to a JSON file."""
    try:
        with open(CART_FILE, 'w') as f:
            json.dump(cart, f, indent=4)
    except IOError as e:
        print(f"Error saving cart to file: {e}")

def load_cart_from_file():
    """Loads the shopping cart from a JSON file."""
    try:
        with open(CART_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Return an empty cart if the file doesn't exist yet
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading cart from file: {e}. Starting with an empty cart.")
        return {}

def display_products(products):
    """Displays all available products."""
    print("\n--- Available Products ---")
    for product_id, details in products.items():
        print(f"ID: {product_id} | {details['name']} - ₹{details['price']:.2f}")
    print("--------------------------")

def search_products(products):
    """Allows the user to search for a product by name."""
    search_term = input("Enter the product name to search for: ").strip().lower()
    found_products = False
    print("\n--- Search Results ---")
    for product_id, details in products.items():
        if search_term in details['name'].lower():
            print(f"ID: {product_id} | {details['name']} - ₹{details['price']:.2f}")
            found_products = True
    if not found_products:
        print("No products found matching your search.")
    print("----------------------")

def add_to_cart(cart, products):
    """Adds a product to the shopping cart."""
    product_id = input("Enter the ID of the product to add: ").strip()
    if product_id in products:
        try:
            quantity = int(input(f"Enter quantity for {products[product_id]['name']}: "))
            if quantity <= 0:
                print("Quantity must be positive.")
                return
            if product_id in cart:
                cart[product_id]['quantity'] += quantity
            else:
                cart[product_id] = {
                    'name': products[product_id]['name'],
                    'price': products[product_id]['price'],
                    'quantity': quantity
                }
            print(f"{quantity} x {products[product_id]['name']} added to cart.")
            save_cart_to_file(cart)
        except ValueError:
            print("Invalid quantity.")
    else:
        print("Product ID not found.")

def remove_from_cart(cart):
    """Removes an item from the cart."""
    if not cart:
        print("Your cart is already empty.")
        return
    product_id = input("Enter the ID of the product to remove: ").strip()
    if product_id in cart:
        removed_item = cart.pop(product_id)
        print(f"'{removed_item['name']}' has been removed.")
        save_cart_to_file(cart)
    else:
        print("Product not found in your cart.")

def update_cart_quantity(cart):
    """Updates the quantity of an item in the cart."""
    if not cart:
        print("Your cart is empty.")
        return
    product_id = input("Enter the ID of the product to update: ").strip()
    if product_id in cart:
        try:
            new_quantity = int(input(f"Enter new quantity for {cart[product_id]['name']}: "))
            if new_quantity <= 0:
                print("Quantity must be positive. Use 'Remove' to delete.")
            else:
                cart[product_id]['quantity'] = new_quantity
                print(f"Quantity for '{cart[product_id]['name']}' updated.")
                save_cart_to_file(cart)
        except ValueError:
            print("Invalid quantity.")
    else:
        print("Product not found in your cart.")

def view_cart(cart):
    """Displays the shopping cart."""
    print("\n--- Your Shopping Cart ---")
    if not cart:
        print("Your cart is empty.")
        return
    total_cost = 0
    for product_id, item in cart.items():
        item_total = item['price'] * item['quantity']
        print(f"ID: {product_id} | {item['name']} (x{item['quantity']}) - ₹{item_total:.2f}")
        total_cost += item_total
    print(f"--------------------------\nTotal Cart Value: ₹{total_cost:.2f}")

def checkout(cart):
    """Simulates the checkout process."""
    if not cart:
        print("Your cart is empty.")
        return False
    view_cart(cart)
    confirm = input("Proceed to checkout? (yes/no): ").strip().lower()
    if confirm == 'yes':
        print("\n--- Checkout Complete! Thank you for your purchase! ---")
        cart.clear()
        save_cart_to_file(cart)
        return True
    else:
        print("Checkout cancelled.")
        return False

def main():
    """Main function to run the E-commerce Store Simulation."""
    products = {
        'P001': {'name': 'Laptop', 'price': 65000.00},
        'P002': {'name': 'Headphones', 'price': 2500.00},
        'P003': {'name': 'Mechanical Keyboard', 'price': 7000.00},
        'P004': {'name': 'Mouse', 'price': 1200.00},
        'P005': {'name': 'Monitor', 'price': 15000.00},
        'P006': {'name': 'USB Drive 64GB', 'price': 800.00},
    }
    
    shopping_cart = load_cart_from_file()
    
    print("--- Welcome to Our Online Store! (Cart loaded from previous session) ---")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Browse All Products")
        print("2. Search for a Product")
        print("3. Add Item to Cart")
        print("4. View Cart")
        print("5. Update Item Quantity in Cart")
        print("6. Remove Item from Cart")
        print("7. Checkout")
        print("8. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            display_products(products)
        elif choice == '2':
            search_products(products)
        elif choice == '3':
            add_to_cart(shopping_cart, products)
        elif choice == '4':
            view_cart(shopping_cart)
        elif choice == '5':
            update_cart_quantity(shopping_cart)
        elif choice == '6':
            remove_from_cart(shopping_cart)
        elif choice == '7':
            checkout(shopping_cart)
        elif choice == '8':
            print("Thank you for shopping with us! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
