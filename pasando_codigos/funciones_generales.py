#
#       ███╗░░░███╗░█████╗░██████╗░██╗░░░██╗██╗░░░░░░█████╗░░██████╗
#       ████╗░████║██╔══██╗██╔══██╗██║░░░██║██║░░░░░██╔══██╗██╔════╝
#       ██╔████╔██║██║░░██║██║░░██║██║░░░██║██║░░░░░██║░░██║╚█████╗░
#       ██║╚██╔╝██║██║░░██║██║░░██║██║░░░██║██║░░░░░██║░░██║░╚═══██╗
#       ██║░╚═╝░██║╚█████╔╝██████╔╝╚██████╔╝███████╗╚█████╔╝██████╔╝
#       ╚═╝░░░░░╚═╝░╚════╝░╚═════╝░░╚═════╝░╚══════╝░╚════╝░╚═════╝░

#      Acá voy a depositar la mayoría de procedimientos
#      para cada uno de los ejercicios de manera ascendente
#      , por el momento lo voy a utilizar de propósito general,
#      luego lo actualizaré meidiante vaya progresando en el proyecto.

"""
Este módulo contiene una colección de funciones generales utilizadas para diversos
ejercicios de programación. Las funciones incluyen operaciones matemáticas básicas,
como calcular cuadrados, productos por sumas sucesivas, factoriales, y también
incluyen funciones para leer entradas del usuario y realizar cálculos específicos
para ciertos problemas de programación.

Funciones incluidas:
- saludar: Saluda a la persona con el nombre dado.
- leer_enteros: Lee un entero desde la entrada estándar.
- calcular_cuadrado: Calcula el cuadrado de un número.
- producto_por_suma: Calcula el producto de dos números utilizando sumas sucesivas.
- factorial: Calcula el factorial de un número.
- calcular_partes: Calcula la quinta y séptima parte de un número y el resto de la división por 5.
- contador_mayores: Cuenta y suma números mayores y menores que ciertos umbrales.
"""


def saludar(nombre):
    """Saluda a la persona con el nombre dado."""
    print(f"Hola, {nombre}!")


def leer_enteros(msj):
    """Lee un entero desde la entrada estándar.

    Args:
        msj (str): El mensaje que se mostrará al usuario.

    Returns:
        int: El entero ingresado por el usuario.
    """
    return int(input(msj))


def calcular_cuadrado(num):
    """Calcula el cuadrado de un número.

    Args:
        num (int): El número a calcular el cuadrado.

    Returns:
        int: El cuadrado del número.
    """
    return num * num


def producto_por_suma(n, m):
    """Calcula el producto de dos números utilizando sumas sucesivas.

    Args:
        n (int): El primer número.
        m (int): El segundo número.

    Returns:
        int: El producto de los dos números.
    """
    producto = 0
    for _ in range(m):  # Acá uso _ ya que no necesito el valor de i
        producto += n
    return producto


def factorial(n):
    """Calcula el factorial de un número.

    Args:
        n (int): El número para calcular el factorial.

    Returns:
        int: El factorial del número.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def calcular_partes(num):
    """Calcula la quinta y séptima parte de un número y el resto de la división por 5.

    Args:
        num (int): El número a calcular las partes.

    Returns:
        tuple: Quinta parte, resto de la división por 5 y séptima parte del número.
    """
    quinta_parte = num / 5
    septima_parte = quinta_parte / 7
    resto = num % 5
    return quinta_parte, resto, septima_parte


def contador_mayores(rango, mayores, menores):
    """Cuenta y suma números mayores y menores que ciertos umbrales.

    Args:
        rango (int): El número de entradas a procesar.
        mayores (int): El umbral superior para contar y sumar.
        menores (int): El umbral inferior para contar y sumar.

    Returns:
        tuple: Suma de los números menores que el umbral 'menores' y 
        promedio de los números mayores que el umbral 'mayores'.
    """
    contador = 0
    suma_mayores = 0
    suma_menores = 0
    promedio_mayores = 0

    for i in range(rango):
        # Utilizo la variable "i" de esta forma para no dejarla sin uso
        numero = leer_enteros(f"Ingrese un número ({i+1}/{rango}): ")
        if numero > mayores:
            contador += 1
            suma_mayores += numero
        elif numero < menores:
            suma_menores += numero

    if contador > 0:
        promedio_mayores = suma_mayores / contador
        print(f"Promedio de mayores que {mayores}: {promedio_mayores}")
    print(f"Suma de menores que {menores}: {suma_menores}")
    return suma_menores, promedio_mayores