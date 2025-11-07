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

def jugar():
    """Ejecuta una ronda completa del juego."""
    modelo.reiniciar_partida()

    while not raylib.WindowShouldClose():
        # --- ACTUALIZACIÓN DE LÓGICA (modelo) ---
        modelo.movimiento_jugador()
        modelo.movimiento_ia()
        modelo.movimiento_pelota()
        modelo.colision_pelota_pisos()
        modelo.colision_pelota_paleta()
"""
        # Mostrar puntuación y vidas
        raylib.DrawText(
            f"Puntos: {modelo.punto}".encode(),
            50, 20, 25, raylib.WHITE
        )
        raylib.DrawText(
            f"Vidas: {modelo.vidas}".encode(),
            1020, 20, 25, raylib.WHITE
        )

        vista.mostrar_menu_juego()
        raylib.EndDrawing()
"""
        # --- CONDICIONES DE FINAL ---
        if modelo.vidas <= 0:
            mostrar_mensaje_final(" Has perdido la partida ")
            break
        elif modelo.puntos >= modelo.PUNTOS_GANAR:
            mostrar_mensaje_final(" ¡Has ganado la ronda! ")
            break

    raylib.CloseWindow()


def mostrar_mensaje_final(texto):
    """Muestra mensaje de fin de partida o victoria."""
    vista.limpiar_pantalla()
    print("\n" + texto)
    input("\nPresiona ENTER para volver al menú...")


def main():
    """Controla el flujo general del programa."""
    while True:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            jugar()
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

