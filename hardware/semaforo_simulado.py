import time

class SemaforoSimulado:
    def __init__(self, canvas, x):
        self.canvas = canvas
        self.x = x
        self.luces = {
            "red": canvas.create_oval(x, 20, x+50, 70, fill="gray"),
            "yellow": canvas.create_oval(x, 80, x+50, 130, fill="gray"),
            "green": canvas.create_oval(x, 140, x+50, 190, fill="gray"),
        }
        self.texto = canvas.create_text(x+25, 230, text="", font=("Arial", 14))
        self.duracion = {
            "red": 5,
            "yellow": 2,
            "green": 5
        }

    def cambiar_a_rojo(self):
        self._encender("red")

    def cambiar_a_amarillo(self):
        self._encender("yellow")

    def cambiar_a_verde(self):
        self._encender("green")

    def _encender(self, color):
        for c in self.luces:
            self.canvas.itemconfig(self.luces[c], fill="gray")
        self.canvas.itemconfig(self.luces[color], fill=color)
        print(f"💡 Semáforo en {color.upper()}")
        self._mostrar_cuenta_regresiva(self.duracion[color])

    def _mostrar_cuenta_regresiva(self, segundos):
        for i in range(segundos, 0, -1):
            self.canvas.itemconfig(self.texto, text=f"{i} s")
            self.canvas.update()
            time.sleep(1)
        self.canvas.itemconfig(self.texto, text="")