class Disciplina:
    def __init__(self):
        self.nome = ''
        self.nota1 = 0
        self.nota2 = 0
        self.nota3 = 0
        self.nota4 = 0
        self.notafinal = 0
       
    def calculo(self):
        media = ((self.nota1 * 2) +  (self.nota1 * 2) + (self.nota1 * 3) + (self.nota1 * 3)) / 10
        return media
    def calculofinal(self):
        mediafinal = ((((self.nota1 * 2) +  (self.nota1 * 2) + (self.nota1 * 3) + (self.nota1 * 3)) / 10) + self.notafinal) / 2
        return mediafinal

x = Disciplina()
x.nome = input('Digite o nome da disciplina: ')
x.nota1 = int(input())
x.nota2 = int(input())
x.nota3 = int(input())
x.nota4 = int(input())

print(x.calculo())
if x.calculo() < 60:
    x.notafinal = int(input())
    print(x.calculofinal())