dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

# concatenar los datos en un solo numero de 8 digitos (AAAAMMDD)
fecha = anio * 10000 + mes * 100 + dia

print(f"\nLa fecha es: {fecha}")
