def display_products(products):
    """Displays all available products with their IDs, names, and prices."""
    print("\n--- Available Products ---")
    if not products:
        print("No products available.")
        return
    for product_id, details in products.items():
        print(f"ID: {product_id} | {details['name']} - ₹{details['price']:.2f}")
    print("--------------------------")

def add_to_cart(cart, products):
    """Allows the user to add a product to their shopping cart."""
    product_id = input("Enter the ID of the product you want to add to cart: ").strip()
    
    if product_id in products:
        try:
            quantity = int(input(f"Enter quantity for {products[product_id]['name']}: "))
            if quantity <= 0:
                print("Quantity must be a positive number.")
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
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    else:
        print("Product ID not found. Please enter a valid product ID.")

def view_cart(cart):
    """Displays the current items in the shopping cart and the total cost."""
    print("\n--- Your Shopping Cart ---")
    if not cart:
        print("Your cart is empty.")
        return
    
    total_cost = 0
    for product_id, item in cart.items():
        item_total = item['price'] * item['quantity']
        print(f"{item['name']} (x{item['quantity']}) - ₹{item['price']:.2f} each | Total: ₹{item_total:.2f}")
        total_cost += item_total
    
    print(f"--------------------------")
    print(f"Total Cart Value: ₹{total_cost:.2f}")
    print("--------------------------")

def checkout(cart):
    """Simulates the checkout process."""
    if not cart:
        print("Your cart is empty. Nothing to checkout.")
        return False
    
    view_cart(cart)
    confirm = input("Proceed to checkout? (yes/no): ").strip().lower()
    
    if confirm == 'yes':
        print("\n--- Checkout Complete! ---")
        print("Thank you for your purchase!")
        cart.clear() # Empty the cart after checkout
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
    
    shopping_cart = {}
    
    print("--- Welcome to Our Online Store! ---")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Browse Products")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            display_products(products)
        elif choice == '2':
            add_to_cart(shopping_cart, products)
        elif choice == '3':
            view_cart(shopping_cart)
        elif choice == '4':
            if checkout(shopping_cart):
                # Optionally, you could ask if they want to continue shopping after checkout
                pass 
        elif choice == '5':
            print("Thank you for shopping with us! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
