# exceptions.py
class BancoError(Exception):
    """Erro base do domínio bancário."""
    pass

# erro: valor de depósito ou saque invalido
class ValorInvalidoError(BancoError):
    pass

# erro: conta não tem saldo o suficiente
class SaldoInsuficienteError(BancoError):
    pass

# erro: conta procurada não existe
class ContaNaoEncontradaError(BancoError):
    pass

# erro: senha incorreta
class SenhaIncorretaError(BancoError):
    pass

# erro: cliente procurado não encontrado
class ClienteNaoEncontradoError(BancoError):
    pass
