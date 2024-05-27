saludo = 25  # ! Variables globales = MALA PRACTICA


def saludar():
    global saludo  # ! PESIMA PRACTICA
    saludo = "Hola mundo!"


def saludaChanchito():
    saludo = 24
    print(saludo)


resultado1 = saludo + 3
print(resultado1)
saludar()
resultado2 = saludo + 3
print(resultado2)
