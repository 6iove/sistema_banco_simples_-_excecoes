from typing import List
from .transacao import Transacao
from .cliente import Cliente
from exceptions import ValorInvalidoError, SaldoInsuficienteError

# classe base
class Conta:
    def __init__(self, numero: str, titular: Cliente, saldo: float, senha: str):
        self._numero = numero
        self._titular = titular
        self._saldo = float(saldo)
        self._senha = senha
        self._transacoes: List[Transacao] = []

    @ property
    def numero(self):
        return self._numero
    
    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo
    
    def autenticar(self, senha: str) -> bool:
        return senha == self._senha
    
    def add_transacao(self, tipo: str, valor: float):
        # adiciono uma transação na listinha (Depósito, Saque…)
        self._transacoes.append(Transacao(tipo, valor, self._saldo, self._titular))

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValorInvalidoError("Valor de depósito deve ser maior que zero.")
        # soma no saldo
        self._saldo += valor
        # salva a transacao
        self.add_transacao("Depósito", valor)

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValorInvalidoError("Valor de saque deve ser maior que zero.")
        # verifica salfo
        if valor > self._saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")
        # debita
        self._saldo -= valor
        self.add_transacao("Saque", -valor)

    def extrato(self):
        # retorna cópia da lista 
        return list(self._transacoes)

    def print_extrato(self):
        print(f"\nExtrato - Conta {self.numero} - Titular: {self.titular.nome}")
        for t in self._transacoes:
            print(t)
        print(f"Saldo atual: R$ {self._saldo:.2f}\n")
