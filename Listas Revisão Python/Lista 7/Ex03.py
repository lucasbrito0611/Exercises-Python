def iniciais(nome):
    palavras = nome.split()
    resultado = ''
    for palavra in palavras:
        resultado += palavra[0]

    return resultado

print(iniciais(input()))