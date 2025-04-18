# 🚦 Sistema Inteligente de Control Semafórico

Este proyecto propone el desarrollo de un sistema de control de semáforos utilizando inteligencia artificial, enfocado en optimizar el tránsito en intersecciones donde una arteria principal es cortada por calles secundarias con tráfico esporádico.

> Proyecto desarrollado para la materia **Laboratorio de Sistemas Embebidos**  
> Universidad Nacional de Río Negro  
> **Integrantes**: Ángeles Rodríguez y José Lambrechts

---

## 🧠 ¿Qué hace este sistema?

- Detecta en tiempo real la presencia de vehículos en calles secundarias.
- Mantiene el semáforo en verde para la arteria principal mientras no se detecten vehículos.
- Cambia el semáforo solo cuando hay un vehículo esperando cruzar.
- Reduce tiempos de espera innecesarios y mejora la fluidez del tránsito.

---

## 🧩 Tecnologías y componentes

- 🔌 **Hardware**: Raspberry Pi 4, cámara USB o CSI, semáforo con LEDs.
- 🧠 **IA**: Modelos ligeros de visión computacional (ej. MobileNet, YOLO-tiny).
- ⚙️ **Lenguaje**: Python (detección + control).
- 💡 **Sensores opcionales**: PIR, radar o ultrasonido.

---

## 🗺️ Ubicación del caso de estudio

La intersección evaluada se encuentra en Dina Huapi, Río Negro (Argentina), sobre la **Ruta Nacional 40**.  
Coordenadas aproximadas:  
- -41.076953728160085, -71.1743732412131  
- -41.08258842663534, -71.1811792023927  
- -41.0721773684481, -71.16854603265422

---

## 🏗️ Cómo correr el proyecto (futuro)

> ⚠️ Esta sección se irá actualizando a medida que se avanza en el desarrollo.

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
