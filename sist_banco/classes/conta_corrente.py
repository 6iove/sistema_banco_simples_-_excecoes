from .conta import Conta
from .cliente import Cliente
from .transacao import Transacao
from exceptions import SaldoInsuficienteError

# herda de conta
class ContaCorrente(Conta):
    def __init__(self, numero: str, titular: Cliente, saldo: float, senha: str, limite: float):
        super().__init__(numero, titular, saldo, senha)
        self._limite = float(limite)
        self._tx_manutencao = 10.0
    
    @property
    def limite(self):
        return self._limite
        
    def sacar(self, valor: float):
        if valor <= 0:
            from exceptions import ValorInvalidoError
            raise ValorInvalidoError("Valor de saque deve ser maior que zero.")
        disponivel = self._saldo + self.limite
        if valor > disponivel:
            raise SaldoInsuficienteError("Saldo + limite insuficientes.")
        self._saldo -= valor
        # adiciona transacao especifica de conta corrente
        self.add_transacao("Saque (CC)", - valor)
        return True
