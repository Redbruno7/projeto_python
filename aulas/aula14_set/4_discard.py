# AULA 14 - ESTRUTURA DE DADOS - SET - DISCARD
# Data: 29/11/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('SET - REMOÇÃO DE ELEMENTO SE EXISTENTE')
print('-' * 70)
print('Sintaxe: set.discard(elemento)')
print('=' * 70)
print()

# Set
numeros = {10, 20, 30, 40, 50}

# Saída Inicial
print('=' * 70)
print(f'Saída Inicial: {numeros}')
print('-' * 70)

# Remoção de elemento existente
numeros.discard(30)

# Remoção de elemento inexistente - (Nada acontece)
numeros.discard(60)

# Saída Final
print(f'Saída Final: {numeros}')
print('=' * 70)
print()