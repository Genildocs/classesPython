from datetime import datetime
from random import randint
import pytz
class ContaCorrente():

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, numero, agencia, cpf, nome):
        self._numero = numero
        self._agencia = agencia
        self.cpf = cpf
        self.nome = nome
        self._saldo = 0
        self._limite = 0
        self.historico_transacoes = []
        self.cartoes = []



    def extrato(self):
        print(f'Saldo atual de {self.nome}: R$ {self._saldo:,.2f}.')
    
    def depositar(self, valor):
        self._saldo += valor
        self.historico_transacoes.append((f'Saldo atual: R$ {self._saldo:,.2f}, Deposito: R$ {valor:,.2f}, Data: {ContaCorrente._data_hora()}'))

    def _limite_conta(self):                      
        self._limite = -1000
        return self._limite

    def sacar(self, valor):
        if(self._saldo - valor < self._limite_conta()):
            print(f"Não é possivel sacar essa quantia de R$ {valor:,.2f},Saldo insuficiente.")
        else:
            self._saldo -= valor
            self.historico_transacoes.append((f'Saldo atual: R$ {self._saldo:,.2f}, Saque: R$ {valor:,.2f}, Data: {ContaCorrente._data_hora()}'))

    def historico_de_transacoes(self):
        print('Historico de transações:')
        for transacoes in self.historico_transacoes:
            print(transacoes)

class CartaoCredito():


    def __init__(self, titular, conta_corrente):
        self.numero = None
        self.titular = titular
        self.validade = '06/28'
        self.cod_seguranca = f'{randint(0,9)}{randint(0,9)}{randint(0,9)}'
        self.limite = None
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    def numero_cartao(self):
        self.numero = '4892 0200 1878 0248'
        return self.numero

    def limite_cartao(self):
        self.limite = 1500
        return self.limite

conta_Genildo = ContaCorrente(1, 883, "14061011766", "Genildo Souza")
cartao_Genildo = CartaoCredito("Genildo", conta_Genildo)
print(cartao_Genildo.cod_seguranca)



