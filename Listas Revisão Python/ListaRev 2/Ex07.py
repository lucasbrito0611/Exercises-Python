print('Digite uma frase:')
frase = input()

palavras = frase.split()

for i in range(len(palavras)):
    print(" ".join(palavras[i:]))