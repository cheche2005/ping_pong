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
        "2. Instrucciones",
        "q. Salir"
    ]
    vista.mostrar_menu(opciones)
    return vista.pedir_opcion()


def mostrar_instrucciones():
    """Muestra las instrucciones del juego."""
    vista.limpiar_pantalla()
    print("""
=== INSTRUCCIONES ===
- Usa las flechas ↑ y ↓ para mover tu paleta.
- Debes rebotar la pelota sin dejarla pasar.
- Si la pelota pasa al lado del enemigo, ganas un punto.
- Si la pelota pasa al tuyo, pierdes una vida.
- Ganas la ronda al llegar a 12 puntos.
- Tienes 3 vidas por partida.
""")
    input("\nPresiona ENTER para volver al menú...")


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

        # Verificar si la pelota sale de la pantalla
        if modelo.pelota["x"] < 0:
            modelo.vidas -= 1
            modelo.reiniciar_pelota()
            modelo.reiniciar_paddles()
            if modelo.vidas <= 0:
                break

        elif modelo.pelota["x"] > modelo.ANCHO_PANTALLA:
            modelo.puntos += 1
            modelo.reiniciar_pelota()
            modelo.reiniciar_paddles()
            if modelo.puntos >= modelo.PUNTOS_GANAR:
                break

        # Mostrar puntuación y vidas
        raylib.DrawText(
            f"Puntos: {modelo.puntos}".encode(),
            50, 20, 25, raylib.WHITE
        )
        raylib.DrawText(
            f"Vidas: {modelo.vidas}".encode(),
            1020, 20, 25, raylib.WHITE
        )

        vista.mostrar_menu_juego()
        raylib.EndDrawing()

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
        elif opcion == "2":
            mostrar_instrucciones()
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

