"""12 - OPERADOR DE DESEMPAQUETADO"""
# lista1 = [1, 2, 3, 4]
# # print(1, 2, 3, 4)
# # print(*lista)

# lista2 = [5, 6]

# combinada = ["Hola", *lista1, "Mundo", *lista2, "Chanchito"]
# print(combinada)

punto1 = {"x": 19, "y": "Hola"}
punto2 = {"y": 15}

#              Desempaquetamiento
nuevo_punto = {**punto1, "lala": "Hola mundo", **punto2, "z": "Mundo"}
print(nuevo_punto)
