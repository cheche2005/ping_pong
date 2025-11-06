"""
FECHA: 2025-10-31
AUTOR(ES): José Prado, Daniel Caraballo y Angel Linares.
DESCRIPCIÓN: Modelo. Maneja la lógica de negocio

NOTA: Lógica de negocio son las reglas y procedimientos que definen cómo opera nuestro juego
"""

#----------------------IMPORTS


import raylib
import random

#----------------------VARIABLES GLOBALES

ANCHO_PANTALLA = 1200
ALTO_PANTALLA = 700
PADDLE_ANCHO = 25
PADDLE_ALTO = 76
PUNTOS_GANAR = 12
VIDAS_INICIALES = 3
POSICION_INICIAL_PADDLE_Y = ALTO_PANTALLA / 2 - PADDLE_ALTO / 2
POSICION_INICIAL_JUGADOR_X = 0
POSICION_INICIAL_IA_X = ANCHO_PANTALLA - PADDLE_ANCHO
VELOCIDAD_INICIAL_PELOTA_X = 5
VELOCIDAD_INICIAL_PELOTA_Y = 5
puntos = 0
vidas = VIDAS_INICIALES

# --- Diccionario del Jugador ---

jugador = {
    "x": POSICION_INICIAL_JUGADOR_X,
    "y": POSICION_INICIAL_PADDLE_Y, # Posición Y centrada
    "ancho": PADDLE_ANCHO,
    "alto": PADDLE_ALTO,
    "velocidad": 8
}

# --- Diccionario de la IA ---

ia = {
    "x": POSICION_INICIAL_IA_X,
    "y": POSICION_INICIAL_PADDLE_Y,
    "ancho": PADDLE_ANCHO,
    "alto": PADDLE_ALTO,
    "velocidad": 6
}

# --- Diccionario de la Pelota ---

pelota = {
    "x": ANCHO_PANTALLA / 2,     # Posición X inicial (centro)
    "y": ALTO_PANTALLA / 2,      # Posición Y inicial (centro)
    "dx": random.choice([-VELOCIDAD_INICIAL_PELOTA_X, VELOCIDAD_INICIAL_PELOTA_X]), # Velocidad y direccion en X
    "dy": random.choice([-VELOCIDAD_INICIAL_PELOTA_Y, VELOCIDAD_INICIAL_PELOTA_Y]), # Velocidad y direccion en Y
    "radio": 25,                 # Radio de la pelota para dibujarla y calcular colisiones
    "vel_x": VELOCIDAD_INICIAL_PELOTA_X,                  # Velocidad en el eje X
    "vel_y": VELOCIDAD_INICIAL_PELOTA_Y                   # Velocidad en el eje Y
}

#----------------------FUNCIONES

def movimiento_ia():
    # Punto central del paddle de la IA
    centro_ia = ia["y"] + ia["alto"] / 2

    # 1. Comparar posiciones
    if pelota["y"] < centro_ia:
        # Mover hacia arriba
        ia["y"] -= ia["velocidad"]
    elif pelota["y"] > centro_ia:
        # Mover hacia abajo
        ia["y"] += ia["velocidad"]

def movimiento_jugador():
     # 1. Detectar Entrada
    if raylib.is_key_down(rl.KEY_UP):
        jugador["y"] -= jugador["velocidad"]
    elif raylib.is_key_down(rl.KEY_DOWN):
        jugador["y"] += jugador["velocidad"]

    # 2. Restringir (Clamp) el movimiento a los límites verticales
    
    if jugador["y"] < 0:
        jugador["y"] = 0
    elif jugador["y"] + jugador["alto"] > ALTO_PANTALLA:
        jugador["y"] = ALTO_PANTALLA - jugador["alto"]

def movimiento_pelota():
    pelota["x"] += pelota["vel_x"]
    pelota["y"] += pelota["vel_y"]

def colision_pelota_pisos():
    # 1. Colisión con el Techo (Borde Superior)
    # Si la parte superior de la pelota (centro - radio) toca o cruza 0
    if pelota["y"] - pelota["radio"] < 0:
        # Reposicionar la pelota para que no se pegue al borde
        pelota["y"] = pelota["radio"] 
        # Invertir la dirección vertical
        pelota["vel_y"] *= -1 

    # 2. Colisión con el Piso (Borde Inferior)
    # Si la parte inferior de la pelota (centro + radio) toca o cruza la altura máxima
    elif pelota["y"] + pelota["radio"] > ALTO_PANTALLA:
        # Reposicionar la pelota
        pelota["y"] = ALTO_PANTALLA - pelota["radio"]
        # Invertir la dirección vertical
        pelota["vel_y"] *= -1

def reiniciar_paddles():
    jugador["x"] = POSICION_INICIAL_JUGADOR_X
    ia["x"] = POSICION_INICIAL_IA_X
    jugador["y"] = ia["y"] = POSICION_INICIAL_PADDLE_Y 

def reiniciar_pelota():
    pelota["x"] = ANCHO_PANTALLA // 2
    pelota["y"] = ALTO_PANTALLA // 2
    pelota["dx"] = random.choice([-VELOCIDAD_INICIAL_PELOTA_X, VELOCIDAD_INICIAL_PELOTA_X])
    pelota["dy"] = random.choice([-VELOCIDAD_INICIAL_PELOTA_Y, VELOCIDAD_INICIAL_PELOTA_Y])

def anotacion_punto(): #esta funcion se llama cuando se aumenta el puntaje del jugador
    global puntos
    puntos += 1
    reiniciar_pelota()
    reiniciar_paddles()
    if puntos >= PUNTOS_GANAR:
        return ganar_ronda()

def ganar_ronda(): #Esta funcion es llamada cuando un jugador gana una ronda
   # reiniciar_pelota()
    return "ronda ganada!"


def colision_pelota_paleta(): #Detecta colisiones entre la pelota y las paletas
    
    # --- Jugador (izquierda) ---
    if (
        pelota["x"] - pelota["radio"] <= jugador["x"] + jugador["ancho"] and
        jugador["y"] < pelota["y"] < jugador["y"] + jugador["alto"]
    ):
        pelota["dx"] *= -1
        pelota["x"] = jugador["x"] + jugador["ancho"] + pelota["radio"]  # evita que se meta

    # --- IA (derecha) ---
    if (
        pelota["x"] + pelota["radio"] >= ia["x"] and
        ia["y"] < pelota["y"] < ia["y"] + ia["alto"]
    ):
        pelota["dx"] *= -1
        pelota["x"] = ia["x"] - pelota["radio"]


def reiniciar_partida(): # Reinicia todo el estado del juego a sus valores iniciales
    global puntos, vidas
    puntos = 0
    vidas = VIDAS_INICIALES
    reiniciar_pelota()
    reiniciar_paddles()


def ganar_partida(): #Se llama cuando el jugador gana todas las rondas o cumple la condición final del juego.
    reiniciar_partida()
    return "Partida ganada! Felicidades."


def perder_partida(): #Se llama cuando el jugador pierde todas las rondas
    reiniciar_partida()
    return "Partida perdida! Mala suerte."
