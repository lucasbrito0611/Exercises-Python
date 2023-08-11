print('Digite uma frase:')
frase = input()
palavras = frase.split()

for i in range(len(palavras)):
    inverter = ''.join(reversed(palavras[i]))
    print(inverter)