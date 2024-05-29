from modulos_arreglos.funciones_arrays import cargar_vector
n = 5
vector = []
cargar_vector(n, vector)

print("------------------------")
for i in range(n):
    print(vector[i])
