def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


num = int(input("Ingresa un numero:"))
print(f"El factorial de {num} es {factorial(num)}")
