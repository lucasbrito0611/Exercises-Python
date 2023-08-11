import datetime
import enum

class Pagamento(enum.Enum):
    EmAberto = 0
    PagoParcial = 1
    Pago = 2

class Boleto:
    def __init__(self, cod, data_emissao, data_venc, valor):
        self.__codBarras = cod
        self.__dateEmissao = data_emissao
        self.__dataVencimento = data_venc
        self.__valorBoleto = valor
        self.__valorPago = 0
        self.__situacaoPagamento = Pagamento.EmAberto

    def Pagar(self, valorPago):
        self.__valorPago += valorPago
        if self.__valorPago > self.__valorBoleto:
            self.__valorPago -= valorPago
            return 'O valor de pagamento não pode ser maior que o valor do boleto.'
        else:     
            if self.__valorPago == 0:
                return self.__situacaoPagamento
            elif self.__valorPago < self.__valorBoleto:
                self.__situacaoPagamento = Pagamento.PagoParcial
            else:
                self.__situacaoPagamento = Pagamento.Pago
            return f'Pagamento efetuado: R$ {valorPago:.2f}'
            
    def Situacao(self):
        if self.__situacaoPagamento == Pagamento.PagoParcial:
            return f'{self.__situacaoPagamento.name}: R$ {self.__valorPago:.2f}\nValor pendente: R$ {(self.__valorBoleto - self.__valorPago):.2f}'
        else:
            return self.__situacaoPagamento.name

    def __str__(self):
        return f"Código de barras: {self.__codBarras}\nData de emissão: {self.__dateEmissao.strftime('%d/%m/%Y')}\nData de vencimento: {self.__dataVencimento.strftime('%d/%m/%Y')}\nValor do boleto: R$ {self.__valorBoleto:.2f}"
    
class UI:
    def menu():
        print('1 - Gerar boleto, 2 - Pagar, 3 - Situação do pagamento, 0 - Fim: ')

    def main():
        op = None
        indice = 0

        while op != 0:
            op = int(input('1 - Gerar boleto, 2 - Pagar, 3 - Situação do pagamento, 0 - Fim: '))

            if op == 1:
                if indice == 1:
                    print('Você não pode gerar dois boletos.')
                else:
                    cod = input('Digite o código de barras: ')
                    emissao = input('Digite a data de emissão: ')
                    data_emissao = datetime.datetime.strptime(emissao, '%d/%m/%Y')
                    venc = input('Digite a data de vencimento: ')
                    data_venc = datetime.datetime.strptime(venc, '%d/%m/%Y')
                    valor = float(input('Digite o valor do boleto: '))

                    boleto = Boleto(cod, data_emissao, data_venc, valor)
                    print(boleto)
                    indice = 1

            if op == 2:
                if indice == 0:
                    print('Gere um boleto antes de pagar.')
                else:
                    pagamento = float(input('Digite o valor a pagar: '))
                    print(boleto.Pagar(pagamento))
                
            if op == 3:
                if indice == 0:
                    print('Gere um boleto antes de saber a situação de pagamento.')
                else:
                    print(boleto.Situacao())

UI.main()