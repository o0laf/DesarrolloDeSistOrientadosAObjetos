from clases.persona import Paciente, Medico
from clases.gestor_turnos import GestorTurnos

def mostrar_menu():
    gestor = GestorTurnos.get_instancia()

    while True:
        print("\n--- Sistema de Turnos Médicos ---")
        print("1. Agregar Paciente")
        print("2. Agregar Médico")
        print("3. Crear Turno")
        print("4. Ver Turnos")
        print("5. Salir")
        opcion = input("Elegi una opción: ")

        if opcion == "1":
            nombre = input("Nombre del paciente: ")
            dni = input("DNI del paciente: ")
            paciente = Paciente(nombre, dni)
            gestor.agregar_paciente(paciente)
            print("Paciente agregado con éxito.")

        elif opcion == "2":
            nombre = input("Nombre del médico: ")
            dni = input("DNI del médico: ")
            especialidad = input("Especialidad: ")
            medico = Medico(nombre, dni, especialidad)
            gestor.agregar_medico(medico)
            print("Médico agregado con éxito.")

        elif opcion == "3":
            paciente_dni = input("DNI del paciente: ")
            medico_dni = input("DNI del médico: ")
            fecha = input("Fecha del turno (dd/mm/yyyy hh:mm): ")
            turno = gestor.crear_turno(paciente_dni, medico_dni, fecha)
            if turno:
                print("Turno creado:", turno.mostrar_turno())
            else:
                print("Error: Verifica los DNIs ingresados.")

        elif opcion == "4":
            turnos = gestor.listar_turnos()
            if turnos:
                print("\n--- Lista de Turnos ---")
                for t in turnos:
                    print(t)
            else:
                print("No hay turnos registrados.")

        elif opcion == "5":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")