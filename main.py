"""Modulo que inicia el programa."""


from pomodoro.tarea import Tarea

from pomodoro.gestor import GestorPomodoro

gestor = GestorPomodoro()

t1 = Tarea("Testear el pomodoro" , 10)
t2 = Tarea("Fase dos del testeo" , 20)

gestor.agregar_tarea(t1)

gestor.mostrar_tareas()

gestor.agregar_tarea(t2)

gestor.mostrar_tareas()

gestor.iniciar_pomodoro(t1)

gestor.mostrar_tareas_completas()
