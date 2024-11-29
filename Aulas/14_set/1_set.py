# AULA 14 - ESTRUTURA DE DADOS - SET
# Data: 29/11/2024

import os


os.system('cls')

# Título
print('=' * 90)
print('SET')
print('-' * 90)
print('Sintaxe: variavel = {elementos} | '
      'variavel = set([elementos]) | variavel = set(lista)')
print('=' * 90)
print()

# Listas
lista_1 = ['João', 'Maria', 'Ana']
lista_2 = ['Carlos', 'Eduardo', 'Joaquim']

# Conversão set
set_1 = set(lista_1)
set_2 = set(lista_2)

# Saída
print('=' * 90)
print(f'Conjuntos Setados:')
print('-' * 90)
print(f'{set_1}')
print('-' * 90)
print(f'{set_2}')
print('=' * 90)
print()