def get_product(**datos):
    # Accedo al nombre del parametro utilizando []
    print(datos["id"], datos["name"], datos["desc"])


# Le indico a py que cada vez que llamo a una función que esté utilizando un
# keyword-args tengo que indicarle si o si el NOMBRE del PARAMETRO
# Salida: {'id': 'id', 'name': 'iPhone', 'desc': 'Esto es un iPhone'} -> diccionario
get_product(id="23", name="iPhone", desc="Esto es un iPhone")
