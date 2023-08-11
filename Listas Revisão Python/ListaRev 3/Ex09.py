def Vogais(texto):
    vogais = []
    for i in texto:
        if i == 'a' or 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U':
            vogais.append(i)

    for x in vogais:
       return x

print(Vogais(input))