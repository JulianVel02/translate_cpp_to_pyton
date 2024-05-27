sumatoria = 0

print("Los primeros 100 numeros naturales son: \n")
for i in range(1, 101):  # genera numeros de 1 a 100
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} FizzBuzz")
    elif i % 3 == 0:
        print(f"{i} Fizz.")
    elif i % 5 == 0:
        print(f"{i} Buzz.")
    else:
        print(i)
    sumatoria += i  # suma valores de 1 a 100

print(f"La sumatoria de los primeros 100 numeros naturales es: {sumatoria}!")
