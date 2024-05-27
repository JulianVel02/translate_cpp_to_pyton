# and - or - not

gas = False
encendido = True
edad = 18

# if gas and encendido and edad > 17:
#     print("Podes avanzar")

# if gas and (encendido or edad > 17):
#     print("Podes avanzar")

# if not gas and (encendido or edad > 17):
#     print("Podes avanzar")

# operador de corto circuito
if not gas or encendido or edad > 17:
    print("Podes avanzar")
