def suma_multiples_argumentos(*numeros):  # parametros -> iterables (con el *)
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


# iterables -> for
suma_multiples_argumentos(2, 5, 7)
suma_multiples_argumentos(2, 5)
suma_multiples_argumentos(2, 8, 7, 45, 32)
