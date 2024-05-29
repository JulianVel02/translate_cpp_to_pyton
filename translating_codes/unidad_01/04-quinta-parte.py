from libraries.funciones_generales import calcular_partes, leer_enteros
if __name__ == "__main__":
    num = leer_enteros("Ingrese un número entero: ")
    quintaParte, resto, septimaParte = calcular_partes(num)

    print("<-Resultados->")
    print(f"La quinta parte es: {quintaParte}")
    print(f"El resto de la división por 5 es: {resto}")
    print(f"La séptima parte de la quinta parte es: {septimaParte}")
