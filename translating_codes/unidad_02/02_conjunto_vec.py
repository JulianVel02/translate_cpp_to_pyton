"""Ejercicio 2"""
from modulos_arreglos.funciones_arrays import leer_enteros, cargar_vector

N = leer_enteros("Ingrese un valor entero para el tamaño (< 30): ")
# Cargar el vector con N elementos ingresados
arr = cargar_vector(N)

# Verifico si el ultimo elemento del vector es menor a 10
if arr[-1] < 10:
    print("\nLos valores negativos son: ")
    for i in arr:
        if i < 0:
            print(i)  # Imprimo los valores negativos
else:
    print("Todos los elemenos menos el ultimo: ")
    # Imprimo los elementos excepto el ultimo
    for i in arr[:-1]:
        print(i)
