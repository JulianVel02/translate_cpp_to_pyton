"""Carga y muestreo del vector"""
# * Similar a c++
N = 5
vector = [None] * N

for i in range(N):
    numero = int(input(f"Ingresa el numero {i+1}: "))
    vector[i] = numero
print("---------------------- \n")
for i in range(N):
    print(vector[i])

# ? Propio de python

# * Crear vector vacio
vector_1 = []
vector_1.append(1)
vector_1.append(2)
vector_1.append(3)
print(f"\nPara el vector 1: {vector_1}")  # Output: [1,2,3]

# * Vector predefinido
vector_2 = [1, 2, 3, 4, 5]
# Crea un vector con valores del 1 al 5
print(f"\nPara el vector 2: {vector_2}")

# * Utilizando comprension de listas
# Crea un vector con valores del 1 al 5
vector_3 = [i for i in range(1, 6)]
print(f"\nPara el vector 3: {vector_3}")

# * Crea un vector con la funcion range()
# Crea un vector con valores del 1 al 5
vector_4 = list(range(1, 6))
print(f"\nPara el vector 4: {vector_4}")
