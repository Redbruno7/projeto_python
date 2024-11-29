# AULA 10 - COMANDO FOR COM SOMATÓRIO
# Data: 12/11/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('ESTRUTURA DE CONTROLE - FOR - SOMATÓRIO')
print('=' * 70)
print()

# Entrada contador
soma = 0

# Iteração entre 4 números
print('-' * 70)
for var_iteradora in range(0, 4):
    numero = int(input(f'Digite o {var_iteradora + 1}º número: '))
    print('-' * 70)

    # Cálculo da soma
    soma += numero # soma = soma + numero

print()
print('=' * 70)
print(f'A soma dos números é: {soma}')
print('=' * 70)
print()