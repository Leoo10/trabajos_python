# def es_palindromo(texto):


# print('Reconocer', es_palindromo('Abba'))

def no_space(texto):
    nuevo_texto = ''
    for char in texto:
        if char != ' ':
            nuevo_texto += char
    return nuevo_texto


def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    print(texto_al_reves)


es_palindromo('amo la paloma')
