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
    vista.dimensionar_pantalla_juego(modelo.ANCHO_PANTALLA, modelo.ALTO_PANTALLA, b"", 60)
   # vista.limpiar_pantalla()

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
    vista.empezar_dibujo()
    vista.mostrar_linea_central(modelo.ANCHO_PANTALLA, modelo.ALTO_PANTALLA)
    vista.mostrar_arcos(modelo.ANCHO_PANTALLA, modelo.ALTO_PANTALLA, modelo.RADIO_CIRCULO_CENTRAL)
    vista.mostrar_paletas(modelo.ANCHO_PANTALLA, modelo.ALTO_PANTALLA, jugador["ancho"], jugador["alto"])
    vista.mostrar_circulo_central(modelo.ANCHO_PANTALLA, modelo.ALTO_PANTALLA, modelo.RADIO_CIRCULO_CENTRAL)
    vista.mostrar_boton_menu(modelo.ANCHO_PANTALLA)
    vista.marco_menu(modelo.ANCHO_PANTALLA)
    vista.titulo_menu_juego(modelo.ANCHO_PANTALLA)
    vista.opciones_menu_juego(["(h) hola", "(p) adios"], modelo.ANCHO_PANTALLA)
   # sets_ia = " ".join(["W"] * modelo.sets_ia)
   # sets_jugador = " ".join(["W"] * modelo.sets_jugador) 
    vista.mostrar_pelota(modelo.ANCHO_PANTALLA, modelo.ALTO_PANTALLA, modelo.pelota["radio"])
    vista.terminar_dibujo()

def main():
    """Controla el flujo general del programa."""
    while True:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            jugar()
            dibujar_elementos_controlador()
            if raylib.IsKeyPressed(raylib.KEY_R):
                break
        elif opcion == "q":
            vista.limpiar_pantalla()
            print("Gracias por jugar ")
            time.sleep(1)
            break
        else:
            print("Opción inválida.")
            time.sleep(1)
            vista.limpiar_pantalla()
    vista.cerrar_ventana()
#----------------------------- EJECUCIÓN -----------------------------
if __name__ == "__main__":
    main()

