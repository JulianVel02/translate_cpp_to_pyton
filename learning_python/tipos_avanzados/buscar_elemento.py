"""05 - BUSQUEDA DE ELEMENTOS EN UN ARREGLO"""
mascotas = ["Dori", "Mao", "Poncho", "Wanda", "Poncho", "Fiona", "Chanchito"]

print(mascotas.count("Poncho"))
if "Poncho" in mascotas:
    print(mascotas.index("Poncho"))
