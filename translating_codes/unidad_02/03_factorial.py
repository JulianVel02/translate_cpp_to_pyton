"""Calcular factorial en un array"""
from modulos_arreglos.funciones_arrays import read_int, factorial
N = read_int("Ingrese el tamaño del array: ")
arr = []
arr_fact = []

for i in range(N):
    numero = read_int(f"Ingrese el numero {i+1}: ")
    arr.append(numero)

for num in arr:
    arr_fact.append(factorial(num))

for i in range(N):
    print(f"El factorial de !{arr[i]}, es: {arr_fact[i]}")
