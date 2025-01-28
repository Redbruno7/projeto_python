# AULA 14 - ESTRUTURA DE DADOS - SET - DIFFERENCE
# Data: 02/12/2024

import os


os.system('cls')

# Título
print('=' * 80)
print('SET - DIFERENÇA DE SETS')
print('-' * 80)
print('Sintaxe: intersecao = set_1.difference(set_2) ou "print(set_1 - set_2)"')
print('=' * 80)
print()

# Sets
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = {'Humberto', 'Luciana', 'Everton'}
set_4 = {'Igor', 'Everton', 'Ronaldo'}

# Diferença dos sets
diferenca_1 = set_1.difference(set_2)
diferenca_2 = set_3.difference(set_4)


# Saída
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
print(f'Diferença 1 (Set 1 - Set 2): {diferenca_1}')
print('-' * 80)
print(f'Diferença 2 (Set 3 - Set 4): {diferenca_2}')
print('=' * 80)
print()