"""
FECHA: 2025-10-31
AUTOR(ES): José Prado
DESCRIPCIÓN: Inicializa el programa
"""

#---------------------------------IMPORTS


import controlador



#---------------------------------FUNCIONES


def main():
    controlador.mostrar_tui()




#---------------------------------MAIN

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario")
    except Exception as e:
        print(f"Error inesperado: {e}")
