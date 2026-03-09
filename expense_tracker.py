import json

# File to store expenses
FILE_NAME = "expenses.json"

# Load expenses from file
def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file)

# Add expense
def add_expense():
    category = input("Enter category (Food/Travel/Shopping): ")
    amount = float(input("Enter amount: "))
    
    expenses = load_expenses()
    
    expense = {
        "category": category,
        "amount": amount
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    
    print("✅ Expense added successfully!")

# View expenses
def view_expenses():
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses found.")
        return
    
    print("\n📊 Your Expenses:")
    
    total = 0
    
    for exp in expenses:
        print(f"{exp['category']} - ₹{exp['amount']}")
        total += exp["amount"]
    
    print("---------------")
    print(f"Total Spent: ₹{total}")

# Main menu
def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

# Run program
if __name__ == "__main__":
    main()
