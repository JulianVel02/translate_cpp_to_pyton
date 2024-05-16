# Pido al usuario la altura del patron y lo convierto a un entero
altura = int(input("Ingrese la altura del patron:"))

# Bucle externo para cada nivel del patron
for i in range(1, altura+1):
    for j in range(i):
        print("* ", end="")
    print()  # ingresa una nueva linea despues de cada nivel
