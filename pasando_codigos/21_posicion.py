n = int(input("Ingrese la cantidad de valores a analizar: "))
valor_actual = int(input("Ingrese un numero: "))

mayor = menor = valor_actual
posicion_actual = 1
posicion_mayor = posicion_menor = posicion_actual

for i in range(1, n):
    valor_actual = int(input("Ingrese un numero: "))
    posicion_actual += 1
    if valor_actual > mayor:
        mayor = valor_actual
        posicion_mayor = posicion_actual
    if valor_actual < menor:
        menor = valor_actual
        posicion_menor = posicion_actual

print(
    f"-> El numero menor es: {menor}. \nSe encuentra en la posicion: {posicion_menor}.\n")
print(
    f"-> El numero mayor es: {mayor}. \nSe encuentra en la posicion: {posicion_mayor}.\n")
