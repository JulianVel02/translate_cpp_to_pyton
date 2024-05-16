ladoUno = int(input("Ingrese el L1: "))
ladoDos = int(input("Ingrese el L2: "))
ladoTres = int(input("Ingrese el L3: "))

if ladoUno == ladoDos and ladoUno == ladoTres:
    print("Es un Triangulo Equilatero.")
elif ladoUno == ladoDos or ladoUno == ladoTres or ladoDos == ladoTres:
    print("Es un Triangulo Isoceles.")
else:
    print("Es un Triangulo Escaleno")
