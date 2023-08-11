def primo(n):
    verdadeiro = 'É primo'
    falso = 'Não é primo'
    divisores = 0

    for i in range(1,n+1):
        if n % i == 0:
            divisores += 1

    if divisores > 2:
        return falso

    else:
        return verdadeiro

print(primo(int(input())))