# ATIVIDADE 005 - ATIVIDADE I
# ALUNO: BRUNO C. RODGERS
# Data: 13/11/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('SAÍDA DE LOOPING')
print('=' * 70)
print()

# Entrada do looping
print('=' * 70)
while True:
    letra = input('Digite uma letra qualquer [f - SAIR]: ').lower()
    print('-' * 70)

    # Condição para saída
    if letra == 'f':
        print('Programa encerrado!')
        print('=' * 70)
        break
print()