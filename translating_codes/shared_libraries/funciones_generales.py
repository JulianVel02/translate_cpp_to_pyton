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
    while True:
        try:
            return int(input(msj))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")


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

# contadores.py


class Contadores:
    def __init__(self):
        self.cant_mult_3 = 0
        self.cant_mult_5 = 0
        self.cant_mult_doble = 0

    def multiplo_de_3(self, n):
        if n % 3 == 0:
            self.cant_mult_3 += 1

    def multiplo_de_5(self, n):
        if n % 5 == 0:
            self.cant_mult_5 += 1

    def multiplo_3_y_5(self, n):
        if n % 3 == 0 and n % 5 == 0:
            self.cant_mult_doble += 1


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


def factorial_largo(n):
    """Calcular el facotrial de un numero"""
    result = 1
    if n < 0:
        print("Factorial no definido para los negativos.")
        return False
    for i in range(1, n+1):
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


def identificar_mayor_menor(n, mensaje):
    """Validación del número mayor y menor de una lista de números ingresados por el usuario.

    Args:
        n (int): La cantidad de números a ingresar.
        mensaje (str): El mensaje a mostrar al pedir cada número.

    Returns:
        tuple: El valor mayor y menor de la lista de números ingresados.
    """
    valor = int(input(mensaje))
    mayor = menor = valor
    for _ in range(n-1):
        if valor > mayor:
            mayor = valor
        if valor < menor:
            menor = valor
    return mayor, menor

    #       Ejemplo de uso de identificar_mayor_menor()     #

# n = leer_enteros("Ingrese la cantidad de valores a analizar: ")
# mensaje = "Ingrese un numero: "
# mayor, menor = identificar_mayor_menor(n, mensaje)
# print(f"-> El numero menor es: {menor}")
# print(f"-> El numero mayor es: {mayor}")


def calcular_mcd(a, b):
    """Calcular el maximo comun divisor(MCD)"""
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def sumar_tiempo(hora_inicial, tiempo_adicional):
    segundos_totales = (hora_inicial % 100 + tiempo_adicional % 100) % 60
    minutos_totales = ((hora_inicial % 10000 // 100 + tiempo_adicional % 10000 // 100) +
                       (hora_inicial % 100 + tiempo_adicional % 100) // 60) % 60
    horas_totales = ((hora_inicial // 10000 + tiempo_adicional // 10000) +
                     (hora_inicial % 10000 // 100 + tiempo_adicional % 10000 // 100 +
                      (hora_inicial % 100 + tiempo_adicional % 100) // 60) // 60) % 24

    nueva_hora = int(horas_totales * 10000 +
                     minutos_totales * 100 + segundos_totales)
    return nueva_hora
