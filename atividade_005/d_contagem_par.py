# ATIVIDADE 005 - ATIVIDADE D
# ALUNO: BRUNO C. RODGERS
# Data: 13/11/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('CONTAGEM DE NÚMEROS PARES ENTRE 0 A 100')
print('=' * 70)
print()

# Iteração de 0 a 100
print('=' * 70)
for i in range (0, 101):

    # Validação de número par
    if (i % 2 == 0):
        print(f'Número: {i}')
print('=' * 70)
print()