# A partir de un valor entero ingresado por teclado, se pide informar:
# a) La quinta parte de dicho valor
# b) El resto de la división por 5
# c) La séptima parte del resultado del punto a)
from funcionesGenerales import calcularPartes

# Forma calcada a C++
# num = int(input("Ingrese un numero entero: "))
# quintaParte = num / 5
# septimaParte = quintaParte / 7
# resto = num % 5

# print(f"<-Resultados-> \nLa quinta parte es: {quintaParte} \nEl resto de la division por 5 es: {
#       resto} \nLa septima parte es: {septimaParte}")


# Formato con funcion
if __name__ == "__main__":
    num = int(input("Ingrese un número entero: "))
    quintaParte, resto, septimaParte = calcularPartes(num)

    print("<-Resultados->")
    print(f"La quinta parte es: {quintaParte}")
    print(f"El resto de la división por 5 es: {resto}")
    print(f"La séptima parte de la quinta parte es: {septimaParte}")
