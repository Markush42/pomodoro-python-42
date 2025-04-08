"""Module providing a function printing python version."""
import time
class GestorPomodoro:
    """Class que representa al gestor de pomodoro"""


    def __init__(self):
        self.tareas= []

    def agregar_tarea(self,tarea):
        """Function que agrega tareas al gestor."""
        self.tareas.append(tarea)

    def mostrar_tareas(self):
        """Function que muestra tareas al gestor."""
        # Muestra todas las tareas con su estado
        print("\n📋 Lista de Tareas:")
        for i, tarea in enumerate(self.tareas, 1):
            print(f"{i}. {tarea}")
        print()

    def iniciar_pomodoro(self, tarea):
        """Function que inicia el pomodoro."""
        print(f"🕒 Iniciando Pomodoro para: {tarea.nombre} ({tarea.duracion} minutos)")
        # Simulamos el temporizador con un contador regresivo (uno por cada segundo)
        for minuto in range(tarea.duracion, 0, -1):
            print(f"⌛ Quedan {minuto} minutos...")
            time.sleep(1)  # Aquí simula 1 segundo por cada minuto real

        tarea.marcar_completada()
        print(f"✅ ¡Pomodoro completado! Tarea '{tarea.nombre}' marcada como completada.\n")

        # 🆕 Pedir feedback al usuario
        feedback = input("📝 ¿Qué lograste durante este Pomodoro? Escribí un pequeño resumen: ")
        tarea.agregar_feedback(feedback)

    def mostrar_tareas_completas(self):
        """Funcion que muestra las tareas completadas."""
        print("\n📋 Lista final de Tareas con Feedback:")
        for tarea in self.tareas:
            estado = "✔️ Completada" if tarea.completada else "⏳ Pendiente"
            print(f"- {tarea.nombre} ({tarea.duracion} min) - {estado}")
            if tarea.feedback:
                print(f"  🧠 Feedback: {tarea.feedback}")
