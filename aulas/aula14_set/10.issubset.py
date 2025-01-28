# AULA 14 - ESTRUTURA DE DADOS - SET - ISSUBSET
# Data: 02/12/2024

import os


os.system('cls')

# Título
print('=' * 60)
print('SET - SUBCONJUNTO DE SET')
print('-' * 60)
print('Sintaxe: subset = set_1.issubset(set_2)')
print('=' * 60)
print()

# Sets
set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4, 5}
set_3 = {'Thiago', 'Eduarda', 'Carolina'}
set_4 = {'Laura', 'Bruno', 'Thiago', 'Carolina', 'Eduarda'}

# Diferença dos sets
subset_1 = set_1.issubset(set_2)
subset_2 = set_2.issubset(set_1)
subset_3 = set_3.issubset(set_4)
subset_4 = set_4.issubset(set_3)


# Saída
print('=' * 60)
print(f'Set 1: {set_1}')
print('-' * 60)
print(f'Set 2: {set_2}')
print('-' * 60)
print(f'Set 3: {set_3}')
print('-' * 60)
print(f'Set 4: {set_4}')
print('=' * 60)
print()
print('=' * 60)
print(f'Set 1 é subset do Set 2? {subset_1}')
print('-' * 60)
print(f'Set 2 é subset do Set 1? {subset_2}')
print('-' * 60)
print(f'Set 3 é subset do Set 4?: {subset_3}')
print('-' * 60)
print(f'Set 4 é subset do Set 3? {subset_4}')
print('=' * 60)
print()