# AULA 05 - ATIVIDADE H
# IMPLEMENTE UM PROGRAMA QUE RECEBA UM NÚMERO INTEIRO E IMPRIMA SUA TABUADA DE MULTIPLICAÇÃO.
# Data: 25/10/2024

# Importar bibliotecas
import os

# Limpar terminal
os.system('cls')

# Título
print('=' * 70)
print('INSIRA UM VALOR PARA REALIZAÇÃO DE SUA TABUADA')
print('=' * 70)

# Entrada
numero = int(input('Digite um número inteiro: '))

# Processamento
nx0 = numero * 0
nx1 = numero * 1
nx2 = numero * 2
nx3 = numero * 3
nx4 = numero * 4
nx5 = numero * 5
nx6 = numero * 6
nx7 = numero * 7
nx8 = numero * 8
nx9 = numero * 9

# Saída
print('=' * 70)
print('TABUADA DO NÚMERO FORNECIDO')
print('-' * 70)
print(f'° {numero} * 0 = {nx0}')
print(f'° {numero} * 1 = {nx1}')
print(f'° {numero} * 2 = {nx2}')
print(f'° {numero} * 3 = {nx3}')
print(f'° {numero} * 4 = {nx4}')
print(f'° {numero} * 5 = {nx5}')
print(f'° {numero} * 6 = {nx6}')
print(f'° {numero} * 7 = {nx7}')
print(f'° {numero} * 8 = {nx8}')
print(f'° {numero} * 9 = {nx9}')
print('=' * 70)