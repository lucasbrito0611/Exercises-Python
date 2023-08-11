print('Digite uma frase:')
frase = input()
palavras = frase.split()

for i in palavras:
    print(len(i), end='')