from menu import menu_principal
from banco import Banco

def main():
    meu_banco = Banco("00.000.000/0001-00", "Banco Exemplo") 
    print("Bem-vindo!")
    menu_principal(meu_banco) 
    
if __name__ == "__main__": 
        main()