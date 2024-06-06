"""Manipulando listas"""
mascotas = ["Wolfgang", "Copito", "Pulga", "Chanchito"]
print(mascotas[0])

mascotas[0] = "Bicho"
# print(mascotas)
# print(mascotas[:3])  # es igual a [0:3]
# print(mascotas[2:])  # toma todos los elementos para la derecha
# print(mascotas[-1])
# print(mascotas[::2])  # saltea de a 2
# print(mascotas[1::2])  # saltea de a 2 desde el indice 1
# print(mascotas[1:2:2])

numeros = list(range(21))
print(numeros[::2])  # numeros pares
print(numeros[1::2])  # numeros impares
