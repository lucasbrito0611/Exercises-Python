entrada = int(input())
total = ratos = coelhos = sapos = 0

for i in range(entrada):
    quantia, tipo = input().split()
    quantia = int(quantia)
    total += quantia
    if tipo == 'C':
        coelhos += quantia
    if tipo == 'R':
        ratos += quantia
    if tipo == 'S':
        sapos += quantia
    
    porcentagemcoelhos = (100 * coelhos) / total 
    porcentagemratos = (100 * ratos) / total 
    porcentagemsapos = (100 * sapos) / total 
        
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {porcentagemcoelhos:.2f} %')
print(f'Percentual de ratos: {porcentagemratos:.2f} %')
print(f'Percentual de sapos: {porcentagemsapos:.2f} %')
    
