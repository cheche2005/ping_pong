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
    vista.mostrar_titulo(" JUEGO DE PING PONG \n")
    opciones = [
            "1. Jugar",
            "q. Salir"
            ]
    vista.mostrar_menu(opciones)
    return vista.pedir_opcion()


#----------------------------- FUNCIONES PARA EL JUEGO----------------

def iniciar_juego():
    vista.dimensionar_pantalla_juego(modelo.ANCHO_PANTALLA, modelo.ALTO_PANTALLA, b"", 60)


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
        raylib.BeginDrawing()
        raylib.ClearBackground(raylib.DARKBLUE)

        vista.marco_menu(ancho)
        vista.titulo_menu_juego(ancho)

        # Mostrar mensaje recibido (ganado, perdido, reiniciado)
        raylib.DrawText(mensaje.encode(),
                        int((ancho / 2) - raylib.MeasureText(mensaje.encode(), 30) / 2),
                        120, 30, raylib.YELLOW)

        # Mostrar opciones del menú
        vista.opciones_menu_juego(["1. Jugar de nuevo", "2. Salir al menú", "3. Salir del juego"],
                                  ancho, seleccion)

        raylib.EndDrawing()


#--------------------- FLUJO PRINCIPAL DEL JUEGO ------------------------

def bucle_juego():
    modelo.reiniciar_partida()
    iniciar_juego()

    mostrar_menu = False
    mensaje = ""

    while not raylib.WindowShouldClose():
        # Detectar reinicio o fin de partida
        if raylib.IsKeyPressed(raylib.KEY_R):
            mostrar_menu = True
            mensaje = ""

        # Fin de partida al mejor de 3
        elif modelo.sets_jugador >= 2:
            mostrar_menu = True
            mensaje = "¡Has ganado la partida!"
        elif modelo.sets_ia >= 2:
            mostrar_menu = True
            mensaje = "Has perdido la partida!"
        # Ronda normal
        elif modelo.puntos_jugador >= modelo.PUNTOS_GANAR:
            modelo.ganar_ronda()
        elif modelo.puntos_ia >= modelo.PUNTOS_GANAR:
            modelo.perder_ronda()

        if mostrar_menu:
            accion = mostrar_menu_resultado(mensaje)
            if accion == "jugar":
                modelo.reiniciar_partida()
                mostrar_menu = False
                mensaje = ""
                continue
            elif accion == "menu":
                vista.cerrar_ventana()
                return
            elif accion == "salir":
                vista.cerrar_ventana()
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
            bucle_juego()
        elif opcion == "q":
            vista.limpiar_pantalla()
            print("Gracias por jugar!!! Vuelve pronto")
            time.sleep(1)
            break
        else:
            print("Opción inválida.")
            time.sleep(1)
            vista.limpiar_pantalla()


#----------------------------- EJECUCIÓN -----------------------------
if __name__ == "__main__":
    main()






