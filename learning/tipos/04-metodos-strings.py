animal = "  chanCHito feliz"
print(animal.upper())
print(animal.lower())

# primera letra en mayuscula, el resto en minuscula
print(animal.capitalize())
print(animal.strip().capitalize())  # se puede encadenar metodos

# toma la primera letra de cada palabra del string y la pone en mayuscula
print(animal.title())

# remueve los espacios en blanco al principio del string
print(animal.strip())
print(animal.lstrip())  # saca espacios de la izquierda
print(animal.rstrip())  # saca espacios de la derecha

# busca los indices
print(animal.find("CH"))  # devuelve el indice donde se encuentra el string dado
print(animal.find("cH"))  # entrega -1 ya que no encuentra lo que se le indica

# devuelve el booleano si es que encuentra o no el string dado
print("nCH" in animal)
print("nCH" not in animal)  # busca si NO se encuentra dentro del string

# reemplaza lo que se le indique
print(animal.replace("nCH", "j"))
