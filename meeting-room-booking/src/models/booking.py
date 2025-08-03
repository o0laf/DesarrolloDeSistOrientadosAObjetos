from datetime import datetime

class Booking:
    def __init__(self, booking_id: int, user_id: int, room_id: int, start_time: datetime, end_time: datetime):
        self.booking_id = booking_id
        self.user_id = user_id
        self.room_id = room_id
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return (f"Reserva({self.booking_id}: Usuario {self.user_id}, Sala {self.room_id}, "
                f"{self.start_time} - {self.end_time})")