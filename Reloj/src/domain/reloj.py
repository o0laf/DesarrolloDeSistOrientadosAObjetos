class Reloj:
    def __init__(self, hora: int, minuto: int, segundo: int):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

    def __str__(self):
        return f"{self.__hora:02}:{self.__minuto:02}:{self.__segundo:02}"

    def adelantar_minutos(self, minutos: int):
        total_minutos = self.__hora * 60 + self.__minuto + minutos
        self.__hora = (total_minutos // 60) % 24
        self.__minuto = total_minutos % 60

    def update_hora(self, hora: int, minuto: int, segundo: int):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

    def __ne__(self, otro_reloj):
        return (
            self.__hora != otro_reloj.__hora or
            self.__minuto != otro_reloj.__minuto or
            self.__segundo != otro_reloj.__segundo
        )
