"""09 - TUPLAS 
        Es lo mismo que las listas pero,
        NO SON MODIFICABLES, no se le puede:
        -Agregar elementos.
        -Eliminar elementos.
        -Modificar.
    Las tuplas las vamos a usar cuando NO QUERAMOS DE MANERA ACCIDENTAL MODIFICAR
    LOS ELEMENTOS DENTRO DEL LISTADO.
"""

numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)
punto = tuple([1, 2])
print(punto)


menos_numeros = numeros[:2]  # Esta accion no modifica la tupla
print(menos_numeros)
pri, seg, *otros = numeros
print(pri, seg, otros)
for n in numeros:
    print(n)

lista_numeros = list(numeros)  # Creo una lista EN BASE a la tupla
#                                pero, NO MODIFICO LA TUPLA
lista_numeros[0] = "Chanchito"
print(lista_numeros)
