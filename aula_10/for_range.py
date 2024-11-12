# AULA 10 - COMANDO FOR, RANGE
# Data: 12/11/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('ESTRUTURA DE CONTROLE ')
print('=' * 70)
print()

# Iteração entre 6 números sem variáveis para range
print('=' * 70)
print('Iteração entre 6 números')
print('-' * 70)

for var_iteradora in range(1, 7):
    # end = '': Coloca os elementos na mesma linha
    print(f'Valor: {var_iteradora}', end = ' | ')
print()
print('=' * 70)
print()

# Iteração com as variáveis propostas
inicio = 1
fim = 7
passo = 2

print('=' * 70)
print('Iteração entre 6 números com passo 2')
print('-' * 70)

for var_iteradora in range (inicio, fim, passo):
    print(f'Valor: {var_iteradora}', end = ' | ')
print()
print('=' * 70)
print()

# Iteração entre 4 cores com "input()"
print('=' * 70)
print('Iteração entre cores fornecidas pelo usuário')
print('-' * 70)

for var_iteradora in range(1,5):
    cor = str(input(f'Digite a {var_iteradora}ª cor: '))
print('=' * 70)
print()