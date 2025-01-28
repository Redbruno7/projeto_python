# AULA 14 - ESTRUTURA DE DADOS - SET - SYMMETRIC DIFFERENCE
# Data: 02/12/2024

import os


os.system('cls')

# Título
print('=' * 90)
print('SET - DIFERENÇA SIMÉTRICA DE SETS')
print('-' * 90)
print('Sintaxe: intersecao = set_1.symmetric_difference(set_2) ou "print(set_1 ^ set_2)"')
print('=' * 90)
print()

# Sets
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = {'Thomas', 'Rafael', 'Poliana'}
set_4 = {'Reinaldo', 'Thomas', 'Raquel'}

# Diferença dos sets
diff_simetrica_1 = set_1.symmetric_difference(set_2)
diff_simetrica_2 = set_3.symmetric_difference(set_4)


# Saída
print('=' * 90)
print(f'Set 1: {set_1}')
print('-' * 90)
print(f'Set 2: {set_2}')
print('-' * 90)
print(f'Set 3: {set_3}')
print('-' * 90)
print(f'Set 4: {set_4}')
print('=' * 90)
print()
print('=' * 90)
print(f'Diferença Simétrica 1 (Set 1 ^ Set 2): {diff_simetrica_1}')
print('-' * 90)
print(f'Diferença Simétrica 2 (Set 3 ^ Set 4): {diff_simetrica_2}')
print('=' * 90)
print()