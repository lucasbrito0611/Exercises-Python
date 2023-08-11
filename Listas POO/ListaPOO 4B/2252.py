caso = 1

while True:
    try:    
        n = int(input())
        v = list(map(float, input().split()))
        
        loop = 0
        senha = []
        
        while loop < n:
            maior = v.index(max(v))
            senha.insert(0, maior)
            v[maior] = 0
            loop += 1
        
        senha.reverse()

        print(f'Caso {caso}:', ''.join(map(str, senha)))

        caso += 1
    except EOFError:
        break