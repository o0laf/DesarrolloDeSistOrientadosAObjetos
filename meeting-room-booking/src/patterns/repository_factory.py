from repositories.user_repository import UserRepository
from repositories.room_repository import RoomRepository
from repositories.booking_repository import BookingRepository

class RepositoryFactory:
    def __init__(self):
        self.user_repo = UserRepository()
        self.room_repo = RoomRepository()
        self.booking_repo = BookingRepository()

    def get_user_repo(self):
        return self.user_repo

    def get_room_repo(self):
        return self.room_repo

    def get_booking_repo(self):
        return self.booking_repo