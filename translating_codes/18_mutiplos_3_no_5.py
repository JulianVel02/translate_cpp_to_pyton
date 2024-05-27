i = 1
multiplos_tres = 0

print("** Programa para encontrar los M primeros múltiplos de 3 que no lo sean de 5 **")
m = int(input("Ingrese la cantidad de números a evaluar: "))

while multiplos_tres < m:
    if i % 3 == 0 and i % 5 != 0:
        print(f"-> {i}")
        multiplos_tres += 1
    i += 1
