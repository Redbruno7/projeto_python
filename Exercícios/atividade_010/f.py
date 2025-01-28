# ALUNO: BRUNO C. RODGERS
# Data: 23/01/2025
# º Criar uma função que receba 2 listas: 
# - lista 1: nome, peso, altura 
# - lista 2: John, 40, 1.8
# º Criar um dicionário par chave e valor utilizando como base as duas listas. 
# º Imprimir esse dicionário com laço for.


import os

# Limpeza de terminal
def clear_terminal():
    os.system('cls')

# Título
def title():
    print('=' * 70)
    print('FUNÇÃO - DICIONÁRIO DO JOHN')
    print('=' * 70)
    print()

# Listas
def create_lists():
    list_1 = ['Nome', 'Peso', 'Altura']
    list_2 = ['John', '40', '1.80']

    return list_1, list_2

# Dicionário
def create_dict(list_1, list_2):
    
    john_dict = {}
    
    for i in range(len(list_1)):
        john_dict[list_1[i]] = list_2[i]
        
    return john_dict

# Invocar função
title()
list_1, list_2 = create_lists()
john_dict = create_dict(list_1, list_2)

print('=' * 70)
for key, value in john_dict.items():    
    print(f'{key}: {value}')
print('=' * 70)
print()