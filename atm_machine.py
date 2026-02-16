# ATM Machine Simulation

def check_balance(balance):
    print(f"\n💰 Your current balance is: ₹{balance}")


def deposit(balance):
    amount = float(input("\nEnter amount to deposit: ₹"))
    if amount > 0:
        balance += amount
        print(f"✅ ₹{amount} deposited successfully.")
    else:
        print("❌ Invalid amount.")
    return balance


def withdraw(balance):
    amount = float(input("\nEnter amount to withdraw: ₹"))
    if amount <= balance and amount > 0:
        balance -= amount
        print(f"✅ ₹{amount} withdrawn successfully.")
    else:
        print("❌ Insufficient balance or invalid amount.")
    return balance


def atm():
    balance = 10000  # Initial balance
    pin = "1234"
    attempts = 0

    print("🏧 Welcome to Python ATM")

    while attempts < 3:
        entered_pin = input("Enter your 4-digit PIN: ")
        if entered_pin == pin:
            print("🔓 Login successful!")
            break
        else:
            attempts += 1
            print("❌ Incorrect PIN")

    if attempts == 3:
        print("🚫 Too many failed attempts. Card blocked.")
        return

    while True:
        print("\n===== ATM Menu =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = deposit(balance)

        elif choice == "3":
            balance = withdraw(balance)

        elif choice == "4":
            print("👋 Thank you for using Python ATM!")
            break

        else:
            print("❌ Invalid option. Please try again.")


if __name__ == "__main__":
    atm()
