# ATIVIDADE 005 - ATIVIDADE B
# ALUNO: BRUNO C. RODGERS
# Data: 13/11/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('CONTAGEM DE NÚMEROS EM INTERVALO PROPOSTO')
print('=' * 70)
print()

# Entrada para intervalo
print('=' * 70)
inicio = int(input(f'Digite o valor inicial para contagem: '))
print('-' * 70)
fim = int(input(f'Digite o valor final para contagem: '))
print('=' * 70)
print()


# Looping de 1 a 100
print('=' * 70)
print('Contagem dos números no intervalo:')
print('=' * 70)

for i in range(inicio, fim + 1):
    print(f'{i}', end = ' | ')

print()
print('=' * 70)
print()