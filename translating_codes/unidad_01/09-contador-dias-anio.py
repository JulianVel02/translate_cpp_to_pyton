mes = int(input("Ingrese el mes (formato numerico: enero=1, febrero=2, etc.): "))
anio = int(input("Ingrese el año: "))

if mes == 2:  # verificamos si se introduce 2 (para febrero)
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):  # verificamos si es bisiesto x el año
        dias = 29
    else:
        dias = 28
elif mes % 2 != 0:
    dias = 30
else:
    dias = 31

print(f"El mes ({mes}) del año ({anio}) tiene ({dias}) dias\n")
