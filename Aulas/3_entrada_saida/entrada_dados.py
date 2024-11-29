# AULA 03 - ENTRADA DE DADOS
# Data: 23/10/2024

# Import
import os

# Limpar terminal
os.system('cls')

# Título
print('-' * 70)
print('ENTRADA DE DADOS EM PYTHON')
print('=' * 70)

# Entrada
nome = input('Entre com um nome: ')
nascimento = input('Data de nascimento: ')
peso = input('Entre com o peso: ')
altura = input('Entre com a altura: ')

# Saída
print('-' * 70)
print('SAÍDA DE DADOS')
print('=' * 70)
print('Nome..............: ', nome)
print('Data de nascimento: ', nascimento)
print('Peso..............: ', peso)
print('Altura............: ', altura)
print('-' * 70)
print('')