from shared_libraries.funciones_generales import leer_enteros, producto_por_suma
n = leer_enteros("Ingrese N: ")
m = leer_enteros("Ingrese M: ")
resultado = producto_por_suma(n, m)
print(f"El producto de {n} y {m} es: {resultado}")
