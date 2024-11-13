# ATIVIDADE 005 - ATIVIDADE J
# ALUNO: BRUNO C. RODGERS
# Data: 13/11/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('NÚMEROS ÍMPARES ENTRE 1 E 100 - QUANTIDADE - SOMA')
print('=' * 70)
print()

# Contador
quantidade = 0
soma = 0

# Iteração entre 1 e 100
for i in range(1, 101):

    # Validação ímpar
    if i % 2 == 0:
        continue

    # Quantidade ímpares
    quantidade += 1
    
    # Soma ímpares
    soma += i

# Saída
print('=' * 70)
print(f'Quantidade de números ímpares no intervalo de 1 a 100: {quantidade}')
print('-' * 70)
print(f'Somatório dos números ímpares no intervalo de 1 a 100: {soma}')
print('=' * 70)
print()
