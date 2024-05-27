# Dados dos valores enteros y distintos,
# emitir una leyenda apropiada que informe
# cuál es el mayor entre ellos.
print("Ingrese dos numeros enteros y distintos para informarle cual es el mayor entre ellos.")
a = int(input("Numero A: "))
b = int(input("Numero B: "))

if a > b:
    print("A es mayor que B. \n")
elif b > a:
    print("B es mayor que A. \n")
else:
    print("Los numeros son iguales. \n")
