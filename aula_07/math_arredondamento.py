# AULA 07 - FUNÇÃO INTERNA - MATH (ARREDONDAMENTO)
# Data: 31/10/2024

import os
import math


os.system('cls')

# Título
print('=' * 70)
print('ESTUDO DA BIBLIOTECA MATEMÁTICA (MATH) - ARREDONDAMENTO')
print('=' * 70)

# Entrada
numero_decimal = float(input('Entre com um número decimal: '))

# Processamento
arredondar_acima = math.ceil(numero_decimal)
arredondar_abaixo = math.floor(numero_decimal)

# Saída
print('~' * 70)
print(f'O número {numero_decimal} arredondado para cima é: '
f'{arredondar_acima}.')
print(f'O número {numero_decimal} arredondado para baixo é: '
f'{arredondar_abaixo}.')
print('~' * 70)