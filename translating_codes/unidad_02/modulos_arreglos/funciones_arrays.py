#
#       ███╗░░░███╗░█████╗░██████╗░██╗░░░██╗██╗░░░░░░█████╗░░██████╗
#       ████╗░████║██╔══██╗██╔══██╗██║░░░██║██║░░░░░██╔══██╗██╔════╝
#       ██╔████╔██║██║░░██║██║░░██║██║░░░██║██║░░░░░██║░░██║╚█████╗░
#       ██║╚██╔╝██║██║░░██║██║░░██║██║░░░██║██║░░░░░██║░░██║░╚═══██╗
#       ██║░╚═╝░██║╚█████╔╝██████╔╝╚██████╔╝███████╗╚█████╔╝██████╔╝
#       ╚═╝░░░░░╚═╝░╚════╝░╚═════╝░░╚═════╝░╚══════╝░╚════╝░╚═════╝░
"""
Módulo donde voy a poner todas las funciones relacionadas a 
los vectores (o arreglos de una dimensión) y arreglos de 2 dimensiones

Funciones incluidas:
- leer_enteros:
- pedir_tamanio:
- cargar_vector:
- mostrar_vector:
- anexar_vectores:
- muestreo_multiple_inverso:
"""


def leer_enteros(msj):
    """Lee un entero desde la entrada estándar.

    Args:
        msj (str): El mensaje que se mostrará al usuario.

    Returns:
        int: El entero ingresado por el usuario.
    """
    while True:
        try:
            return int(input(msj))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")


def cargar_vector(N, vector):
    vector.extend([None]*N)  # redimensiona la lista para que tenga N elementos
    for i in range(N):
        numero = int(input(f"Ingresa el numero {i+1}: "))
        vector[i] = numero
