import time
import threading

class IntersectionControllerGUI:
    def __init__(self, sem_principal, sem_secundario, tiempo_min_verde):
        self.semaforo_principal = sem_principal
        self.semaforo_secundario = sem_secundario
        self.tiempo_min_verde = tiempo_min_verde
        self.ultimo_verde_principal = time.time()
        self.en_transicion = False

    def manejar_evento(self):
        if self.en_transicion:
            print("⚠️ Esperando que termine la transición actual...")
            return

        tiempo_actual = time.time()
        if (tiempo_actual - self.ultimo_verde_principal) >= self.tiempo_min_verde:
            self.en_transicion = True
            threading.Thread(target=self._transicionar_semaforos).start()
        else:
            restante = int(self.tiempo_min_verde - (tiempo_actual - self.ultimo_verde_principal))
            print(f"⏳ Esperar {restante}s más antes de permitir paso a la secundaria.")

    def _transicionar_semaforos(self):
        self.semaforo_principal.cambiar_a_amarillo()
        self.semaforo_principal.cambiar_a_rojo()
        self.semaforo_secundario.cambiar_a_verde()
        self.semaforo_secundario.cambiar_a_amarillo()
        self.semaforo_secundario.cambiar_a_rojo()
        self.semaforo_principal.cambiar_a_verde()
        self.ultimo_verde_principal = time.time()
        self.en_transicion = False