import funciones_generales
nro = funciones_generales.leer_enteros(
    "Ingrese el numero del que quiera saber el factorial: ")
print(f"El factorial de {nro}, es: {funciones_generales.factorial_largo(nro)}")
