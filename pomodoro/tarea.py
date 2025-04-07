class Tarea:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion
        self.completada = False
      
        
    def marcar_completada(self):
        self.completada = True