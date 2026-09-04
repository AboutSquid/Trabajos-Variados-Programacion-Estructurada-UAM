"""
MedidorDeMiembros

Mide la longitud de cada dedo de la mano usando la camara, MediaPipe
(deteccion de landmarks de la mano, Tasks API) y OpenCV.

Por que hace falta "calibrar":
Una camara normal no sabe por si sola a que distancia real esta tu mano
(no tiene profundidad metrica), asi que no puede convertir pixeles a
centimetros sin ayuda. Por eso el programa primero pide una CALIBRACION:
le dices el tamano real de un objeto conocido (una tarjeta, un billete,
una regla...) y marcas sus dos extremos con el mouse sobre el video.
Con eso calcula la relacion pixeles/cm.

Despues, mientras muestres la mano A LA MISMA DISTANCIA de la camara a la
que estaba el objeto de referencia, el programa suma la distancia entre
las articulaciones de cada dedo y la convierte a centimetros.

Controles:
  - Durante la calibracion: click izquierdo en los 2 extremos del objeto
    de referencia, y luego escribe su longitud real en cm en la consola.
  - 'c' : repetir la calibracion
  - 'q' / ESC : salir

Requisitos (instalar antes de correr):
    pip install opencv-python mediapipe

La primera vez que se ejecuta, descarga automaticamente el modelo
"hand_landmarker.task" (~7.5 MB) de Google en esta misma carpeta si no
existe todavia (requiere conexion a internet solo esa vez).
"""

import math
import os
import urllib.request

import cv2
import mediapipe as mp
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision as mp_vision

CARPETA = os.path.dirname(os.path.abspath(__file__))
MODELO_PATH = os.path.join(CARPETA, "hand_landmarker.task")
MODELO_URL = (
    "https://storage.googleapis.com/mediapipe-models/hand_landmarker/"
    "hand_landmarker/float16/latest/hand_landmarker.task"
)

# Landmarks que forman cada dedo (de la base a la punta), segun MediaPipe Hands
FINGERS = {
    "Pulgar": [1, 2, 3, 4],
    "Indice": [5, 6, 7, 8],
    "Medio": [9, 10, 11, 12],
    "Anular": [13, 14, 15, 16],
    "Menique": [17, 18, 19, 20],
}

FINGER_COLORS = {
    "Pulgar": (255, 0, 0),
    "Indice": (0, 255, 0),
    "Medio": (0, 255, 255),
    "Anular": (255, 0, 255),
    "Menique": (0, 128, 255),
}

# Conexiones entre landmarks para dibujar el esqueleto de la mano
CONEXIONES_MANO = [(c.start, c.end) for c in mp_vision.HandLandmarksConnections.HAND_CONNECTIONS]


class Calibrador:
    def __init__(self):
        self.puntos = []
        self.px_por_cm = None

    def click(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN and len(self.puntos) < 2:
            self.puntos.append((x, y))

    def reset(self):
        self.puntos = []
        self.px_por_cm = None

    def calibrado(self):
        return self.px_por_cm is not None


def asegurar_modelo():
    if os.path.exists(MODELO_PATH):
        return
    print("Descargando modelo de deteccion de manos (una sola vez)...")
    urllib.request.urlretrieve(MODELO_URL, MODELO_PATH)
    print("Modelo descargado.\n")


def crear_detector():
    base_options = mp_python.BaseOptions(
        model_asset_path=MODELO_PATH,
        delegate=mp_python.BaseOptions.Delegate.CPU,
    )
    opciones = mp_vision.HandLandmarkerOptions(
        base_options=base_options,
        running_mode=mp_vision.RunningMode.VIDEO,
        num_hands=2,
        min_hand_detection_confidence=0.6,
        min_tracking_confidence=0.6,
    )
    return mp_vision.HandLandmarker.create_from_options(opciones)


def distancia_px(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def landmark_a_px(landmark, ancho, alto):
    return (int(landmark.x * ancho), int(landmark.y * alto))


def longitud_dedo_px(landmarks_px, indices):
    puntos = [landmarks_px[i] for i in indices]
    total = 0.0
    for i in range(len(puntos) - 1):
        total += distancia_px(puntos[i], puntos[i + 1])
    return total, puntos


def dibujar_mano(frame, landmarks_px):
    for a, b in CONEXIONES_MANO:
        cv2.line(frame, landmarks_px[a], landmarks_px[b], (200, 200, 200), 2)
    for p in landmarks_px:
        cv2.circle(frame, p, 3, (255, 255, 255), -1)


def pedir_longitud_real():
    while True:
        try:
            texto = input("Longitud real del objeto de referencia en cm: ")
            valor = float(texto.replace(",", "."))
            if valor > 0:
                return valor
        except ValueError:
            pass
        print("Escribe un numero valido, ej: 8.56")


def main():
    asegurar_modelo()
    detector = crear_detector()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("No se pudo abrir la camara.")
        return

    calibrador = Calibrador()

    ventana = "MedidorDeMiembros - dedos"
    cv2.namedWindow(ventana)
    cv2.setMouseCallback(ventana, calibrador.click)

    print("=== Calibracion ===")
    print("Coloca un objeto de longitud conocida (tarjeta, billete, regla...)")
    print("a la MISMA distancia de la camara donde luego pondras tu mano.")
    print("Haz click en sus dos extremos sobre la ventana de video.")
    print("Presiona 'c' en cualquier momento para recalibrar, 'q' para salir.\n")

    timestamp_ms = 0

    while True:
        ok, frame = cap.read()
        if not ok:
            print("No se pudo leer de la camara.")
            break

        frame = cv2.flip(frame, 1)
        alto, ancho = frame.shape[:2]

        # --- Calibracion pendiente ---
        if not calibrador.calibrado():
            for p in calibrador.puntos:
                cv2.circle(frame, p, 6, (0, 0, 255), -1)
            if len(calibrador.puntos) == 2:
                cv2.line(frame, calibrador.puntos[0], calibrador.puntos[1], (0, 0, 255), 2)
                px = distancia_px(calibrador.puntos[0], calibrador.puntos[1])
                cv2.imshow(ventana, frame)
                cv2.waitKey(1)
                cm = pedir_longitud_real()
                calibrador.px_por_cm = px / cm
                print(f"Calibracion lista: {calibrador.px_por_cm:.2f} px/cm\n")
            else:
                cv2.putText(
                    frame,
                    "Click en los 2 extremos del objeto de referencia",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2,
                )
                cv2.imshow(ventana, frame)
                tecla = cv2.waitKey(1) & 0xFF
                if tecla in (ord("q"), 27):
                    break
                elif tecla == ord("c"):
                    calibrador.reset()
                continue

        # --- Deteccion de manos ---
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_imagen = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        resultado = detector.detect_for_video(mp_imagen, timestamp_ms)
        timestamp_ms += 33  # ~30 fps

        if resultado.hand_landmarks:
            for landmarks in resultado.hand_landmarks:
                landmarks_px = [landmark_a_px(lm, ancho, alto) for lm in landmarks]
                dibujar_mano(frame, landmarks_px)

                y_texto = 60
                for nombre, indices in FINGERS.items():
                    largo_px, puntos = longitud_dedo_px(landmarks_px, indices)
                    largo_cm = largo_px / calibrador.px_por_cm
                    color = FINGER_COLORS[nombre]

                    punta = puntos[-1]
                    cv2.putText(
                        frame,
                        f"{largo_cm:.1f}cm",
                        (punta[0] + 8, punta[1]),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        color,
                        2,
                    )

                    cv2.putText(
                        frame,
                        f"{nombre}: {largo_cm:.1f} cm",
                        (10, y_texto),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        color,
                        2,
                    )
                    y_texto += 25
        else:
            cv2.putText(
                frame,
                "Muestra tu mano a la camara",
                (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2,
            )

        cv2.putText(
            frame,
            "'c' recalibrar   'q' salir",
            (10, alto - 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            1,
        )

        cv2.imshow(ventana, frame)
        tecla = cv2.waitKey(1) & 0xFF
        if tecla in (ord("q"), 27):
            break
        elif tecla == ord("c"):
            calibrador.reset()
            print("\n=== Recalibrando ===")
            print("Haz click en los dos extremos del nuevo objeto de referencia.")

    detector.close()
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
