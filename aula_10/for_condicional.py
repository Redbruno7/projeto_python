# AULA 10 - COMANDO FOR COM CONDICIONAL
# Data: 12/11/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('ESTRUTURA DE CONTROLE - FOR - CONDICIONAL')
print('=' * 70)
print()

# Entrada contador
soma = 0

# Iteração entre 4 números
for var_iteradora in range(0, 4):
    print('=' * 70)
    numero = int(input(f'{var_iteradora + 1}º número: '))
    print('-' * 70)

    # Verificação de par ou ímpar
    if (numero % 2 == 0):
        print(f'O número {numero} é par.')
        print('=' * 70)
        print()
    else:
        print(f'O número {numero} é ímpar.')
        print('=' * 70)
        print()