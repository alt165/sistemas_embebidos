import time
import threading


class IntersectionControllerGUI:

    def __init__(self, sem_vertical, sem_horizontal_izq, sem_horizontal_der, tiempo_verde_secundaria):
        self.semaforo_vertical = sem_vertical
        self.semaforo_horizontal_izq = sem_horizontal_izq
        self.semaforo_horizontal_der = sem_horizontal_der
        self.tiempo_verde_secundaria = tiempo_verde_secundaria  # Tiempo que las calles secundarias estarán en verde
        self.en_transicion = False
        self.ultimo_cambio_vertical_a_verde = time.time()  # Para controlar si la vertical debe esperar

        # Inicialmente, el semáforo vertical está en verde.
        self.semaforo_vertical.cambiar_a_verde()
        # Los semáforos horizontales deben empezar en rojo
        self.semaforo_horizontal_izq.cambiar_a_rojo()
        self.semaforo_horizontal_der.cambiar_a_rojo()

    def manejar_evento_horizontal(self, semaforo_activado):
        # semaforo_activado será 'izq' o 'der'
        if self.en_transicion:
            print("⚠️ Esperando que termine la transición actual...")
            return

        tiempo_actual = time.time()
        # Puedes añadir un tiempo mínimo que la vertical debe estar en verde antes de ceder el paso
        # Por ejemplo, si self.tiempo_min_verde_principal = 10, y (tiempo_actual - self.ultimo_cambio_vertical_a_verde) < self.tiempo_min_verde_principal:
        #   print("⛔ La calle vertical aún no ha cumplido su tiempo mínimo en verde.")
        #   return

        self.en_transicion = True
        # Iniciar la transición en un hilo separado para no congelar la GUI
        threading.Thread(target=self._transicionar_semaforos, args=(semaforo_activado,)).start()

    def _transicionar_semaforos(self, semaforo_activado):
        print(f"\n--- Transición activada por semáforo {semaforo_activado.upper()} ---")

        # 1. Semáforo Vertical a Amarillo
        print("🚦 Vertical: Cambiando a Amarillo")
        self.semaforo_vertical.cambiar_a_amarillo()
        # El sleep ya está en _mostrar_cuenta_regresiva de SemaforoSimulado

        # 2. Semáforo Vertical a Rojo
        print("🚦 Vertical: Cambiando a Rojo")
        self.semaforo_vertical.cambiar_a_rojo()
        # El sleep ya está en _mostrar_cuenta_regresiva de SemaforoSimulado

        # 3. Habilitar Semáforo Horizontal (el que detectó)
        if semaforo_activado == 'izq':
            print("🚦 Horizontal Izquierda: Cambiando a Verde")
            self.semaforo_horizontal_izq.cambiar_a_verde()
            time.sleep(self.tiempo_verde_secundaria)  # Este es el tiempo que estará en verde la secundaria
            print("🚦 Horizontal Izquierda: Cambiando a Amarillo")
            self.semaforo_horizontal_izq.cambiar_a_amarillo()
            print("🚦 Horizontal Izquierda: Cambiando a Rojo")
            self.semaforo_horizontal_izq.cambiar_a_rojo()

        elif semaforo_activado == 'der':
            print("🚦 Horizontal Derecha: Cambiando a Verde")
            self.semaforo_horizontal_der.cambiar_a_verde()
            time.sleep(self.tiempo_verde_secundaria)  # Este es el tiempo que estará en verde la secundaria
            print("🚦 Horizontal Derecha: Cambiando a Amarillo")
            self.semaforo_horizontal_der.cambiar_a_amarillo()
            print("🚦 Horizontal Derecha: Cambiando a Rojo")
            self.semaforo_horizontal_der.cambiar_a_rojo()

        # 4. Volver a Semáforo Vertical a Verde
        print("🚦 Vertical: Volviendo a Verde")
        self.semaforo_vertical.cambiar_a_verde()
        self.ultimo_cambio_vertical_a_verde = time.time()
        self.en_transicion = False
        print("--- Transición Finalizada ---")
