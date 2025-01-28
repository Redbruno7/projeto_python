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
def lists():
    list_1 = ['Nome', 'Peso', 'Altura']
    list_2 = ['John', '40', '1.80']

    return list_1, list_2

# Invocar função
title()

print('=' * 70)
list_1, list_2 = lists()



print(f'{list_1}')
print('=' * 70)
print()