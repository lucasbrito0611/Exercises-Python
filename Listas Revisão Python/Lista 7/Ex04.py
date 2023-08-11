def aprovado(nota1, nota2):
    media = (nota1 + nota2) / 2

    if media >= 60:
        return True
    else:
        return False

print(aprovado(int(input()), int(input())))