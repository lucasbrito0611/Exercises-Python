def referencia(nome):
    nomes = nome.split()
    resultado = []

    ultimo = nomes[-1]
    resultado.append(ultimo)

    for x in nomes[:-1]:
        resultado.append(x[0] + '.')

    resultado[0] += ','

    return ' '.join(resultado)

print(referencia(input()))
