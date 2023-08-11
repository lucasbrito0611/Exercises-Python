def formatar_nome(nome):
    palavras = nome.split()
    resultado = ''
    for palavra in palavras:
        maiusculas = palavra[0]
        minusculas = palavra[1:]
        maiusculas = maiusculas.upper()
        minusculas = minusculas.lower()

        resultado += maiusculas + minusculas + ' '

    return resultado

print(formatar_nome(input()))