"""Ejercicio de la UNSO - CIBERCEGURIDAD"""

# Declarar lista de numeros
numeros = [1, 2, 3, 4, 5]
# Calcular la suma de los elementos de la lista
total = sum(numeros)
print(f"La suma de los elementos es: {total}")

for dia in range(1, 8):
    if dia == 1:
        print("Es Lunes")
    elif dia == 2:
        print("Es Martes")
    elif dia == 3:
        print("Es Miercoles")
    elif dia == 4:
        print("Es Jueves")
    elif dia == 5:
        print("Es Viernes")
    elif dia == 6:
        print("Es Sabado")
    else:
        print("Es Domingo")

for i in range(1, 6):
    print(f"Hola! {i}")

dia_semana = "Lunes,Martes,Miércoles,Jueves,Viernes"
print(dia_semana)

array_dias = dia_semana.split(",")
print(array_dias)

array_dias.sort(reverse=True)
print(array_dias)
