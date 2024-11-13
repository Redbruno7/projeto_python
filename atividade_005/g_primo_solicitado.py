# ATIVIDADE 005 - ATIVIDADE G
# ALUNO: BRUNO C. RODGERS
# Data: 13/11/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('NÚMEROS PRIMOS EM INTERVALO PROPOSTO')
print('=' * 70)
print()

# Entrada para intervalo
print('=' * 70)
inicio = int(input('Digite um valor para o ínicio do intervalo: '))
print('-' * 70)
fim = int(input('Digite um valor para o final do intervalo: '))
print('=' * 70)
print()

# Iteração no intervalo proposto
print('=' * 70)
for numero in range(inicio, fim + 1):

    if numero < 2:
        continue

    # Validação de número primo
    primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break
    
    if primo:
        print(f'{numero}')
print('=' * 70)