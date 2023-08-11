print('Digite uma frase:')
frase = input()
lista = []
for i in range(len(frase)):
    if frase[i].isdigit():
        lista.append(frase[i])

lista_inteiros = [int(x) for x in lista]

print(sum(lista_inteiros))