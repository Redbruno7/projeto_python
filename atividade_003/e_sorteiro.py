# ATIVIDADE 003 - ATIVIDADE E
# ALUNO: BRUNO C. RODGERS
# Data: 04/11/2024
# FAÇA UM PROGRAMA PARA SORTEAR UM NÚMERO DE 1 A 20.

import os
import random


os.system('cls')

print('=' * 70)
print('SORTEIO NUMÉRICO DE 1 A 20')
print('=' * 70)

# Processamento e Saída
numero = random.randint(1, 20)
print(f'O número aleatório gerado é: {numero}.')
print('=' * 70)