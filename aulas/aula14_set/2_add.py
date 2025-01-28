# AULA 14 - ESTRUTURA DE DADOS - SET - ADD
# Data: 29/11/2024

import os


os.system('cls')

# Título
print('=' * 90)
print('SET - ADIÇÃO DE ELEMENTO')
print('-' * 70)
print('Sintaxe: set.add(elemento)')
print('=' * 90)
print()

# Set
frutas = {'Abacaxi', 'Banana', 'Caqui', 'Damasco', 'Esfregadinha'}

# Saída Inicial
print('=' * 90)
print(f'Set Inicial: {frutas}')

# Adicionar fruta
frutas.add('Framboesa')

# Adicionar fruta já existente
frutas.add('Abacaxi')

# Saída Final
print('-' * 90)
print(f'Set Final: {frutas}')
print('=' * 90)
print()