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


def read_int(prompt):
    """
    Función para leer un número entero desde la entrada estándar.
    :param prompt: Mensaje que se mostrará al usuario.
    :return: Número entero ingresado por el usuario.
    """
    return int(input(prompt))


def esPar(num):
    return num % 2 == 0


def factorial(n):
    """Calcular el factorial de N"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def cargar_vector(N):
    """Función para cargar un vector con N elementos."""
    vector = []
    # Bucle para solicitar N números enteros al usuario
    for i in range(N):
        numero = leer_enteros(f"Ingresa el numero {i + 1}: ")
        vector.append(numero)  # Añade cada número ingresado al vector
    return vector
