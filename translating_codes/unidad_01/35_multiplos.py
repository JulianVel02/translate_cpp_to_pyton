from modulos_generales.funciones_generales import leer_enteros, Contadores, factorial_largo
contadores = Contadores()

n = leer_enteros("Ingrese la cantidad de números a analizar: ")
NUM = None

print("Chanchito")
for _ in range(n):
    NUM = leer_enteros("Ingrese un número: ")
    print(f"Su factorial es: {factorial_largo(NUM)}\n")
    contadores.multiplo_de_3(NUM)
    contadores.multiplo_de_5(NUM)
    contadores.multiplo_3_y_5(NUM)

print(f"Cantidad de múltiplos de 3: {contadores.cant_mult_3}")
print(f"Cantidad de múltiplos de 5: {contadores.cant_mult_5}")
print(f"Cantidad de múltiplos de 3 y 5: {contadores.cant_mult_doble}")
