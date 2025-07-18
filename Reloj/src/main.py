from domain.reloj import Reloj

reloj1 = Reloj(10, 30, 0)
reloj2 = Reloj(15, 45, 10)
reloj3 = Reloj(23, 59, 59)

print("Reloj 1:", reloj1)
print("Reloj 2:", reloj2)
print("Reloj 3:", reloj3)

reloj1.adelantar_minutos(1)
print("Reloj 1 adelantado 1 minuto:", reloj1)

reloj2.update_hora(8, 0, 0)
print("Reloj 2 actualizado:", reloj2)

if reloj2 != reloj3:
    print("Reloj 2 y Reloj 3 NO tienen la misma hora.")
else:
    print("Reloj 2 y Reloj 3 tienen la misma hora.")