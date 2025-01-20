# AULA 16 - FUNÇÕES EM PYTHON - PARÂMENTROS OPCIONAL OU DEFAULT
# Data: 20/01/2024

import os

# Definir função "def x(a, b = 1)"
def multiplicar(a, b = 1):
    return a * b


os.system('cls')

# Título
print('=' * 80)
print('Multiplicar valor a * b')
print('-' * 80)
print('Operação 1: a = 5, b = 1')
print('-' * 80)
print('Operação 2: a = 5, b = 2')
print('=' * 80)
print()

# Multiplicar função com valor padrão "y = x(a)"
result_1 = multiplicar(5)

# Multiplicar função com valor definido "y = x(a, b)"
result_2 = multiplicar(5, 2)

# Saída
print('=' * 80)
print(f'Primeiro resultado: {result_1}')
print('-' * 80)
print(f'Segundo resultado: {result_2}')
print('=' * 80)
print()