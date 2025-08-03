from models.booking import Booking

class BookingRepository:
    def __init__(self):
        self.bookings = []
        self.counter = 1

    def create(self, user_id: int, room_id: int, start_time, end_time):
        booking = Booking(self.counter, user_id, room_id, start_time, end_time)
        self.bookings.append(booking)
        self.counter += 1
        return booking

    def list(self):
        return self.bookings

    def get_by_user(self, user_id: int):
        return [b for b in self.bookings if b.user_id == user_id]

    def get_by_room(self, room_id: int):
        return [b for b in self.bookings if b.room_id == room_id]

    def is_conflict(self, room_id: int, start_time, end_time):
        for b in self.bookings:
            if b.room_id == room_id and not (end_time <= b.start_time or start_time >= b.end_time):
                return True
        return False