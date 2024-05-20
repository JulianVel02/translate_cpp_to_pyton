CANT_CONTENEDORES = 3
# peso no tiene ningun valor inicial
puerto_arribo, puerto_1, puerto_2, puerto_3, peso, acum, mayor_peso = 0, 0, 0, 0, None, 0, 0
id_cont = id_mayor = ""


for i in range(CANT_CONTENEDORES):
    id_cont = str(input("Ingrese identificación del contenedor: "))
    peso = float(input("Ingrese el peso del contenedor: "))
    puerto_arribo = int(input("Ingrese al puerto de arribo (1, 2 o 3): "))
    acum += peso
    if peso > mayor_peso:
        mayor_peso = peso
        id_mayor = id_cont
    if puerto_arribo == 1:
        puerto_1 += 1
    elif puerto_arribo == 2:
        puerto_2 += 1
    else:
        puerto_3 += 1

print(f"\nLa canitdad del peso del buque es: {acum}\n")
print(f"La identificación del contenedor con más peso es: {id_mayor}\n")
print(f"Cantidad de contenedores al puerto 1: {puerto_1}\n")
print(f"Cantidad de contenedores al puerto 2: {puerto_2}\n")
print(f"Cantidad de contenedores al puerto 3: {puerto_3}\n")
