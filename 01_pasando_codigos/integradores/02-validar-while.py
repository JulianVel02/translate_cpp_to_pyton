num = 0
numero_valido = False

while not numero_valido:
    num = int(input("Ingrese un numero entre 0 y 9: "))
    if 0 <= num <= 9:
        print(f"Numero valido: {num} \n")
        numero_valido = True
    else:
        print("Numero no valido. Intente de nuevo!! \n")
