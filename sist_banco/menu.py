from banco import Banco
from agencia import Agencia
from validacoes import validar_email, validar_cpf
from classes.cliente import Cliente
from classes.funcionario import Funcionario
from classes.conta_corrente import ContaCorrente
from classes.conta_poupanca import ContaPoupanca
from exceptions import (ValorInvalidoError, SaldoInsuficienteError, ContaNaoEncontradaError, SenhaIncorretaError)
import uuid
from pwinput import pwinput

# gera numero de conta
def gerar_numero():
    return str(uuid.uuid4())[:8]

def menu_principal(banco: Banco):
    while True:
        print("=== MENU ===")
        print("1 - Criar cliente e conta corrente")
        print("2 - Criar cliente e conta poupança")
        print("3 - Depositar")
        print("4 - Sacar")
        print("5 - Extrato")
        print("6 - Sair")
        escolha = input("Escolha: ").strip()

        try:
            if escolha == "1":
                criar_conta(banco, tipo="cc")
            elif escolha == "2":
                criar_conta(banco, tipo="poup")
            elif escolha == "3":
                operacao_deposito(banco)
            elif escolha == "4":
                operacao_saque(banco)
            elif escolha == "5":
                operacao_extrato(banco)
            elif escolha == "6":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
        except (ValorInvalidoError, SaldoInsuficienteError, ContaNaoEncontradaError, SenhaIncorretaError) as e:
            print(f"Erro: {e}")
        except ValueError:
            print("Entrada inválida: valor numérico esperado.")
        except Exception as e:
            print(f"Erro inesperado: {e}")

# input de infos 
def criar_conta(banco: Banco, tipo="cc"):
    nome = input("Nome do cliente: ").strip()
    
    while True: 
        cpf = input("CPF: ").strip()
        if validar_cpf(cpf):
            break 
        print("CPF inválido. Tente novamente.")
        
    while True: 
        email = input("Email: ").strip()
        if validar_email(email):
            break
        print("E-mail inválido. Tente novamente.")
    
    # senha escondida
    senha = pwinput("Senha da conta: ", mask="*")
    numero = gerar_numero()
    # cria cliente
    cliente = Cliente(numero + "-cli", cpf, nome, email)
        
        # verifica tipo de conta 
    if tipo == "cc":
        limite = float(input("Limite da conta corrente (ex: 500.0): ") or 0)
        conta = ContaCorrente(numero, cliente, 0.0, senha, limite)
    else:
        tx = float(input("Taxa de juros (ex: 0.01): ") or 0.01)
        conta = ContaPoupanca(numero, cliente, 0.0, senha, tx)
            
    # cria agencia se não tiver 
    if not banco.listar_agencias():
        funcionario_padrao = Funcionario("1-func", "000.000.000-00", "Funcionario Sede", "ABC123")
        ag = Agencia(1, "Sede", "0000-0000", funcionario_padrao)
        banco.adicionar_agencia(ag)
            
    agencia = banco.listar_agencias()[0]
    # salva conta
    agencia.adicionar_conta(conta)
    print(f"Conta criada. Número: {conta.numero}")

# procura em todas as agencias
def localizar_conta_global(banco: Banco, numero: str):
    for ag in banco.listar_agencias():
        try:
            return ag.buscar_conta(numero)
        except:
            continue
    raise ContaNaoEncontradaError(f"Conta {numero} não encontrada no banco.")

def pedir_numero_e_senha():
    numero = input("Número da conta: ").strip()
    senha = input("Senha: ").strip()
    return numero, senha

def operacao_deposito(banco: Banco):
    numero = input("Número da conta: ").strip()
    valor = float(input("Valor para depositar: ").strip())
    conta = localizar_conta_global(banco, numero)
    conta.depositar(valor)
    print("Depósito realizado com sucesso.")

def operacao_saque(banco: Banco):
    numero, senha = pedir_numero_e_senha()
    valor = float(input("Valor para sacar: ").strip())
    conta = localizar_conta_global(banco, numero)
    if not conta.autenticar(senha):
        raise SenhaIncorretaError("Senha incorreta.")
    conta.sacar(valor)
    print("Saque realizado com sucesso.")

def operacao_extrato(banco: Banco):
    numero, senha = pedir_numero_e_senha()
    conta = localizar_conta_global(banco, numero)
    if not conta.autenticar(senha):
        raise SenhaIncorretaError("Senha incorreta.")
    conta.print_extrato()
