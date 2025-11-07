"""
FECHA: 2025-11-07
AUTOR(ES): José Prado, Daniel Caraballo y Angel Linares
DESCRIPCIÓN: Inicializa el programa
"""

#---------------------------------IMPORTS


import controlador


#---------------------------------FUNCIONES


def main():
    controlador.main()
    


#---------------------------------MAIN

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario")
    except Exception as e:
        print(f"Error inesperado: {e}")
