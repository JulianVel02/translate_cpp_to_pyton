from modulos_arreglos.funciones_arrays import leer_enteros, cargar_vector
n = leer_enteros("Ingrese el tamaño del arreglo (<40): ")
arr1 = cargar_vector(n)
arr2 = cargar_vector(n)
arr3 = [0] * n

for i in range(n):
    arr3[i] = arr1[i] + arr2[n-1-i]
print("-- Vector resultante --")
for i in range(n):
    print(f"C[{i}] = {arr3[i]}")
