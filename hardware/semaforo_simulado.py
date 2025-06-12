# hardware/semaforo_simulado.py
import time
import tkinter as tk


class SemaforoSimulado:

    def __init__(self, canvas, x):
        self.canvas = canvas
        self.x = x
        self.luces = {
            "red": canvas.create_oval(x, 20, x + 50, 70, fill="gray"),
            "yellow": canvas.create_oval(x, 80, x + 50, 130, fill="gray"),
            "green": canvas.create_oval(x, 140, x + 50, 190, fill="gray"),
        }
        # El texto se posiciona un poco más abajo para no chocar con las luces
        self.texto = canvas.create_text(x + 25, 230, text="", font=("Arial", 14))
        self.duracion = {
            "red": 5,  # Duración para el rojo
            "yellow": 2,  # Duración para el amarillo
            "green": 5  # Duración para el verde
        }

    def cambiar_a_rojo(self):
        self._encender("red")

    def cambiar_a_amarillo(self):
        self._encender("yellow")

    def cambiar_a_verde(self):
        self._encender("green")

    def _encender(self, color):
        # Apagar todas las luces
        for c in self.luces:
            self.canvas.itemconfig(self.luces[c], fill="gray")
        # Encender la luz del color especificado
        self.canvas.itemconfig(self.luces[color], fill=color)
        print(f"💡 Semáforo en {color.upper()}")
        # Mostrar la cuenta regresiva para el color actual
        self._mostrar_cuenta_regresiva(self.duracion[color])

    def _mostrar_cuenta_regresiva(self, segundos):
        # Mostrar la cuenta regresiva en el texto asociado al semáforo
        for i in range(segundos, 0, -1):
            self.canvas.itemconfig(self.texto, text=f"{i} s")
            self.canvas.update()  # Asegura que la GUI se actualice
            time.sleep(1)  # Pausa por un segundo
        self.canvas.itemconfig(self.texto, text="")  # Limpiar el texto al finalizar la cuenta
