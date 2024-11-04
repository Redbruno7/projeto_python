# ATIVIDADE 003 - ATIVIDADE C
# Data: 04/11/2024
# FAÇA UM PROGRAMA QUE RECEBA AS INFORMAÇÕES DE BASE E EXPOENTE. CALCULE A POTÊNCIA.


import os
import math


os.system('cls')

print('=' * 70)
print('CÁLCULO DE POTÊNCIA')
print('=' * 70)

# Entrada de dados
base = float(input('Insira um valor de base: '))
expoente = float(input('Insira um valor de expoente: '))

# Processamento
potencia = math.pow(base, expoente)

# Saída
print(f'O número {base} elevado a {expoente} é igual a: {potencia}')
print('=' * 70)