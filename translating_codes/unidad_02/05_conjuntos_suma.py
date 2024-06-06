"""Suma de 2 arrays"""
from modulos_arreglos.funciones_arrays import *
n = leer_enteros("Ingrese el tamaño para los arrays UNO y DOS (< 30): ")

print("Carga del arr UNO: ")
arr_uno = cargar_vector(n)

print("Carga del arr DOS: ")
arr_dos = cargar_vector(n)

arr_tres = [0] * n

for i in range(n):
    if esPar(i):
        arr_tres[i] = arr_uno[i]
    else:
        arr_tres[i] = arr_dos[i]

print("\nVector resultante ->")
for i in range(n):
    print(f"TRES[{i}] -> {arr_tres[i]}")
