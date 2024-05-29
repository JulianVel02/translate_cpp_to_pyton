fecha1 = int(input("Ingrese la primera fecha (AAAAMMDD): "))
fecha2 = int(input("Ingrese la segunda fecha (AAAAMMDD): "))
if fecha1 > fecha2:
    print("La fecha 1 es mas reciente que la fecha 2. \n")
elif fecha2 > fecha1:
    print("La fecha 2 es mas reciente que la fecha 1. \n")
else:
    print("Las fechas son iguales. \n")
