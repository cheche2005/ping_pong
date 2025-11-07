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
   # modelo.reiniciar_partida()
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
    
    # Paletas en posiciones reales
    vista.mostrar_paletas(
        modelo.jugador["x"], modelo.jugador["y"], modelo.jugador["ancho"], modelo.jugador["alto"],
        modelo.ia["x"], modelo.ia["y"], modelo.ia["ancho"], modelo.ia["alto"]
    )
    
    vista.mostrar_circulo_central(modelo.ANCHO_PANTALLA, modelo.ALTO_PANTALLA, modelo.RADIO_CIRCULO_CENTRAL)
    vista.mostrar_boton_menu(modelo.ANCHO_PANTALLA)
   # vista.marco_menu(modelo.ANCHO_PANTALLA)
   # vista.titulo_menu_juego(modelo.ANCHO_PANTALLA)
   # vista.opciones_menu_juego(["(h) hola", "(p) adios"], modelo.ANCHO_PANTALLA)
    vista.mostrar_puntaje(modelo.puntos_ia, modelo.puntos_jugador)
    vista.mostrar_sets(modelo.sets_ia, modelo.sets_jugador)
    
    # Pelota en posición real
    vista.mostrar_pelota(modelo.pelota["x"], modelo.pelota["y"], modelo.pelota["radio"])
    
    vista.terminar_dibujo()                       

def main():
    """Controla el flujo general del programa."""
    while True:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            iniciar_juego()
            modelo.reiniciar_partida()
            while not raylib.WindowShouldClose():
                jugar()
                dibujar_elementos_controlador()
            if raylib.IsKeyPressed(raylib.KEY_R):
                vista.cerrar_ventana()
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

#----------------------------- EJECUCIÓN -----------------------------
if __name__ == "__main__":
    main()

