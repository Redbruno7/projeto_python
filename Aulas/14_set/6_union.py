# AULA 14 - ESTRUTURA DE DADOS - SET - UNION
# Data: 29/11/2024

import os


os.system('cls')

# Título
print('=' * 90)
print('SET - UNIÃO DE SETS')
print('-' * 90)
print('Sintaxe: uniao = set_1.union(set_2) ou "print(set_1 | set_2)"')
print('=' * 90)
print()

# Sets
set_1 = {1, 2, 3, 4, 5}
set_2 = {6, 7, 8, 9, 10}
set_3 = {'Ana', 'Bruno', 'Carla', 'Daniel', 'Eduarda'}
set_4 = {'Ana', 'Carla', 'Eduarda', 'Fernando', 'Guilherme'}

# Saída inicial
print('=' * 90)
print(f'Set 1 Inicial: {set_1}')
print('-' * 90)
print(f'Set 2 Inicial: {set_2}')
print('-' * 90)
print(f'Set 3 Inicial: {set_3}')
print('-' * 90)
print(f'Set 4 Inicial: {set_4}')
print('=' * 90)
print()

# União dos sets
uniao_1 = set_1.union(set_2)

# União de sets com elementos comuns
uniao_2 = set_3.union(set_4)

# Saída Final
print('=' * 90)
print(f'Saída Final 1: {uniao_1}')
print('-' * 90)
print(f'Saída Final 2: {uniao_2}')
print('=' * 90)
print()