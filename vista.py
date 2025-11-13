"""
FECHA: 2025-11-13
AUTOR(ES): José Prado, Daniel Caraballo, Angel Linares
DESCRIPCIÓN: Vista. Maneja la interfaz de usuario y la presentación de datos
"""

#---------------------------------IMPORTS


import os
import raylib
import time

#---------------------------------FUNCIONES

corona = None

# Muestra el título del TUI
def mostrar_titulo(titulo):
    print(f"{titulo}\n")

# Muestra el menú del TUI
def mostrar_menu(items):
    list(map(print,items))

#Pide la opción en el menú TUI
def pedir_opcion():
        return input(">>> ")

#Limpia la pantalla
def limpiar_pantalla():
    os.system("clear")

#"""Le da dimensiones a la pantalla, hay que pasarle: Ancho de la ventana, alto de la ventana, título(ninguno), y los FPS"""

def dimensionar_pantalla_juego(ancho, alto, título, fps): 
    raylib.InitWindow(ancho, alto, título)
    raylib.SetTargetFPS(fps)

#Empieza a dibujar la pantalla
def empezar_dibujo():
    raylib.BeginDrawing()
    raylib.ClearBackground(raylib.BLUE)

#Termina de dibujar la pantalla
def terminar_dibujo():
    raylib.EndDrawing()

#Cierra la ventana
def cerrar_ventana():
    raylib.CloseWindow()   

#"""Muestra la línea central, hay que pasarle: ancho de la ventana, alto de la ventana"""
def mostrar_linea_central(ancho, alto):
    raylib.DrawLine(int(ancho/2),0,int(ancho/2), alto, raylib.WHITE)

#"""Muestra los arcos, hay que pasarle: x es el ancho de la ventana, y el alto de la ventana y el radio es el radio del círculo"""
def mostrar_arcos(x, y, radio):
    raylib.DrawCircleLines(0, int(y/2), radio, raylib.WHITE)
    raylib.DrawCircleLines(x,int(y/2), radio, raylib.WHITE)

#"""Muestra las paletas, hay que pasarle: x es el ancho de la ventana, y el alto de la ventana, base_rectángulo es la base del rectángulo y altura_rectángulo es la altura del rectángulo"""  
def mostrar_paletas(x_jugador, y_jugador, ancho_jugador, alto_jugador, x_ia, y_ia, ancho_ia, alto_ia):
    raylib.DrawRectangle(int(x_jugador), int(y_jugador), ancho_jugador, alto_jugador, raylib.WHITE)
    raylib.DrawRectangle(int(x_ia), int(y_ia), ancho_ia, alto_ia, raylib.WHITE)


#"""Muestra el círculo central, hay que pasarle: x es el ancho de la ventana, y el alto de la ventana, y el radio-circulo_central es el rádio de dicho círculo"""
def mostrar_circulo_central(x, y, radio_circulo_central):
    raylib.DrawCircleLines(int(x/2),int(y/2), radio_circulo_central, raylib.WHITE)

#"""Muestra la pelota en pantalla, hay que pasarle: x es el ancho de la ventana, y es el alto de la ventana y radio_pelota es el radio de la pelota"""
def mostrar_pelota(x, y, radio_pelota):
    raylib.DrawCircle(int(x), int(y), radio_pelota, raylib.BLACK)

#"""Muestra el botón del menú en el juego, solo hay que pasarle el ancho de la ventana"""
def mostrar_boton_menu(ancho):
    raylib.DrawRectangle(555,10, 95, 40, raylib.WHITE)
    raylib.DrawRectangleLines(555,10,95, 40, raylib.BLACK)
    raylib.DrawText(b"(r) Menu", int((ancho/2)-(raylib.MeasureText(b"(r) Menu", 20)/2)), 20, 20, raylib.BLACK)

#Dibuja el título del menú del juego, solo hay que pasarle el ancho de la ventana
def titulo_menu_juego(titulo, mensaje, ancho):
    raylib.DrawText(titulo.encode(),int((ancho / 2) - raylib.MeasureText(titulo.encode(), 40) / 2),40, 40, raylib.WHITE)
    raylib.DrawText(mensaje.encode(),int((ancho / 2) - raylib.MeasureText(mensaje.encode(), 30) / 2), 85, 30, raylib.YELLOW)

#Dibuja el marco del emnú del juego. solo hay que pasarle el ancho de la vengtana
def marco_menu(ancho):
    raylib.DrawRectangle(int((ancho/2) - (440/2)), 10,440, 500, raylib.BLACK) 
    raylib.DrawRectangleLines(int((ancho / 2) - (440 / 2)), 10, 440, 500, raylib.WHITE)

#DIbuja las opciones del menú del juego, solo hay que pasarle la lista de las opciones y el ancho de la ventana
def opciones_menu(opciones, ancho, seleccion):
    y_inicio = 200

    for i, opcion in enumerate(opciones):
        color = raylib.YELLOW if i == seleccion else raylib.WHITE
        raylib.DrawText(opcion.encode(),
                        int((ancho / 2) - raylib.MeasureText(opcion.encode(), 25) / 2)
                        ,y_inicio + (i * 60), 25
                        , color)

#Dibuja el puntaje de la IA y del jugador principal

def mostrar_puntaje(puntos_ia, puntos_jugador):
    raylib.DrawText(f"IA: {puntos_ia}".encode(), 200, 20, 30, raylib.BLACK)    
    raylib.DrawText(f"Jugador: {puntos_jugador}".encode(), 900, 20, 30, raylib.BLACK)

def cargar_texturas():
    global corona
    corona = raylib.LoadTexture(b"corona.png")

#Muestra los sets ganados por cada jugador
def mostrar_sets(sets_ia, sets_jugador):
    global corona
    for i in range(sets_ia):
        raylib.DrawTexture(corona, 200 + i*50, 70, raylib.WHITE)
    for i in range(sets_jugador):
        raylib.DrawTexture(corona, 980 + i*50, 70, raylib.WHITE)

#Función que muestra las instrucciones
def mostrar_instrucciones(instrucciones):
    print(*instrucciones, sep="\n\n")

#Función que espera al usuario
def esperar_usuario():
    input("\n>>> Ingrese ENTER para continuar: ")
    limpiar_pantalla()


def despedirse():
    print("Gracias por jugar!!! Vuelve pronto")
    time.sleep(1)

