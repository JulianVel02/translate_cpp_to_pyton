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
    if texto.lower() == texto_invertivo.lower():
        return print((f"La palabra: {texto} es palindromo! ({texto_invertivo})\n"))
    else:
        return print(f"La palabra: {texto} NO es palindromo :/ \n")


es_palindromo("Amo la paloma")
es_palindromo("Hola mundo")
es_palindromo("Reconocer")
es_palindromo("Somos o no somos")
