# AULA 11 - COMANDO WHILE, ELSE, CONTINUE
# Data: 12/11/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('ESTRUTURA DE CONTROLE - WHILE - ELSE - CONTINUE')
print('=' * 70)
print()

# Flag
contador = 0

# Iteração entre 1 a 10
print('=' * 70)
print('Contagem de números ímpares de 1 a 10:')
print('=' * 70)
while contador <= 10:
    contador += 1

    # Condição para contador ser ímpar
    if (contador % 2 == 0):
        continue
    print(f'Contador = {contador}')
else:
    print('-' * 70)
    print(f'Bloco While / Else finalizado em {contador}.')
print('=' * 70)
teste