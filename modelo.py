"""
FECHA: 2025-11-13
AUTOR(ES): José Prado, Daniel Caraballo y Ángel Linares.
DESCRIPCIÓN: Modelo. Maneja la lógica de negocio del juego de Ping Pong
"""
#----------------------IMPORTS---------------------------
import raylib
import random

#---------------------- CONSTANTES ----------------------
ANCHO_PANTALLA = 1200 #ESTO ES EL ANCHO DE LA PANTALLA
ALTO_PANTALLA = 700 #EL ALTO DE LA VENTANA
PADDLE_ANCHO = 25 #EL ANCHO DE LAS PALETAS
PADDLE_ALTO = 76 #EL ALTO DE LAS PALETAS
PUNTOS_GANAR = 12 #PUNTOS NECESARIOS PARA GANAR UNA RONDA
RADIO_CIRCULO_CENTRAL = 100 #RADIO DEL CIRCULO CENTRAL DEL JUEGO
VELOCIDAD_INICIAL_PELOTA_X = 8 #VELOCIDAD INICIAL HORIZONTAL DE LA PELOTA
VELOCIDAD_INICIAL_PELOTA_Y = 8 #VELOCIDAD INICIAL VERTICAL DE LA PELOTA
TITULO_TUI = "JUEGO DE PING PONG"
OPCIONES = [
            "1. Jugar",
            "2. Instrucciones",
            "q. Salir"
            ]
INSTRUCCIONES_TITULO = "INSTRUCCIONES"

INSTRUCCIONES = ["a. Presione la tecla Up Arrow (↑) para subir la paleta", "b. Presione la tecla Down Arrow (↓) para bajar la paleta ", "c. El ganador de la partida será aquel que resulte vencedor en 2 sets", "d. Para ganar un set, hay que anotar 12 puntos", "e. Cuando un participante de la partida gane un set, se reinicirán las puntuaciones", "f. Dentro de la partida, ingrese la tecla (r) para abrir el menú"]

OPCIONES_MENU_RESULTADO = ["1. Jugar de nuevo", "2. Salir al menú", "3. Salir del juego"]

OPCIONES_MENU_PAUSA = ["1. Volver al juego", "2. Reiniciar partida", "3. Salir de la partida", "4. Salir del juego"]
    
#---------------------- PUNTOS Y SETS ----------------------
puntos_jugador = 0
puntos_ia = 0
sets_jugador = 0
sets_ia = 0

#---------------------- JUGADOR ----------------------
POSICION_INICIAL_PADDLE_Y = ALTO_PANTALLA / 2 - PADDLE_ALTO / 2
POSICION_INICIAL_IA_X = 0
POSICION_INICIAL_JUGADOR_X = ANCHO_PANTALLA - PADDLE_ANCHO

#DICCIONARIOS QUE GUARDAN LAS PROPIEDADES DE FACTORES COMO ELJUGADOR, LA IA Y LA PELOTA

jugador = {
        "x": POSICION_INICIAL_JUGADOR_X,
        "y": POSICION_INICIAL_PADDLE_Y,
        "ancho": PADDLE_ANCHO,
        "alto": PADDLE_ALTO,
        "velocidad": 8
        }

ia = {
        "x": POSICION_INICIAL_IA_X,
        "y": POSICION_INICIAL_PADDLE_Y,
        "ancho": PADDLE_ANCHO,
        "alto": PADDLE_ALTO,
        "velocidad": 4.5
        }

#---------------------- PELOTA ----------------------
pelota = {
        "x": ANCHO_PANTALLA / 2,
        "y": ALTO_PANTALLA / 2,
        "vel_x": VELOCIDAD_INICIAL_PELOTA_X,
        "vel_y": VELOCIDAD_INICIAL_PELOTA_Y,
        "radio": 10
        }

#---------------------- FUNCIONES ----------------------
def movimiento_ia():
#MUEVE LA PALETA DE LA IA PARA SEGUIR LA PELOTA

    centro_ia = ia["y"] + ia["alto"] / 2
    margen_error = random.uniform(-40, 40)
    if abs(pelota["y"] - centro_ia) > 10:
        if pelota["y"] + margen_error < centro_ia:
            ia["y"] -= ia["velocidad"]
        elif pelota["y"] + margen_error > centro_ia:
            ia["y"] += ia["velocidad"]
    ia["y"] = max(0, min(ALTO_PANTALLA - ia["alto"], ia["y"]))

def movimiento_jugador():
#MUEVE LA PALETA DEL JUGADOR SEGUN LA TECLA PRESIONADA (ARRIBA O ABAJO EN ESTE CASO)
    
    if raylib.IsKeyDown(raylib.KEY_UP):
        jugador["y"] -= jugador["velocidad"]
    elif raylib.IsKeyDown(raylib.KEY_DOWN):
        jugador["y"] += jugador["velocidad"]
    jugador["y"] = max(0, min(ALTO_PANTALLA - jugador["alto"], jugador["y"]))

def movimiento_pelota():
#ACTUALIZA EL MOVIMIENTO DE LA PELOTA

    pelota["x"] += pelota["vel_x"]
    pelota["y"] += pelota["vel_y"]

def colision_pelota_pisos():
#DETECTA COLISIONES DE LA PELOTA CON EL TECHO Y CON EL PISO
    
    if pelota["y"] - pelota["radio"] < 0:
        pelota["y"] = pelota["radio"]
        pelota["vel_y"] *= -1
    elif pelota["y"] + pelota["radio"] > ALTO_PANTALLA:
        pelota["y"] = ALTO_PANTALLA - pelota["radio"]
        pelota["vel_y"] *= -1

def colision_pelota_paleta():
    # IA izquierda
    if pelota["x"] - pelota["radio"] <= ia["x"] + ia["ancho"] and ia["y"] < pelota["y"] < ia["y"] + ia["alto"]:
        pelota["vel_x"] = abs(pelota["vel_x"])
        offset = (pelota["y"] - (ia["y"] + ia["alto"]/2)) / (ia["alto"]/2)
        pelota["vel_y"] = offset * abs(pelota["vel_x"])
    # Jugador derecha
    if pelota["x"] + pelota["radio"] >= jugador["x"] and jugador["y"] < pelota["y"] < jugador["y"] + jugador["alto"]:
        pelota["vel_x"] = -abs(pelota["vel_x"])
        offset = (pelota["y"] - (jugador["y"] + jugador["alto"]/2)) / (jugador["alto"]/2)
        pelota["vel_y"] = offset * abs(pelota["vel_x"])

def reiniciar_pelota(): #ESTA FUNCION REINICIA LA PELOTA CADA VEZ QUE SE ANOTA UN PUNTO
    pelota["x"] = ANCHO_PANTALLA / 2
    pelota["y"] = ALTO_PANTALLA / 2
    pelota["vel_x"] = random.choice([-1,1]) * VELOCIDAD_INICIAL_PELOTA_X
    pelota["vel_y"] = random.uniform(-1.0,1.0) * VELOCIDAD_INICIAL_PELOTA_Y * 0.8

def reiniciar_paddles():
#COLOCA LAS PALETAS DEL JUGADOR Y LA IA EN SU POSICION INICIAL

    jugador["y"] = ia["y"] = POSICION_INICIAL_PADDLE_Y
    jugador["x"] = POSICION_INICIAL_JUGADOR_X
    ia["x"] = POSICION_INICIAL_IA_X

def reiniciar_puntos(): #REINICIA LOS PUNTOS DE LAS RONDAS
    global puntos_jugador, puntos_ia
    puntos_jugador = puntos_ia = 0

def anotacion_punto_jugador(): #SUMA UN PUNTO AL JUGADOR SI LA PELOTA PASA LA PALETA DE LA IA. REINICIA LA PELOTA Y LAS PALANCAS.
    global puntos_jugador
    if pelota["x"] - pelota["radio"] < 0:
        puntos_jugador += 1
        reiniciar_pelota()
        reiniciar_paddles()
        if puntos_jugador >= PUNTOS_GANAR:
            ganar_ronda()
#SUMA UN PUNTO A LA IA SI LA PELOTA PASA LA PALETA DEL JUGADOR. REINICIA LA PELOTA Y LAS PALETAS.

def anotacion_punto_ia():    
    global puntos_ia
    if pelota["x"] + pelota["radio"] > ANCHO_PANTALLA:
        puntos_ia += 1
        reiniciar_pelota()
        reiniciar_paddles()
        if puntos_ia >= PUNTOS_GANAR:
            perder_ronda()

def ganar_ronda():
    global sets_jugador
    sets_jugador += 1
    reiniciar_puntos()
    reiniciar_pelota()
    reiniciar_paddles()

def resultado_partida():
    if sets_jugador == 2 or sets_ia == 2:
       return True
    else:
       return False

def perder_ronda():
    global sets_ia
    sets_ia += 1
    reiniciar_puntos()
    reiniciar_pelota()
    reiniciar_paddles()

def reiniciar_partida():
    global sets_jugador, sets_ia
    sets_jugador = sets_ia = 0
    reiniciar_puntos()
    reiniciar_pelota()
    reiniciar_paddles()

def detectar_opcion(selección, num_opciones):
    if raylib.IsKeyPressed(raylib.KEY_DOWN):
       seleccion = (seleccion + 1) % num_opciones
    elif raylib.IsKeyPressed(raylib.KEY_UP):
       seleccion = (seleccion - 1) % num_opciones
    elif raylib.IsKeyPressed(raylib.KEY_ENTER):
       return seleccion 

def abrir_menu():
     if raylib.IsKeyPressed(raylib.KEY_R):
        return True
     else:
        return False


