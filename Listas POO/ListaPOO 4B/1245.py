while True:
    try:
        entrada = int(input())
        esquerdo = []
        direito = []
        pares = 0
        for i in range(entrada):
            numero, pe = input().split()
            numero = int(numero)
            
            if pe == 'D':
                direito.append(numero)
            if pe == 'E':
                esquerdo.append(numero)

        for k in direito:
            if k in esquerdo:
                pares += 1

        print(pares)
    except EOFError:
        break