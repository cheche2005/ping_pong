"""
FECHA: 2025-10-31
AUTOR(ES): José Prado
DESCRIPCIÓN: Controlador. Maneja la interacción entre el modelo y la vista
"""

#---------------------------------IMPORTS


#Conecta este módulo con el módulo vista

import vista


#---------------------------------FUNCIONES


def mostrar_tui():
    while True:
        vista.limpiar_pantalla()
        # Muesta el tui
        titulo_principal = "PROGRAMA"
        menu_principal = ("1. Jugar", "q. Salir")
        vista.mostrar_titulo(titulo_principal)
        vista.mostrar_menu(menu_principal)
        opcion_principal = vista.pedir_opcion()

        # Controla las opciones del menú

        if opcion_principal == 'q':
            exit()
        else:
         vista.mostrar_pantalla_juego()


