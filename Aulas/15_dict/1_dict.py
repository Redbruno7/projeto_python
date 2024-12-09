# AULA 15 - ESTRUTURA DE DADOS - DICIONÁRIO
# Data: 09/12/2024

import os


os.system('cls')

# Título
print('=' * 140)
print('DICT')
print('-' * 140)
print('Sintaxe: variavel = {"chave" : "valor"}')
print('=' * 140)
print()

# Dicionários
compras = {}
pessoas = {}
cores = {}
elementos = dict()
numeros = dict()

# Atribuição de valores
# Sintaxe: variavel['chave'] = valor
compras['id'] = 1
compras['item'] = 'Caderno'
compras['valor'] = 10.80

pessoas['id'] = '0010'
pessoas['nome'] = 'Sherlock Holmes'
pessoas['enereco'] = 'Baker Street'
pessoas['numero'] = '221B'
pessoas['cidade'] = 'Londres'
pessoas['pais'] = 'Inglaterra'

cores['red'] = 'Vermelho'
cores['green'] = 'Verde'
cores['blue'] = 'Azul'

elementos['Pb'] = 'Chumbo'
elementos['Au'] = 'Ouro'
elementos['N'] = 'Nitrogênio'

numeros[1] = 100
numeros[2] = 200
numeros[3] = 300

# Saída
print('=' * 140)
print('Saída de Dicionários:')
print('=' * 140)
print(f'Minhas compras: {compras}')
print('-' * 140)
print(f'Detetives: {pessoas}')
print('-' * 140)
print(f'Cor RGB: {cores}')
print('-' * 140)
print(f'Tabela Periódica: {elementos}')
print('-' * 140)
print(f'Listagem de números: {numeros}')
print('=' * 140)
print()