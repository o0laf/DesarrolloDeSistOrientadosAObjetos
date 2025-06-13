from clases.turno import Turno

class GestorTurnos:
    _instancia = None

    def __init__(self):
        if GestorTurnos._instancia is not None:
            raise Exception("Esta clase es Singleton, usa get_instancia().")
        else:
            self.pacientes = []
            self.medicos = []
            self.turnos = []
            GestorTurnos._instancia = self

    @staticmethod
    def get_instancia():
        if GestorTurnos._instancia is None:
            GestorTurnos()
        return GestorTurnos._instancia

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def crear_turno(self, paciente_dni, medico_dni, fecha):
        paciente = next((p for p in self.pacientes if p.dni == paciente_dni), None)
        medico = next((m for m in self.medicos if m.dni == medico_dni), None)
        if paciente and medico:
            turno = Turno(paciente, medico, fecha)
            self.turnos.append(turno)
            return turno
        return None

    def listar_turnos(self):
        return [t.mostrar_turno() for t in self.turnos]