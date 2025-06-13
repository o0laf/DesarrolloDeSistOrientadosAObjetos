class Turno:
    def __init__(self, paciente, medico, fecha):
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha

    def mostrar_turno(self):
        return f"Turno: {self.fecha} - {self.paciente.nombre} con {self.medico.nombre} ({self.medico.especialidad})"