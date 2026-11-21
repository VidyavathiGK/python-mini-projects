from datetime import datetime
import math


class ParkingTicket:
    def __init__(self, ticket_id: str, plate_number: str, vehicle_type: str):
        self.ticket_id = ticket_id
        self.plate_number = plate_number
        self.vehicle_type = vehicle_type
        self.entry_time = datetime.now()
        self.exit_time = None
        self.fee = 0.0


class ParkingLot:
    HOURLY_RATES = {"bike": 10.0, "car": 25.0, "truck": 40.0}

    def __init__(self, capacity: int = 20):
        self.capacity = capacity
        self.active_tickets: dict[str, ParkingTicket] = {}
        self.ticket_counter = 100

    def park_vehicle(self, plate_number: str, vehicle_type: str) -> str:
        vehicle_type = vehicle_type.lower().strip()
        if vehicle_type not in self.HOURLY_RATES:
            raise ValueError(f"Unsupported vehicle type: {vehicle_type}")
        if len(self.active_tickets) >= self.capacity:
            raise RuntimeError("Parking lot is full.")
        if plate_number in self.active_tickets:
            raise ValueError(f"Vehicle {plate_number} is already parked.")

        self.ticket_counter += 1
        ticket_id = f"TKT-{self.ticket_counter}"
        self.active_tickets[plate_number] = ParkingTicket(ticket_id, plate_number, vehicle_type)
        return ticket_id

    def exit_vehicle(self, plate_number: str, simulated_hours: float | None = None) -> float:
        ticket = self.active_tickets.pop(plate_number, None)
        if not ticket:
            raise KeyError(f"No active ticket found for plate {plate_number}.")

        ticket.exit_time = datetime.now()
        hours = simulated_hours if simulated_hours is not None else max(
            1, math.ceil((ticket.exit_time - ticket.entry_time).total_seconds() / 3600)
        )
        ticket.fee = round(hours * self.HOURLY_RATES[ticket.vehicle_type], 2)
        return ticket.fee

    def available_spots(self) -> int:
        return self.capacity - len(self.active_tickets)


if __name__ == "__main__":
    lot = ParkingLot(capacity=15)
    t1 = lot.park_vehicle("KA-01-AB-1234", "car")
    t2 = lot.park_vehicle("KA-05-XY-9876", "bike")
    print(f"Issued {t1} and {t2}. Available spots: {lot.available_spots()}")
    fee = lot.exit_vehicle("KA-01-AB-1234", simulated_hours=3)
    print(f"Exit fee for KA-01-AB-1234: ₹{fee:.2f}. Available spots: {lot.available_spots()}")
