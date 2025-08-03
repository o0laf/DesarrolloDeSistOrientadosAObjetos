from datetime import datetime

class BookingService:
    def __init__(self, booking_repo):
        self.booking_repo = booking_repo

    def create_booking(self, user_id: int, room_id: int, start_time: datetime, end_time: datetime):
        if self.booking_repo.is_conflict(room_id, start_time, end_time):
            raise Exception("Conflicto de horario con otra reserva.")
        return self.booking_repo.create(user_id, room_id, start_time, end_time)