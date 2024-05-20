from shared_libraries.funciones_generales import leer_enteros
num = 0
num_ingresados = 0

while num >= 0:
    num = leer_enteros("Ingrese un número: ")
    if num >= 0:
        num_ingresados += 1

print(f"Numero de valores ingresados: {num_ingresados}. \n")
