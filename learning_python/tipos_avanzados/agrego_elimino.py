"""06- AGREGANDO Y ELIMINANDO"""
mascotas = ["Dori",             # index: 0
            "Mao",              # index: 1
            "Wanda",            # index: 2
            "Fiona",            # index: 3
            "Wanda",            # index: 4
            "Chanchito feliz"   # index: 5
            ]
mascotas.insert(1, "Melvin")
mascotas.append("Chanchito triste")

mascotas.remove("Wanda")  # se le pasa el ELEMENTO
mascotas.pop(1)  # saca a Melvin, ya que le paso el indice
del mascotas[0]
# mascotas.clear()

print(mascotas)
