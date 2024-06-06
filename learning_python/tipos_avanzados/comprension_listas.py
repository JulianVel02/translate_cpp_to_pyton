"""08 - COMPRENSION DE LISTAS"""
usuarios = [
    ["Dori", 4],
    ["Mao", 1],
    ["Wanda", 5]
]  # Queremos transformar la lista para que
#   nos devuelva una lista de NOMBRES

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# MAP -> Transformar
# nombres = [user[0] for user in usuarios]
#               ^--- Accedo al primer elemento de la lista

# Filter -> Filtrar
# nombres = [user for user in usuarios if user[1] > 2]

#          Filtrar y Transformar
# nombres = [user[0] for user in usuarios if user[1] > 2]


# nombres = list(map(lambda usuario: usuario[0], usuarios))
menos_usuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menos_usuarios)
