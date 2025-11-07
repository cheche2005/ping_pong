"""
FECHA: 2025-11-06
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
    """Muestra el menú principal en consola."""
    vista.limpiar_pantalla()
    vista.mostrar_titulo(" JUEGO DE PING PONG \n")
    opciones = [
        "1. Jugar",
        "q. Salir"
    ]
    vista.mostrar_menu(opciones)
    return vista.pedir_opcion()

def iniciar_juego():
    vista.mostrar_pantalla_juego(modelo.ANCHO_PANTALLA, modelo.ALTO_PANTALLA, b"Ping Pong", 60)


def jugar():
    # --- ACTUALIZACIÓN DE LÓGICA (modelo) ---
    modelo.reiniciar_partida()
    modelo.movimiento_jugador()
    modelo.movimiento_ia()
    modelo.movimiento_pelota()
    modelo.colision_pelota_pisos()
    modelo.colision_pelota_paleta()
    modelo.anotacion_punto_jugador()
    modelo.anotacion_punto_ia()

def dibujar_elementos_controlador():
    vista.mostrar_linea_central(modelo.ANCHO_PANTALLA, modelo.ALTO_PANTALLA)
    # vista.mostrar_arcos()
    vista.mostrar_paletas(modelo.ANCHO_PANTALLA, modelo.jugador["y"], jugador["ancho"], jugador["alto"])
    vista.mostrar_circulo_central(modelo.ANCHO_PANTALLA, modelo.ALTO_PANTALLA, )
    vista.mostrar_pelota(modelo.pelota["x"], modelo.pelota["y"], modelo.pelota["radio"])
    vista.mostrar_boton_menu()

    sets_ia = " ".join(["W"] * modelo.sets_ia)
    sets_jugador = " ".join(["W"] * modelo.sets_jugador)

def main():
    """Controla el flujo general del programa."""
    while not raylib.WindowShouldClose():
        opcion = mostrar_menu_principal()

        if opcion == "1":
            jugar()
            dibujar_elementos_controlador()
        elif opcion == "q":
            vista.limpiar_pantalla()
            print("Gracias por jugar ")
            time.sleep(1)
            break
        else:
            print("Opción inválida.")
            time.sleep(1)
            vista.limpiar_pantalla()

#----------------------------- EJECUCIÓN -----------------------------
if __name__ == "__main__":
    main()

