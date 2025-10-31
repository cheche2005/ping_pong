"""
FECHA: 2025-10-31
AUTOR(ES): José Prado
DESCRIPCIÓN: Inicializa el programa
"""

#---------------------------------IMPORTS


import os



#---------------------------------FUNCIONES

def mostrar_titulo(titulo):
    print(titulo)

def mostrar_menu(items):
    list(map(print,items))

def pedir_opcion():
        return input(">>> ")

def limpiar_pantalla():
    os.system("clear")

