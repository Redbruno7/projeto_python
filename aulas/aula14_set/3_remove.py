# AULA 14 - ESTRUTURA DE DADOS - SET - REMOVE
# Data: 29/11/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('SET - REMOÇÃO DE ELEMENTO')
print('-' * 70)
print('Sintaxe: set.remove(elemento)')
print('=' * 70)
print()

# Set
numeros = {1, 2, 3, 4, 5}

# Saída Inicial
print('=' * 70)
print(f'Set Inicial: {numeros}')


# Remover número - (Remoção de número inexistente resulta em erro)
numeros.remove(3)

# Saída Final
print('-' * 70)
print(f'Set Final: {numeros}')
print('=' * 70)
print()