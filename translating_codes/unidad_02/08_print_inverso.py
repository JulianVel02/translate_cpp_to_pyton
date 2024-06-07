from modulos_arreglos.funciones_arrays import muestreo_multiple_inverso, cargar_vector, leer_enteros
n = leer_enteros("Ingrese el tamaño del arreglo: ")
muestreo = cargar_vector(n)
muestreo_multiple_inverso(n, muestreo)
