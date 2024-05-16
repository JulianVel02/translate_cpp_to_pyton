def imprimirBienvenida():
    print("Bienvenido al programa de calculo de cuadrados! \n")


def calcularCuadrado(num):
    return num * num


numero = 0
imprimirBienvenida()
while True:
    numero = int(input("Ingrese un numero entero: "))
    print(f"El cuadrado {numero} es: {calcularCuadrado(numero)}\n")
    respuesta = input("¿Desea continuar? (s/n): ")
    if respuesta.lower() == 'n':
        break

print("Gracias por usar el programa! \n")
