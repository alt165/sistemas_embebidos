import tkinter as tk
import threading
import time
from hardware.semaforo_simulado import SemaforoSimulado
from controller.intersection_controller_gui import IntersectionControllerGUI

def main():
    root = tk.Tk()
    root.title("Simulación de Semáforos - Intersección")

    canvas = tk.Canvas(root, width=500, height=350)
    canvas.pack()

    semaforo_principal = SemaforoSimulado(canvas, 100)
    semaforo_secundario = SemaforoSimulado(canvas, 300)

    semaforo_principal.cambiar_a_verde()

    controller = IntersectionControllerGUI(semaforo_principal, semaforo_secundario, tiempo_min_verde=10)

    def manejar_evento():
        controller.manejar_evento()

    boton = tk.Button(root, text="🚗 Vehículo detectado", font=("Arial", 14), command=manejar_evento)
    boton.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()