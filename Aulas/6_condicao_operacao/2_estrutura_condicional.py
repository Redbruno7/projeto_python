# AULA 06 - ESTRUTURA CONDICIONAL SIMPLES E ANINHADA
# Data: 29/10/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('Estudo de Condicional (Simples)')
print('=' * 70)

# Entrada simples
a = 10
b = 5
resposta = ''

# Processamento de condicional simples
if a > b:
    resposta = f'{a} é maior que {b}.'
else:
    resposta = f'{a} não é maior que {b}'

# Saída simples
print('=' * 70)
print(resposta)

# Título
print('=' * 70)
print('Estudo de Condicional (Aninhada)')
print('=' * 70)

# Entrada aninhada
a = 5
b = 5

# Processamento de condicional aninhada
if a > b:
    resposta = f'{a} é maior que {b}.'
elif a < b:
    resposta = f'{a} não é maior que {b}'
else:
    resposta = f'Os valores são iguais: {a} = {b}'

# Saída aninhada
print('=' * 70)
print(resposta)
print('=' * 70)
print()