# ATIVIDADE 005 - ATIVIDADE F
# ALUNO: BRUNO C. RODGERS
# Data: 13/11/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('NÚMEROS PRIMOS ENTRE 0 A 100')
print('=' * 70)
print()

# Iteração para 0 a 100
print('=' * 70)
for numero in range(0, 101):

    if numero < 2:
        continue

    # Validação de número primo
    primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break
    
    # Saída de números primos
    if primo:
        print(f'{numero}')
print('=' * 70)