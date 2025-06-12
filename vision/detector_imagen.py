import cv2


def detectar_vehiculo(ruta_camara=0):
    cap = cv2.VideoCapture(ruta_camara)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        # print("No se pudo acceder a la cámara o leer el frame.") # Opcional: para depuración
        return False

    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, umbral = cv2.threshold(gris, 120, 255, cv2.THRESH_BINARY)
    contornos, _ = cv2.findContours(umbral, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contorno in contornos:
        area = cv2.contourArea(contorno)
        if area > 1000:  # Ajusta este valor según el tamaño esperado de un vehículo en tu imagen
            return True

    return False
