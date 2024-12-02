# AULA 14 - ESTRUTURA DE DADOS - SET - INTERSECTION
# Data: 02/12/2024

import os


os.system('cls')

# Título
print('=' * 80)
print('SET - INTERSEÇÃO DE SETS')
print('-' * 80)
print('Sintaxe: intersecao = set_1.intersection(set_2) ou "print(set_1 & set_2)"')
print('=' * 80)
print()

# Sets
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = {'João', 'Maria', 'Laura'}
set_4 = {'Ana', 'Laura', 'Jorge'}

# Interseção dos sets
intersecao_1 = set_1.intersection(set_2)
intersecao_2 = set_3.intersection(set_4)

# Saída Inicial
print('=' * 80)
print(f'Set 1: {set_1}')
print('-' * 80)
print(f'Set 2: {set_2}')
print('-' * 80)
print(f'Set 3: {set_3}')
print('-' * 80)
print(f'Set 4: {set_4}')
print('=' * 80)
print()
print('=' * 80)
print(f'Interseção Set 1 e Set 2: {intersecao_1}')
print('-' * 80)
print(f'Interseção Set 3 e Set 4: {intersecao_2}')
print('=' * 80)
print()