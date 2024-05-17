#
#       ███╗░░░███╗░█████╗░██████╗░██╗░░░██╗██╗░░░░░░█████╗░░██████╗
#       ████╗░████║██╔══██╗██╔══██╗██║░░░██║██║░░░░░██╔══██╗██╔════╝
#       ██╔████╔██║██║░░██║██║░░██║██║░░░██║██║░░░░░██║░░██║╚█████╗░
#       ██║╚██╔╝██║██║░░██║██║░░██║██║░░░██║██║░░░░░██║░░██║░╚═══██╗
#       ██║░╚═╝░██║╚█████╔╝██████╔╝╚██████╔╝███████╗╚█████╔╝██████╔╝
#       ╚═╝░░░░░╚═╝░╚════╝░╚═════╝░░╚═════╝░╚══════╝░╚════╝░╚═════╝░

#       Aquí voy a depositar la mayoría de procedimientos
#      para cada uno de los ejercicios de manera ascendente
#      , por el momento lo voy a utilizar de propósito general,
#      luego lo actualizaré meidiante vaya progresando en el proyecto.


def saludar(nombre):
    print(f"Hola, {nombre}!")


def leerEnteros(msj):
    n = int(input(msj))
    return n


def calcularCuadrado(num):
    return num * num


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Ejercicio 04 / Calcular Partes (quinta y septima)


def calcularPartes(num):
    quintaParte = num / 5
    septimaParte = quintaParte / 7
    resto = num % 5
    return quintaParte, resto, septimaParte
