"""Anexado de conjuntos"""
from modulos_arreglos.funciones_arrays import leer_enteros, cargar_vector, anexar_arrays, anexo_sin_cero
# Leer tamaños de los conjuntos
N = leer_enteros("Ingrese el tamaño del conjunto A: ")
M = leer_enteros("Ingrese el tamaño del conjunto B: ")

# Cargar los conjuntos
print("\nCarga del conjunto A ->\n")
conjunto_a = cargar_vector(N)
print("\nCarga del conjunto B ->\n")
conjunto_b = cargar_vector(M)

# Anexar conjuntos
conjunto_c = anexar_arrays(conjunto_a, conjunto_b)
print(f"Conjunto anexado entre A y B: {conjunto_c}")

# Anexar conjuntos sin ceros
conjunto_d = anexo_sin_cero(conjunto_a, conjunto_b)
print(f"Conjunto anexado sin ceros: {conjunto_d}")
