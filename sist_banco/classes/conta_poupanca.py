from datetime import datetime
from .conta import Conta
from exceptions import SaldoInsuficienteError

# herda de conta
class ContaPoupanca(Conta):
    def __init__(self, numero: str, titular, saldo: float, senha: str, tx_juros: float):
        super().__init__(numero, titular, saldo, senha)
        self._tx_juros = float(tx_juros)
        self._aniversario = datetime.now().day
        
        @property
        def tx_juros(self):
            return self._tx_juros
        
        @property
        def numero(self):
            return self._numero

    def sacar(self, valor: float):
        if valor <= 0:
            from exceptions import ValorInvalidoError
            raise ValorInvalidoError("Valor de saque deve ser maior que zero.")
        if valor > self._saldo:
            raise SaldoInsuficienteError("Saldo insuficiente na poupança.")
        self._saldo -= valor
        self.add_transacao("Saque (Poup)", -valor)

    def render_juros(self):
        rendimento = self._saldo * self.tx_juros
        self._saldo += rendimento
        self.add_transacao("Rendimento", rendimento)
        
    
