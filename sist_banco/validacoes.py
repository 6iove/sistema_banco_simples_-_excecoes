import re

def validar_cpf(cpf: str) -> bool:
    cpf = re.sub(r"\D", "", cpf) # limpa tudo que nao é numero
    
    if len(cpf) != 11:
        return False
    return True 

def validar_email(email):
    return "@" in email