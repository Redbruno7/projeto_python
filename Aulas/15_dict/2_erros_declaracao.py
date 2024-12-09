# AULA 15 - ESTRUTURA DE DADOS - DICIONÁRIO - ERROS DE DECLARAÇÃO
# Data: 09/12/2024

import os


os.system('cls')

# Título
print('=' * 80)
print('DICT - ERROS')
print('-' * 80)
print('Sintaxe: variavel = {"chave" : "valor"}')
print('=' * 80)
print()

# Índices iguais: só irá exibir o último item.
dict_1 = {'nome' : 'João', 'nome' : 'Joana'}

# Possibilidade de tupla como índice e lista como valor. 
# Sintaxe: dict = {tupla : lista} | dict = {() : []}
dict_2 = {(1, 2) : [1, 2]}

# Impossibilidade do inverso
# Sintaxe: dict = {lista : tupla} | dict = {[] : ()}

# Saída
print('=' * 80)
print('Saída com erros de declaração:')
print('=' * 80)
print(f'Índices iguais: {dict_1}')
print('-' * 80)
print(f'Somente "(tupla) : [lista]": {dict_2}')
print('=' * 80)
print()