from models.room import Room

class RoomRepository:
    def __init__(self):
        self.rooms = []
        self.counter = 1

    def create(self, name: str):
        room = Room(self.counter, name)
        self.rooms.append(room)
        self.counter += 1
        return room

    def list(self):
        return self.rooms

    def get(self, room_id: int):
        return next((r for r in self.rooms if r.room_id == room_id), None)

    def delete(self, room_id: int):
        self.rooms = [r for r in self.rooms if r.room_id != room_id]