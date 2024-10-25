# AULA 05 - ATIVIDADE B
# CRIE UM PROGRAMA QUE PERGUNTE O ANO DE NASCIMENTO DO USUÁRIO E CALCULE SUA IDADE ATUAL.
# Data: 25/10/2024

# Importar bibliotecas
import os
import datetime

# Limpar terminal
os.system('cls')

# Título
print('=' * 70)
print('CÁLCULO DE IDADE')
print('=' * 70)

# Entrada
nascimento = int(input('Informe o ano de seu nascimento: '))

# Processamento
ano_atual = datetime.datetime.now().year
idade = ano_atual - nascimento

# Saída
print('=' * 70)
print(f'Você tem ou irá fazer {idade} anos!')
print('=' * 70)