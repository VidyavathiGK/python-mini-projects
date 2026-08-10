rooms = {
    101: {"type": "Single", "price": 1500, "available": True},
    102: {"type": "Single", "price": 1500, "available": True},
    201: {"type": "Double", "price": 2500, "available": True},
    202: {"type": "Double", "price": 2500, "available": False},
    301: {"type": "Deluxe", "price": 3500, "available": True},
    302: {"type": "Deluxe", "price": 3500, "available": True}
}


def view_available_rooms():
    print("\n===== AVAILABLE ROOMS =====")

    found = False

    for room_no, details in rooms.items():
        if details["available"]:
            print(
                f"Room No: {room_no} | "
                f"Type: {details['type']} | "
                f"Price: ₹{details['price']} per night"
            )
            found = True

    if not found:
        print("No rooms are currently available.")


view_available_rooms()
