from funciones_generales import leer_enteros
edad = leer_enteros("Ingrese su edad: ")

if edad <= 12:
    print("Es Menor.\n")
elif 13 <= edad <= 18:
    print("Es Cadete.\n")
elif 18 < edad <= 26:
    print("Es Juvenil.\n")
else:
    print("Es Mayor.\n")
