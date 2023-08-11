print('Digite uma frase:')
frase = input()
palavras = frase.split()

for i in palavras:
    vogal = 0
    
    for x in i:
        if x == 'A' or x == 'a' or x == 'E' or x == 'e' or x == 'I' or x == 'i' or x == 'O' or x == 'o' or x == 'U' or x == 'u':
            vogal += 1

    print((i + ' ') * vogal, end='')