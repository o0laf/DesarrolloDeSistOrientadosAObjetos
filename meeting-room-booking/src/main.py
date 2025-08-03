print(">>> Iniciando sistema...")

from datetime import datetime
from patterns.repository_factory import RepositoryFactory
from services.booking_service import BookingService

def main():
    factory = RepositoryFactory()
    user_repo = factory.get_user_repo()
    room_repo = factory.get_room_repo()
    booking_repo = factory.get_booking_repo()
    booking_service = BookingService(booking_repo)

    print("Sistema de reservas de salas de reunión")

    u1 = user_repo.create("Mariana")
    r1 = room_repo.create("Sala A")

    try:
        booking = booking_service.create_booking(
            user_id=u1.user_id,
            room_id=r1.room_id,
            start_time=datetime(2025, 8, 3, 10, 0),
            end_time=datetime(2025, 8, 3, 11, 0)
        )
        print("Reserva creada:", booking)
    except Exception as e:
        print("Error:", e)

    print("Reservas de Mariana:", booking_repo.get_by_user(u1.user_id))
    print("Reservas en Sala A:", booking_repo.get_by_room(r1.room_id))

if __name__ == "__main__":
    main()