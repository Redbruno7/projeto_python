# AULA 06 - ESTRUTURA CONDICIONAL SIMPLES
# Data: 29/10/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('Estudo de Condicional: Parte 1')
print('=' * 70)

# Entrada
numero = float(input('Digite um número: '))
resposta = ''

# Processamento de condicional
if numero % 2 == 0: # ==: operador relacional
    resposta = f'O número {numero} é par.'
else:
    resposta = f'O número {numero} é ímpar.'

# Saída
print('=' * 70)
print(resposta)
print('Fim do programa!\n') # \n: salta uma linha