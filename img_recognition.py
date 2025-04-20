import os
os.environ["QT_QPA_PLATFORM"] = "xcb"  # Para evitar errores en Ubuntu con Wayland

from ultralytics import YOLO
import cv2

# Cargar el modelo YOLOv8
model = YOLO("yolov8n.pt")  # Puedes usar también yolov8s.pt o una versión entrenada

# Leer la imagen que subiste (cambia el nombre si guardaste diferente)
img_path = "vehiculos.jpg"
img = cv2.imread(img_path)

if img is None:
    print("❌ No se pudo cargar la imagen.")
    exit()

# Ejecutar detección
results = model(img)

# Mostrar resultados por consola
print("Clases detectadas:")
for r in results:
    for box in r.boxes:
        cls = int(box.cls[0])
        name = model.names[cls]
        print(f"- {name}")

        # Dibujar solo si es vehículo
        if name in ["car", "motorbike", "bus", "truck"]:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, name, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            


# Mostrar la imagen
cv2.imshow("Vehículos detectados", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
