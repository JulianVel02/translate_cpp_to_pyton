"""07 - ORDENANDO LISTAS - LAMBDAS"""
numeros = [2, 4, 1, 45, 75, 22, 99, 23, -8, 5, 52]

# numeros.sort(reverse=True)
# numeros.sort()

# La diferencia de sorted ante sort, es que crea una lista NUEVA, no afecta a la original
numeros2 = sorted(numeros)  # Devuelve una nueva lista
numeros2 = sorted(numeros, reverse=True)

print(numeros)
print(numeros2)

usuarios = [
    ["Dori", 4],
    ["Mao", 1],
    ["Wanda", 5]
]


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=lambda el: el[1])
print(usuarios)  # ^---- Accede al segundo elemento de la lista,
#                        ej: ["Dori", 4], accede a 4 para comenzar
#                        a ordenar la lista entera.
