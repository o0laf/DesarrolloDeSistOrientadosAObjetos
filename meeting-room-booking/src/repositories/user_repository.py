from models.user import User

class UserRepository:
    def __init__(self):
        self.users = []
        self.counter = 1

    def create(self, name: str):
        user = User(self.counter, name)
        self.users.append(user)
        self.counter += 1
        return user

    def list(self):
        return self.users

    def get(self, user_id: int):
        return next((u for u in self.users if u.user_id == user_id), None)

    def delete(self, user_id: int):
        self.users = [u for u in self.users if u.user_id != user_id]