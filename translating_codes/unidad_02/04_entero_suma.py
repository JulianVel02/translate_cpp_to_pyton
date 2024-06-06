"""Suna de los componentes de un arr[N]"""
from modulos_arreglos.funciones_arrays import *
N = leer_enteros("Ingrese el tamaño N (< 25): ")
arr = cargar_vector(N)

suma = 0
for i in range(N):
    suma += arr[i]
if suma > 0:
    print("\nLa suma de los componentes es mayor que CERO ->")
    for i in range(1, N, 2):
        print(f"El indice: {i}, es IMPAR y contiene el número: {arr[i]}")
else:
    print("La suma de los componentes es menor/igual a CERO ->")
    for i in range(0, N, 2):
        print(f"El indice: {i}, es PAR y contiene el número: {arr[i]}")
