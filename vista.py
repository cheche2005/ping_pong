"""
FECHA: 2025-10-31
AUTOR(ES): José Prado
DESCRIPCIÓN: Vista. Maneja la interfaz de usuario y la presentación de datos
"""

#---------------------------------IMPORTS


import os
import raylib



#---------------------------------FUNCIONES

# Muestra el título del TUI
def mostrar_titulo(titulo):
    print(titulo)

# Muestra el menú del TUI
def mostrar_menu(items):
    list(map(print,items))

#Pide la opción en el menú TUI
def pedir_opcion():
        return input(">>> ")

#Limpia la pantalla
def limpiar_pantalla():
    os.system("clear")

"""Le da dimensiones a la pantalla, hay que pasarle: Ancho de la ventana, alto de la ventana, título(ninguno), y los FPS"""
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

"""Muestra la línea central, hay que pasarle: ancho de la ventana, alto de la ventana"""
def mostrar_linea_central(ancho, alto):
    raylib.DrawLine(int(ancho/2),0,int(ancho/2), alto, raylib.WHITE)

"""Muestra los arcos, hay que pasarle: x es el ancho de la ventana, y el alto de la ventana y el radio es el radio del círculo"""
def mostrar_arcos(x, y, radio):
    raylib.DrawCircleLines(0, int(y/2), radio, raylib.WHITE)
    raylib.DrawCircleLines(x,int(y/2), radio, raylib.WHITE)

"""Muestra las paletas, hay que pasarle: x es el ancho de la ventana, y el alto de la ventana, base_rectángulo es la base del rectángulo y altura_rectángulo es la altura del rectángulo"""  
def mostrar_paletas(x, y , base_rectángulo, altura_rectángulo):
    raylib.DrawRectangle(0,int((y/2) - (altura_rectángulo/2)), base_rectángulo, altura_rectángulo, raylib.WHITE)  
    raylib.DrawRectangle(x,int((y/2) - (altura_rectángulo/2)), base_rectángulo, altura_rectángulo, raylib.WHITE)  

"""Muestra el círculo central, hay que pasarle: x es el ancho de la ventana, y el alto de la ventana, y el radio-circulo_central es el rádio de dicho círculo"""
def mostrar_circulo_central(x, y, radio_circulo_central):
    raylib.DrawCircleLines(int(x/2),int(y/2), radio_circulo_central, raylib.WHITE)

"""Muestra la pelota en pantalla, hay que pasarle: x es el ancho de la ventana, y es el alto de la ventana y radio_pelota es el radio de la pelota"""
def mostrar_pelota(x, y, radio_pelota):
    raylib.DrawCircle(int(x/2),int(y/2), radio_pelota, raylib.BLACK) 

"""Muestra el botón del menú en el juego, solo hay que pasarle el ancho de la ventana"""
def mostrar_boton_menu(ancho):
    raylib.DrawRectangle(555,10, 95, 40, raylib.WHITE)
    raylib.DrawRectangleLines(555,10,95, 40, raylib.BLACK)
    raylib.DrawText(b"(r) Menu", int((ancho/2)-(raylib.MeasureText(b"(r) Menu", 20)/2)), 20, 20, raylib.BLACK)

#Dibuja el título del menú del juego, solo hay que pasarle el ancho de la ventana
def titulo_menu_juego(ancho):
    raylib.DrawText(b"OPCIONES", int((ancho/2)-(raylib.MeasureText(b"OPCIONES",40)/2)), 30, 40, raylib.WHITE)

#Dibuja el marco del emnú del juego. solo hay que pasarle el ancho de la vengtana
def marco_menu(ancho):
    raylib.DrawRectangle(int((ancho/2) - (440/2)), 10,440, 600, raylib.BLACK)  

#DIbuja las opciones del menú del juego, solo hay que pasarle la lista de las opciones y el ancho de la ventana
def opciones_menu_juego(elementos, ancho):
    j = 0
    for i in elementos:
      raylib.DrawText(i.encode(), int((ancho/2)-(raylib.MeasureText(i.encode(), 20)/2)),120 + 40*j, 20, raylib.WHITE)
      j = j+1

#    
