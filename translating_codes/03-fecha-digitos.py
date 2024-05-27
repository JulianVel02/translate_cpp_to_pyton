# Dada un número entero de la forma (AAAAMMDD), que representa una fecha valida
# mostrar el dia, mes y año que representa.
fecha = int(input("Ingrese la fecha en formato AAAAMMDD: "))
dia = fecha % 100  # Obtengo el ultimo par de digitos que representan el dia
fecha //= 100  # Elimina los ultimos dos digitos para obtener AAAAMM
mes = fecha % 100  # Obtengo el siguiente par de digitos que representan el mes
anio = fecha // 100  # Obtengo los primeros 4 digitos que representan el anio

print(f"La fecha ingresada es: {dia}/{mes}/{anio} \n")
