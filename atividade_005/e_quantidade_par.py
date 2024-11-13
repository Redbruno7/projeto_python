# ATIVIDADE 005 - ATIVIDADE E
# ALUNO: BRUNO C. RODGERS
# Data: 13/11/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('QUANTIDADE DE NÚMEROS PARES ENTRE 0 A 100')
print('=' * 70)
print()

# Contador
soma = 0

# iteração de 0 a 100
for i in range(0, 101):

    # Validação de número par
    if (i % 2 == 0):
        soma += 1

# Saída
print('=' * 70)
print(f'Quantidade de números pares no intervalo de 0 a 100: {soma}')
print('=' * 70)