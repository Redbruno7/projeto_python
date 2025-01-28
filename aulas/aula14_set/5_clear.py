# AULA 14 - ESTRUTURA DE DADOS - SET - CLEAR
# Data: 29/11/2024

import os


os.system('cls')

# Título
print('=' * 80)
print('SET - REMOÇÃO DE TODOS OS ELEMENTOS')
print('-' * 80)
print('Sintaxe: set.clear()')
print('=' * 80)
print()

# Set
frutas = {'Goiaba', 'Hesperídio', 'Ingá', 'Jabuticaba', 'Laranja'}

# Saída Inicial
print('=' * 80)
print(f'Saída Inicial: {frutas}')
print('-' * 80)

# Remoção de todos as frutas
frutas.clear()

# Saída Final
print(f'Saída Final: {frutas}')
print('=' * 80)
print()