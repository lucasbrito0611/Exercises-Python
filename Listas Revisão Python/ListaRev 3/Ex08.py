def Soma(inicio,fim):
    valores = []
    for i in range(inicio, fim + 1):
        valores.append(i)
        soma = sum(valores)

    return soma

print(Soma(int(input()), int(input())))