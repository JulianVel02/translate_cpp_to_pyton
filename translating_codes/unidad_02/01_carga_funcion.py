"""Cargando un array"""
from modulos_arreglos.funciones_arrays import cargar_vector
N = 5
vector = []
cargar_vector(N, vector)

print("------------------------")
for i in range(N):
    print(vector[i])
