import time
from vision.detector_imagen import detectar_vehiculo

class IntersectionController:
    def __init__(self, semaforo_sec, semaforo_principal, tiempo_min_verde):
        self.semaforo_secundario = semaforo_sec
        self.semaforo_principal = semaforo_principal
        self.tiempo_min_verde = tiempo_min_verde
        self.ultimo_cambio_a_verde = time.time()

    def manejar(self):
        ahora = time.time()
        tiempo_verde_actual = ahora - self.ultimo_cambio_a_verde

        if detectar_vehiculo():
            print("🚗 Vehículo detectado en secundaria")
            if tiempo_verde_actual >= self.tiempo_min_verde:
                print("⏱️ Tiempo mínimo cumplido. Cambiando paso a intersección secundaria.")
                self.semaforo_principal.cambiar_a_amarillo()
                self.semaforo_principal.cambiar_a_rojo()
                self.semaforo_secundario.cambiar_a_verde()
                self.semaforo_secundario.cambiar_a_amarillo()
                self.semaforo_secundario.cambiar_a_rojo()
                self.semaforo_principal.cambiar_a_verde()
                self.ultimo_cambio_a_verde = time.time()
            else:
                print(f"⛔ Esperando tiempo mínimo. Faltan {int(self.tiempo_min_verde - tiempo_verde_actual)}s")
        else:
            print("🟢 Sin vehículos en secundaria.")