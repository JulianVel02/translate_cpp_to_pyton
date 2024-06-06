"""11 - DICCIONARIOS
    Los diccionrios son una conexion de datos que se encuentran agrupados por:
        - LLAVE - VALOR -
        nombre = "Hola mundo"
        edad = 22
"""

punto = {"x": 25,
         "y": 50}

print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
# print(punto, punto["lala"])
if "lala" in punto:
    print("Encontre lala!", punto["lala"])

print(punto.get("x"))
print(punto.get("lala", 97))
del punto["x"]
del (punto["y"])

print(punto)
punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

for val in punto.items():
    print(val)

for llave, val in punto.items():
    print(llave, val)

usuarios = [
    {"id": 1, "nombre": "Chanchito"},  # Identificador unico
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Julian"},
    {"id": 4, "nombre": "Aby"}
]

for user in usuarios:
    print(user["nombre"])
