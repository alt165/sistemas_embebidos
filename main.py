import tkinter as tk
import threading
import time
from hardware.semaforo_simulado import SemaforoSimulado
from controller.intersection_controller_gui import IntersectionControllerGUI


def main():
    root = tk.Tk()
    root.title("Simulación de Semáforos - Intersección de 3 Vías")

    canvas = tk.Canvas(root, width=600, height=450, bg="lightgray")
    canvas.pack()

    # --- Dibujar la intersección para mejorar la visualización ---
    # Calle vertical (más ancha para semáforo central)
    canvas.create_rectangle(275, 0, 325, 450, fill="darkgray", outline="darkgray")
    # Calle horizontal
    canvas.create_rectangle(0, 200, 600, 250, fill="darkgray", outline="darkgray")

    # --- Posicionar los semáforos ---
    # Semaforo Vertical (superior)
    # Ubicado en la parte superior de la calle vertical
    sem_vertical = SemaforoSimulado(canvas, 275)  # x=275 para centrarlo en la calle vertical (ancho 50)
    canvas.create_text(sem_vertical.x + 25, 15, text="Calle Vertical", font=("Arial", 10, "bold"), fill="black")

    # Semaforo Horizontal Izquierda
    # Ubicado a la izquierda, sobre la calle horizontal
    sem_horizontal_izq = SemaforoSimulado(canvas, 100)  # x=100
    # Mover el semáforo para que sus luces y texto estén sobre la calle horizontal
    canvas.move(sem_horizontal_izq.luces["red"], 0, 200)
    canvas.move(sem_horizontal_izq.luces["yellow"], 0, 200)
    canvas.move(sem_horizontal_izq.luces["green"], 0, 200)
    canvas.move(sem_horizontal_izq.texto, 0, 200)
    canvas.create_text(sem_horizontal_izq.x + 25, 200 + 15, text="Lateral Izq.", font=("Arial", 10, "bold"), fill="black")

    # Semaforo Horizontal Derecha
    # Ubicado a la derecha, sobre la calle horizontal
    sem_horizontal_der = SemaforoSimulado(canvas, 450)  # x=450
    # Mover el semáforo para que sus luces y texto estén sobre la calle horizontal
    canvas.move(sem_horizontal_der.luces["red"], 0, 200)
    canvas.move(sem_horizontal_der.luces["yellow"], 0, 200)
    canvas.move(sem_horizontal_der.luces["green"], 0, 200)
    canvas.move(sem_horizontal_der.texto, 0, 200)
    canvas.create_text(sem_horizontal_der.x + 25, 200 + 15, text="Lateral Der.", font=("Arial", 10, "bold"), fill="black")

    # --- Inicializar el controlador de la intersección ---
    controller = IntersectionControllerGUI(
        sem_vertical,
        sem_horizontal_izq,
        sem_horizontal_der,
        tiempo_verde_secundaria=7  # Tiempo que una calle secundaria estará en verde si se activa
    )

    # --- Contenedor para los botones de detección ---
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    # --- Botones para simular detección de vehículos ---
    def on_detect_vertical():
        # Este botón simula una detección en la calle vertical, pero no activa un cambio de ciclo
        # según la lógica actual (vertical siempre en verde por defecto).
        print("🚗 Vehículo detectado en Calle Vertical (no inicia cambio de ciclo en esta lógica).")
        # Aquí podrías añadir una lógica futura si la vía principal también necesitara reaccionar.

    def on_detect_izq():
        controller.manejar_evento_horizontal('izq')

    def on_detect_der():
        controller.manejar_evento_horizontal('der')

    # Crear y empaquetar los botones
    boton_vertical = tk.Button(button_frame, text="🚗 Detectar Vertical", font=("Arial", 12), command=on_detect_vertical)
    boton_vertical.pack(side=tk.LEFT, padx=10)

    boton_izq = tk.Button(button_frame, text="🚗 Detectar Izq.", font=("Arial", 12), command=on_detect_izq)
    boton_izq.pack(side=tk.LEFT, padx=10)

    boton_der = tk.Button(button_frame, text="🚗 Detectar Der.", font=("Arial", 12), command=on_detect_der)
    boton_der.pack(side=tk.LEFT, padx=10)

    # --- Iniciar la GUI ---
    root.mainloop()


if __name__ == "__main__":
    main()
