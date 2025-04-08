"""Modulo que inicia una tarea y muestra información al completarse."""


class Tarea:
    """Class que representa a una tarea"""


    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion
        self.completada = False
        self.feedback = None


    def marcar_completada(self):
        """Funcion que establece como completada la tarea una vez termina"""
        self.completada = True


    def __str__(self):
        """Representación legible de la tarea para mostrar en consola"""
        estado = "✔️ Completada" if self.completada else "⏳ Pendiente"
        return f"{self.nombre} ({self.duracion} min) - {estado}"


    def agregar_feedback(self,mensaje):
        """Funcion agrega un feedback al final del pomodoro"""
        self.feedback = mensaje
