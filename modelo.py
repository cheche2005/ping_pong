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
PUNTOS = 0
VIDAS = VIDAS_INCIALES

# --- Diccionario del Jugador ---

jugador = {
    "x": 0,
    "y": ALTO_PANTALLA / 2 - PADDLE_ALTO / 2, # Posición Y centrada
    "ancho": PADDLE_ANCHO,
    "alto": PADDLE_ALTO,
    "velocidad": 8
}

# --- Diccionario de la IA ---

ia = {
    "x": ANCHO_PANTALLA - PADDLE_ANCHO,
    "y": ALTO_PANTALLA / 2 - PADDLE_ALTO / 2,
    "ancho": PADDLE_ANCHO,
    "alto": PADDLE_ALTO,
    "velocidad": 6
}

# --- Diccionario de la Pelota ---

pelota = {
    "x": ANCHO_PANTALLA / 2,     # Posición X inicial (centro)
    "y": ALTO_PANTALLA / 2,      # Posición Y inicial (centro)
    "radio": 25,                 # Radio de la pelota para dibujarla y calcular colisiones
    "vel_x": 5,                  # Velocidad en el eje X
    "vel_y": 5                   # Velocidad en el eje Y
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
    pass

def colision_pelota_pisos():
    pass

def anotacion_punto():
    pass

def ganar_ronda():
    pass

def ganar_partida():
    pass

def colision_pelota_paleta():
    pass

def reiniciar_partida():
    pass
