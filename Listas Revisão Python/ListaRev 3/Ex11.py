def Senha(texto):
    palavras = texto.split()
    senha = ''
    for i in palavras:
        senha += str(len(i))

    return senha

print(Senha(input()))