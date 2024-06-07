"""Calcular el maximo de un array"""
from modulos_arreglos.funciones_arrays import leer_enteros, cargar_vector, calcular_maximo, encontrar_posiciones
n = leer_enteros("Ingrese el tamaño del array: ")
arr = cargar_vector(n)

maximo = calcular_maximo(arr)
print(f"El maximo es: {maximo} \n")

posiciones = encontrar_posiciones(arr, maximo)
for posicion in posiciones:
    print(f"El maximo se encuentra en la posicion: {posicion} \n")
