# ATIVIDADE 005 - ATIVIDADE H
# ALUNO: BRUNO C. RODGERS
# Data: 13/11/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('CONTAGEM DE NÚMEROS EM INTERVALO PROPOSTO COM INTERRUPÇÕES')
print('=' * 70)
print()

# Entrada para intervalo
print('=' * 70)
inicio = int(input('Digite um valor para o início do intervalo: '))
print('-' * 70)
fim = int(input('Digite um valor para o fim do intervalo: '))
print('=' * 70)
print()

# Iteração no intervalo proposto
print('=' * 70)
print('Números 3, 5 e 7 ignorados:')
print('-' * 70)
for i in range(inicio, fim + 1):

    if i == 3:
        continue
    elif i == 5:
        continue
    elif i == 7:
        continue
    else:
        print(f'{i}')
print('=' * 70)
print()