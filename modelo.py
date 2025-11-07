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
VIDAS_INICIALES_IA = 3
POSICION_INICIAL_PADDLE_Y = ALTO_PANTALLA / 2 - PADDLE_ALTO / 2
POSICION_INICIAL_JUGADOR_X = 0
POSICION_INICIAL_IA_X = ANCHO_PANTALLA - PADDLE_ANCHO
VELOCIDAD_INICIAL_PELOTA_X = 8
VELOCIDAD_INICIAL_PELOTA_Y = 8
RADIO_CIRCULO_CENTRAL = 100
puntos_jugador = 0
puntos_ia = 0
vidas_jugador = VIDAS_INICIALES
vidas_ia = VIDAS_INICIALES_IA
sets_jugador = 0
sets_ia = 0

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
    "velocidad": 5.5
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

    centro_ia = ia["y"] + ia["alto"] / 2
    margen_error = random.uniform(-40, 40)

    # zona muerta: si la pelota está cerca, no reacciona
    if abs(pelota["y"] - centro_ia) > 10:
        if pelota["y"] + margen_error < centro_ia:
            ia["y"] -= ia["velocidad"]
        elif pelota["y"] + margen_error > centro_ia:
            ia["y"] += ia["velocidad"]

    # Mantener dentro de pantalla
    ia["y"] = max(0, min(ALTO_PANTALLA - ia["alto"], ia["y"]))

def movimiento_jugador():
    # 1. Detectar Entrada
    if raylib.IsKeyDown(raylib.KEY_UP):
        jugador["y"] -= jugador["velocidad"]
    elif raylib.IsKeyDown(raylib.KEY_DOWN):
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

    # Dirección horizontal aleatoria (izquierda o derecha)
    pelota["vel_x"] = random.choice([-1, 1]) * VELOCIDAD_INICIAL_PELOTA_X

    # Ángulo vertical aleatorio entre -75° y +75° aprox.
    pelota["vel_y"] = random.uniform(-1.0, 1.0) * VELOCIDAD_INICIAL_PELOTA_Y * 0.8

def anotacion_punto_jugador(): # Esta funcion se llama cuando se aumenta el puntaje del jugador
    if pelota["x"] < 0:
        global puntos_jugador
        puntos_jugador += 1
        reiniciar_pelota()
        reiniciar_paddles()
        if puntos_jugador >= PUNTOS_GANAR:
            return ganar_ronda()

def anotacion_punto_ia():
    if pelota["x"] > ANCHO_PANTALLA:
        global puntos_ia
        puntos_ia += 1
        reiniciar_pelota()
        reiniciar_paddles()
        if puntos_ia >= PUNTOS_GANAR:
            return perder_ronda()

def ganar_ronda(): #Esta funcion es llamada cuando un jugador gana una ronda
    global vidas_ia, sets_ia
    vidas_ia -= 1
    sets_ia += 1
    if vidas_ia <= 0:
        return "Has ganado la partida"

def perder_ronda(): #Esta funcion es llamada cuando un jugador pierde una ronda
    global vidas_jugador, sets_jugador
    vidas_jugador -= 1
    sets_jugador += 1
    if vidas_jugador <= 0:
        return "Has perdido la partida"

def colision_pelota_paleta(): #Detecta colisiones entre la pelota y las paletas

     # --- Jugador (izquierda) ---
    if (
        pelota["x"] - pelota["radio"] <= jugador["x"] + jugador["ancho"] and
        jugador["y"] < pelota["y"] < jugador["y"] + jugador["alto"]
    ):
        pelota["vel_x"] = abs(pelota["vel_x"])
        # Ángulo según el punto de impacto
        offset = (pelota["y"] - (jugador["y"] + jugador["alto"]/2)) / (jugador["alto"]/2)
        pelota["vel_y"] = offset * abs(pelota["vel_x"])

    # --- IA (derecha) ---
    if (
        pelota["x"] + pelota["radio"] >= ia["x"] and
        ia["y"] < pelota["y"] < ia["y"] + ia["alto"]
    ):
        pelota["vel_x"] = -abs(pelota["vel_x"])
        offset = (pelota["y"] - (ia["y"] + ia["alto"]/2)) / (ia["alto"]/2)
        pelota["vel_y"] = offset * abs(pelota["vel_x"])

def reiniciar_partida(): # Reinicia todo el estado del juego a sus valores iniciales
    global puntos_jugador, puntos_ia,  vidas_jugador, vidas_ia
    puntos_jugador = 0
    puntos_ia = 0
    vidas_jugador = vidas_ia = VIDAS_INICIALES
    reiniciar_pelota()
    reiniciar_paddles()
