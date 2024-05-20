# num = 1
# while num < 100:
#     print(num)
#     num *= 2

comando = ""

# while comando.lower() != "salir":
#     comando = input("$ ")
#     print(comando)

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break  # condicion de corte
