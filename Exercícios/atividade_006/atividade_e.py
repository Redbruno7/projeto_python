# ATIVIDADE 006 - ATIVIDADE E
# ALUNO: BRUNO C. RODGERS
# Data: 22/11/2024
# Faça um programa que leia as vogais, depois mostre-as em ordem inversa.

import os


os.system('cls')

# Título
print('=' * 70)
print('Leitura e Inversão de Vogais')
print('=' * 70)
print()

# Entrada
vogais = ['a', 'e', 'i', 'o', 'u']

# Inversão lista
vogais_inverso = vogais[::-1]

# Saída
print('=' * 70)
print(f'Lista inicial: {vogais}')
print('-' * 70)
print(f'Lista invertida: {vogais_inverso}')
print('=' * 70)
print()