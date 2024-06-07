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


def cargar_set(n):
    numeros = set()  # Inicializo un set vacio
    for i in range(n):
        numero = leer_enteros(f"Ingrese el numero {i+1}: ")
        numeros.add(numero)  # Agrego numeros al set
    return numeros


def cargar_vector(N):
    """Función para cargar un vector con N elementos."""
    vector = []
    # Bucle para solicitar N números enteros al usuario
    for i in range(N):
        numero = leer_enteros(f"Ingresa el numero {i + 1}: ")
        vector.append(numero)  # Añade cada número ingresado al vector
    return vector


def calcular_maximo(arr):
    """Calcular valor maximo de un array"""
    maximo = arr[0]
    for valor in arr:
        if valor > maximo:
            maximo = valor
    return maximo


def encontrar_posiciones(arr, valor):
    """Encontrar todas las posiciones del arreglo"""
    posiciones = []
    for index, element in enumerate(arr):
        if element == valor:
            posiciones.append(index)
    return posiciones


def muestreo_multiple_inverso(n, arr):
    """Funcion para Mostrar una lista inversa de diferentes maneras"""
    option = input(
        "Ingrese la opción de visualización (uno, cinco, diez): ").lower()
    arr_inv = arr[::-1]
    if option == "uno":
        print("\n -> Uno por línea: \n")
        for i in arr_inv:
            print(i)
    elif option == "cinco":
        print("\n -> Cinco por linea e identificación: \n")
        for i in range(n):
            print(f"VEC[{n-1-i}] = {arr_inv[i]}   -   ", end="")
            if (i+1) % 5 == 0:
                print()
    elif option == "diez":
        print("\n -> Diez por linea: \n")
        for i in range(n):
            print(f"{arr_inv[i]}, ")
            if (i+1) % 10 == 0:
                print()
    else:
        print("Opcion no valida...")


def anexar_arrays(arr_uno, arr_dos):
    """
    Anexa dos arreglos.
    """
    return arr_uno + arr_dos


def anexo_sin_cero(arr1, arr2):
    """
    Anexa dos arreglos, omitiendo ceros.
    """
    return [elemento for elemento in arr1
            if elemento != 0] + [elemento for elemento in arr2
                                 if elemento != 0]
