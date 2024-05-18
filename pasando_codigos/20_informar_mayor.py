valor = 0
valor_mayor = 0
for i in range(10):
    valor = int(input("Ingrese un valor: "))
    if valor > valor_mayor:
        valor_mayor = valor

print(f"Dados 10 numeros, el mayor de todos es: {valor_mayor}")
