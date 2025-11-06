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

def mostrar_pantalla_juego():
    raylib.InitWindow(1200, 700, b"hola")
    raylib.SetTargetFPS(1200)
    limpiar_pantalla()
    while not raylib.WindowShouldClose():
       raylib.BeginDrawing()
       raylib.ClearBackground(raylib.BLUE)
       mostrar_linea_central()
       mostrar_circulo_central()
       mostrar_arcos()
       mostrar_paletas()
       mostrar_pelota()
       raylib.EndDrawing()
       mostrar_menu_juego()
    raylib.CloseWindow()

def mostrar_linea_central():
    raylib.DrawLine(600,0, 600, 700, raylib.WHITE)

def mostrar_arcos():
    raylib.DrawCircleLines(0, 350, 200, raylib.WHITE)
    raylib.DrawCircleLines(0+1200, 350, 200, raylib.WHITE)
   
def mostrar_paletas():
    raylib.DrawRectangle(0,350-38, 25, 76, raylib.WHITE)  
    raylib.DrawRectangle(0+1200-25,350-38, 25, 76, raylib.WHITE)

def mostrar_circulo_central():
    raylib.DrawCircleLines(600, 350, 100, raylib.WHITE)

def mostrar_pelota():
    raylib.DrawCircle(600, 350, 25, raylib.BLACK) 

def mostrar_menu_juego():
    raylib.DrawRectangle(580-25,10, 90, 40, raylib.WHITE)
    raylib.DrawRectangleLines(580-25,10,91, 41, raylib.BLACK)
    raylib.DrawText(b"Menu", 560, 20, 30, raylib.BLACK)
