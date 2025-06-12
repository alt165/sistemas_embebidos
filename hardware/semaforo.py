import RPi.GPIO as GPIO
import time


class Semaforo:

    def __init__(self, pin_rojo, pin_amarillo, pin_verde, tiempo_rojo=10, tiempo_verde=15, tiempo_amarillo=3):
        self.pins = {
            "red": pin_rojo,
            "yellow": pin_amarillo,
            "green": pin_verde
        }
        self.tiempos = {
            "red": tiempo_rojo,
            "green": tiempo_verde,
            "yellow": tiempo_amarillo
        }
        self.estado = "red"
        GPIO.setmode(GPIO.BCM)
        for pin in self.pins.values():
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

    def _encender(self, color):
        for c, pin in self.pins.items():
            GPIO.output(pin, GPIO.HIGH if c == color else GPIO.LOW)
        self.estado = color
        print(f"Semáforo en {color.upper()}")
        self._temporizador(color)

    def cambiar_a_rojo(self):
        self._encender("red")

    def cambiar_a_amarillo(self):
        self._encender("yellow")

    def cambiar_a_verde(self):
        self._encender("green")

    def _temporizador(self, color):
        segundos = self.tiempos[color]
        for i in range(segundos, 0, -1):
            print(f"{color.upper()} - {i} segundos", end="\r")
            time.sleep(1)

    def limpiar(self):
        for pin in self.pins.values():
            GPIO.output(pin, GPIO.LOW)
        GPIO.cleanup()
