"""
FECHA: 2025-11-07
AUTOR(ES): José Prado, Daniel Caraballo y Ángel Linares
DESCRIPCIÓN: Controlador. Maneja el flujo principal del juego (interacción entre modelo y vista)
"""

#----------------------------- IMPORTS -----------------------------
import raylib
import modelo
import vista
import os
import time


#----------------------------- FUNCIONES -----------------------------

def mostrar_menu_principal():
   # """Muestra el menú principal en consola."""
    vista.limpiar_pantalla()
    vista.mostrar_titulo(modelo.TITULO_TUI)
    vista.mostrar_menu(modelo.OPCIONES)
    return vista.pedir_opcion()


#----------------------------- FUNCIONES PARA EL JUEGO----------------

def iniciar_juego():
    vista.dimensionar_pantalla_juego(modelo.ANCHO_PANTALLA, modelo.ALTO_PANTALLA, b"", 60)
    vista.cargar_texturas() 

"""    def cerrar_ventana():
    global corona
    if corona:
        raylib.UnloadTexture(corona)
    raylib.CloseWindow()
"""


def jugar():
   # """Actualiza la lógica principal del juego."""
    modelo.movimiento_jugador()
    modelo.movimiento_ia()
    modelo.movimiento_pelota()
    modelo.colision_pelota_pisos()
    modelo.colision_pelota_paleta()
    modelo.anotacion_punto_jugador()
    modelo.anotacion_punto_ia()

    resultado_jugador = modelo.anotacion_punto_jugador()
    resultado_ia = modelo.anotacion_punto_ia()

    if resultado_jugador:
        return resultado_jugador
    if resultado_ia:
        return resultado_ia

    return None


def dibujar_elementos_controlador():
   # """Dibuja los elementos del juego en pantalla."""
    vista.empezar_dibujo()
    vista.mostrar_linea_central(modelo.ANCHO_PANTALLA, modelo.ALTO_PANTALLA)
    vista.mostrar_arcos(modelo.ANCHO_PANTALLA, modelo.ALTO_PANTALLA, modelo.RADIO_CIRCULO_CENTRAL)

    vista.mostrar_paletas(
            modelo.jugador["x"], modelo.jugador["y"], modelo.jugador["ancho"], modelo.jugador["alto"],
            modelo.ia["x"], modelo.ia["y"], modelo.ia["ancho"], modelo.ia["alto"]
            )

    vista.mostrar_circulo_central(modelo.ANCHO_PANTALLA, modelo.ALTO_PANTALLA, modelo.RADIO_CIRCULO_CENTRAL)
    vista.mostrar_boton_menu(modelo.ANCHO_PANTALLA)

    vista.mostrar_puntaje(modelo.puntos_ia, modelo.puntos_jugador)
    vista.mostrar_sets(modelo.sets_ia, modelo.sets_jugador)
    vista.mostrar_pelota(modelo.pelota["x"], modelo.pelota["y"], modelo.pelota["radio"])

    vista.terminar_dibujo()

#------------------------- MENÚ DE PAUSA ---------------------------------

def mostrar_menu_pausa():
    """Muestra el menú de pausa durante la partida."""
    seleccion = 0
    ancho = modelo.ANCHO_PANTALLA

    while not raylib.WindowShouldClose():
        # Actualizar selección con teclas ↑ ↓
        if raylib.IsKeyPressed(raylib.KEY_DOWN):
            seleccion = (seleccion + 1) % 4
        elif raylib.IsKeyPressed(raylib.KEY_UP):
            seleccion = (seleccion - 1) % 4

        # Si el jugador presiona ENTER, devolver la opción
        if raylib.IsKeyPressed(raylib.KEY_ENTER):
            if seleccion == 0:
                return "jugar"
            elif seleccion == 1:
                return "reiniciar"
            elif seleccion == 2:
                return "menu"
            elif seleccion == 3:
                return "salir"

        # Dibujar menú de pausa
        vista.empezar_dibujo()
        vista.marco_menu(ancho)
        vista.titulo_menu_juego("MENÚ", "PAUSA" ,ancho)

        # Mostrar las opciones con resaltado
        vista.opciones_menu(modelo.OPCIONES_MENU_PAUSA, ancho, seleccion)
        vista.terminar_dibujo()



#------------------------- MENÚ DE RESULTADOS ----------------------------

def mostrar_menu_resultado(mensaje):
   # """Pantalla final al ganar, perder o presionar R."""
    seleccion = 0
    ancho = modelo.ANCHO_PANTALLA

    while not raylib.WindowShouldClose():
        # Navegar con flechas ↑ ↓
        if raylib.IsKeyPressed(raylib.KEY_DOWN):
            seleccion = (seleccion + 1) % 3
        elif raylib.IsKeyPressed(raylib.KEY_UP):
            seleccion = (seleccion - 1) % 3
        elif raylib.IsKeyPressed(raylib.KEY_ENTER):
            if seleccion == 0:
                return "jugar"
            elif seleccion == 1:
                return "menu"
            elif seleccion == 2:
                return "salir"

        # Dibujar menú de resultado
        vista.empezar_dibujo()
        vista.marco_menu(ancho)
        vista.titulo_menu_juego("FIN DE LA PARTIDA", mensaje, ancho)

        # Mostrar opciones del menú
        vista.opciones_menu(modelo.OPCIONES_MENU_RESULTADO, ancho, seleccion)

        vista.terminar_dibujo()


#--------------------- FLUJO PRINCIPAL DEL JUEGO ------------------------

def bucle_juego():
    vista.limpiar_pantalla()
    modelo.reiniciar_partida()
    iniciar_juego()

    mostrar_menu_final = False
    pausa_activa = False
    mensaje = ""

    while not raylib.WindowShouldClose():
        # Detecta si se abrió o no el menú
        abrir_menu_pausa = modelo.abrir_menu()
        # Fin de partida al mejor de 3
        mostrar_menu_final = modelo.resultado_partida()
        # Ronda normal
        if modelo.puntos_jugador >= modelo.PUNTOS_GANAR:
            modelo.ganar_ronda()
        elif modelo.puntos_ia >= modelo.PUNTOS_GANAR:
            modelo.perder_ronda()
        
        #Activar menú pausa
        if abrir_menu_pausa:
            accion = mostrar_menu_pausa()
            if accion == "jugar":
                continue  # reanuda la partida
            elif accion == "reiniciar":
                modelo.reiniciar_partida()
                continue
            elif accion == "menu":
                vista.cerrar_ventana()
                return None
            elif accion == "salir":
                vista.cerrar_ventana()
                exit()

        #Mensaje según victoria o derrota
        if modelo.sets_ia == 2:
            mensaje = "HAS PERDIDO"
        elif modelo.sets_jugador == 2:
            mensaje = "HAS GANADO"
        #Activar menú final
        if mostrar_menu_final:
            accion = mostrar_menu_resultado(mensaje)
            if accion == "jugar":
                modelo.reiniciar_partida()
                mostrar_menu = False
                mensaje = ""
                continue
            elif accion == "menu":
                vista.cerrar_ventana()
                return None
            elif accion == "salir":
                vista.cerrar_ventana()
                vista.limpiar_pantalla()
                exit()

        # Juego normal
        modelo.movimiento_jugador()
        modelo.movimiento_ia()
        modelo.movimiento_pelota()
        modelo.colision_pelota_pisos()
        modelo.colision_pelota_paleta()
        modelo.anotacion_punto_jugador()
        modelo.anotacion_punto_ia()

        vista.empezar_dibujo()
        vista.mostrar_linea_central(modelo.ANCHO_PANTALLA, modelo.ALTO_PANTALLA)
        vista.mostrar_arcos(modelo.ANCHO_PANTALLA, modelo.ALTO_PANTALLA, modelo.RADIO_CIRCULO_CENTRAL)
        vista.mostrar_paletas(
            modelo.jugador["x"], modelo.jugador["y"], modelo.jugador["ancho"], modelo.jugador["alto"],
            modelo.ia["x"], modelo.ia["y"], modelo.ia["ancho"], modelo.ia["alto"]
        )
        vista.mostrar_circulo_central(modelo.ANCHO_PANTALLA, modelo.ALTO_PANTALLA, modelo.RADIO_CIRCULO_CENTRAL)
        vista.mostrar_boton_menu(modelo.ANCHO_PANTALLA)
        vista.mostrar_puntaje(modelo.puntos_ia, modelo.puntos_jugador)
        vista.mostrar_sets(modelo.sets_ia, modelo.sets_jugador)
        vista.mostrar_pelota(modelo.pelota["x"], modelo.pelota["y"], modelo.pelota["radio"])
        vista.terminar_dibujo()

    vista.cerrar_ventana()


   # --- SEGUIR JUGANDO NORMALMENTE ---

resultado = jugar()   
if resultado:
    mostrar_menu = True
    mensaje = resultado


#--------------------- MENÚ PRINCIPAL DEL PROGRAMA ----------------------

def main():
    #"""Controla el flujo general del programa."""
    while True:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            vista.limpiar_pantalla()
            bucle_juego()
        elif opcion == "2":
            vista.limpiar_pantalla()
            vista.mostrar_titulo(modelo.INSTRUCCIONES_TITULO)
            vista.mostrar_instrucciones(modelo.INSTRUCCIONES)
            vista.esperar_usuario()
        elif opcion == "q":
            vista.limpiar_pantalla()
            print("Gracias por jugar!!! Vuelve pronto")
            time.sleep(1)
            break
        else:
            print("Opción inválida.")
            time.sleep(1)
            vista.limpiar_pantalla()



