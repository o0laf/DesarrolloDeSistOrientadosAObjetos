from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    @abstractmethod
    def mostrar_info(self):
        pass

class Paciente(Persona):
    def mostrar_info(self):
        return f"Paciente: {self.nombre}, DNI: {self.dni}"

class Medico(Persona):
    def __init__(self, nombre, dni, especialidad):
        super().__init__(nombre, dni)
        self.especialidad = especialidad

    def mostrar_info(self):
        return f"Médico: {self.nombre}, DNI: {self.dni}, Especialidad: {self.especialidad}"
