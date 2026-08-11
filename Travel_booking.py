# Travel Booking System

packages = {
    1: {"destination": "Goa", "days": 4, "price": 8000},
    2: {"destination": "Manali", "days": 5, "price": 12000},
    3: {"destination": "Ooty", "days": 3, "price": 7000},
    4: {"destination": "Jaipur", "days": 4, "price": 9000},
    5: {"destination": "Kerala", "days": 5, "price": 10000}
}

booking = {}


def view_packages():
    print("\n========== TRAVEL PACKAGES ==========")

    for number, package in packages.items():
        print(
            f"{number}. {package['destination']} - "
            f"{package['days']} Days - "
            f"₹{package['price']} per person"
        )


def book_trip():
    view_packages()

    try:
        choice = int(input("\nEnter package number: "))

        if choice not in packages:
            print("Invalid package number.")
            return

        name = input("Enter customer name: ")
        phone = input("Enter phone number: ")
        people = int(input("Enter number of people: "))

        if people <= 0:
            print("Number of people must be greater than 0.")
            return

        package = packages[choice]

        booking["package"] = choice
        booking["name"] = name
        booking["phone"] = phone
        booking["people"] = people

        print("\nBooking successful!")
        print(f"Destination: {package['destination']}")
        print(f"Customer: {name}")
        print(f"Number of people: {people}")

    except ValueError:
        print("Please enter valid information.")


def view_booking():
    if not booking:
        print("\nNo booking found.")
        return

    package = packages[booking["package"]]

    print("\n========== BOOKING DETAILS ==========")
    print(f"Customer Name : {booking['name']}")
    print(f"Phone Number  : {booking['phone']}")
    print(f"Destination   : {package['destination']}")
    print(f"Duration      : {package['days']} Days")
    print(f"People        : {booking['people']}")
    print(f"Price/Person  : ₹{package['price']}")


def cancel_booking():
    if not booking:
        print("\nNo booking found.")
        return

    booking.clear()
    print("\nBooking cancelled successfully!")


def calculate_bill():
    if not booking:
        print("\nNo booking found.")
        return

    package = packages[booking["package"]]

    total = package["price"] * booking["people"]

    print("\n========== BILL ==========")
    print(f"Destination  : {package['destination']}")
    print(f"Price/Person : ₹{package['price']}")
    print(f"People       : {booking['people']}")
    print("---------------------------")
    print(f"Total Amount : ₹{total}")


def view_destinations():
    print("\n========== DESTINATIONS ==========")

    for package in packages.values():
        print(f"• {package['destination']}")


def main():
    while True:
        print("\n====================================")
        print("       TRAVEL BOOKING SYSTEM")
        print("====================================")
        print("1. View Travel Packages")
        print("2. Book a Trip")
        print("3. View Booking Details")
        print("4. Cancel Booking")
        print("5. Calculate Total Bill")
        print("6. View Available Destinations")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_packages()

        elif choice == "2":
            book_trip()

        elif choice == "3":
            view_booking()

        elif choice == "4":
            cancel_booking()

        elif choice == "5":
            calculate_bill()

        elif choice == "6":
            view_destinations()

        elif choice == "7":
            print("\nThank you for using Travel Booking System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
