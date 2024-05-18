def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    texto_invertido = ""
    for char in texto:
        texto_invertido = char + texto_invertido
    return texto_invertido


def es_palindromo(texto):
    texto = no_space(texto)
    texto_invertivo = reverse(texto)
    return texto.lower() == texto_invertivo.lower()


print(es_palindromo("Amo la paloma"))
print(es_palindromo("Hola mundo"))
print(es_palindromo("Reconocer"))
print(es_palindromo("Somos o no somos"))
