import uuid


class Event:
    def __init__(self, name: str, total_seats: int, ticket_price: float):
        self.name = name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.available_seats = set(range(1, total_seats + 1))
        self.bookings: dict[str, dict] = {}

    def book_seats(self, attendee_name: str, seat_numbers: list[int]) -> str:
        unavailable = [s for s in seat_numbers if s not in self.available_seats]
        if unavailable:
            raise ValueError(f"Seats unavailable: {unavailable}")

        for seat in seat_numbers:
            self.available_seats.remove(seat)

        booking_id = str(uuid.uuid4())[:8].upper()
        total_cost = round(len(seat_numbers) * self.ticket_price, 2)
        self.bookings[booking_id] = {
            "attendee": attendee_name,
            "seats": sorted(seat_numbers),
            "total_cost": total_cost,
        }
        return booking_id

    def cancel_booking(self, booking_id: str) -> bool:
        booking = self.bookings.pop(booking_id, None)
        if not booking:
            return False
        self.available_seats.update(booking["seats"])
        return True


if __name__ == "__main__":
    concert = Event("Python Dev Summit 2026", total_seats=30, ticket_price=499.0)
    b_id = concert.book_seats("Vidyavathi", [1, 2, 3])
    print("Booking confirmed:", b_id, concert.bookings[b_id])
    print("Remaining seats:", len(concert.available_seats))
