# AULA 12 - ESTRUTURA DE DADOS - LISTA / FATIAMENTO
# Data: 21/11/2024

import os


os.system('cls')

print('=' * 80)
print('FATIAMENTO DE LISTAS')
print('=' * 80)
print()

# Entrada lista
lista_mista = ['a', 'b', 3, 'João', 'e', 500, 'g','h']

# Processamento para fatiamento

# 1º elemento
fatia_1 = lista_mista[0]

# Todos os elementos
fatia_2 = lista_mista[0:]

# Elementos de índice 0 até o índice 5
fatia_3 = lista_mista[0:6]

# Elementos de índice 0 até o índice 5 com passo 2
fatia_4 = lista_mista[0:6:2]

# Todos os elementos da direita para a esquerda
fatia_5 = lista_mista[::-1]

print('=' * 80)
print('Tipos de fatiamento:')
print('-' * 80)
print(f'Fatia de 1º elemento: {fatia_1}')
print(f'Fatia de todos os elementos: {fatia_2}')
print(f'Fatia de parte dos elementos: {fatia_3}')
print(f'Fatia de parte dos elementos com passo: {fatia_4}')
print(f'Fatia inversa de todos os elementos: {fatia_5}')
print('=' * 80)
print()