"""
FECHA: 2025-10-31
AUTOR(ES): José Prado
DESCRIPCIÓN: Vista. Maneja la interfaz de usuario y la presentación de datos
"""

#---------------------------------IMPORTS


import os
import raylib



#---------------------------------FUNCIONES

def mostrar_titulo(titulo):
    print(titulo)

def mostrar_menu(items):
    list(map(print,items))

def pedir_opcion():
        return input(">>> ")

def limpiar_pantalla():
    os.system("clear")

def mostrar_pantalla_juego(ancho, alto, título, fps):
    raylib.InitWindow(ancho, alto, título)
    raylib.SetTargetFPS(fps)
    limpiar_pantalla()
    

def mostrar_linea_central(ancho, alto):
    raylib.DrawLine(ancho/2,0, ancho/2, alto, raylib.WHITE)

def mostrar_arcos():
    raylib.DrawCircleLines(0, alto/2, radio_arcos, raylib.WHITE)
    raylib.DrawCircleLines(ancho, alto/2, radio_arcos, raylib.WHITE)
   
def mostrar_paletas(ancho, y , base_retángulo, altura_rectángulo):
    raylib.DrawRectangle(0,(y/2) - (altura_rectángulo/2), base_rectángulo, altura_rectángulo, raylib.WHITE)  
    raylib.DrawRectangle(ancho,(y/2) - (altura_rectángulo/2), base_rectángulo, altura_rectángulo, raylib.WHITE)  

def mostrar_circulo_central(ancho, alto, radio_circuilo_central):
    raylib.DrawCircleLines(ancho/2, alto/2, radio_circulo_central, raylib.WHITE)

def mostrar_pelota(x, y, radio_pelota):
    raylib.DrawCircle(x, y, radio_pelota, raylib.BLACK) 

def mostrar_boton_menu_():
    raylib.DrawRectangle(580-25,10, 90, 40, raylib.WHITE)
    raylib.DrawRectangleLines(580-25,10,91, 41, raylib.BLACK)
    raylib.DrawText(b"Menu", 560, 20, 30, raylib.BLACK)

def mostrar_menu():
    pass
