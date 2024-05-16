# Solicitar los valores de los lados del triángulo
a = int(input("Ingrese el valor del lado A: "))
b = int(input("Ingrese el valor del lado B: "))
c = int(input("Ingrese el valor del lado C: "))

# Verificar si los lados pueden formar un triángulo
if a != b and a != c and b != c:
    if a + b > c and a + c > b and b + c > a:
        print("Los lados ingresados forman un triángulo ▲")
    else:
        print("Los lados ingresados no forman un triángulo :(")
else:
    print("Los lados ingresados no forman un triángulo :(")
