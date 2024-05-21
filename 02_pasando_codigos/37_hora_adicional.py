from shared_libraries.funciones_generales import leer_enteros, sumar_tiempo
hora_inicial = leer_enteros("Ingrese la hora inicial (HHMMSS): ")
tiempo_adicional = leer_enteros(
    "Ingrese el tiempo a sumar (adicional - HHMMSS): ")

tiempo_sumado = sumar_tiempo(hora_inicial, tiempo_adicional)
print(f"La nueva hora es: {tiempo_sumado} \n")
