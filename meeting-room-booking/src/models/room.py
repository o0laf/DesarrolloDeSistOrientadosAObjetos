class Room:
    def __init__(self, room_id: int, name: str):
        self.room_id = room_id
        self.name = name

    def __repr__(self):
        return f"Sala({self.room_id}: {self.name})"