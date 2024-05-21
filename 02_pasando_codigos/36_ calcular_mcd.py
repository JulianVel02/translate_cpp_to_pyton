from shared_libraries.funciones_generales import calcular_mcd, leer_enteros
numerador = leer_enteros("Ingrese numerador: ")
denominador = leer_enteros("Ingrese denominador (NO PUEDE SER 0): ")

mcd = calcular_mcd(numerador, denominador)
fraccion_simplificada = f"{numerador//mcd}/{denominador//mcd}"
print(f"La fraccion simplificada es: {fraccion_simplificada}\n")
