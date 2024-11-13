# ATIVIDADE 003 - ATIVIDADE F
# ALUNO: BRUNO C. RODGERS
# Data: 04/11/2024
# FAÇA UM PROGRAMA ONDE O USUÁRIO TENTA ADIVINHAR O NÚMERO QUE O COMPUTADOR ESTÁ ‘PENSANDO’.

import os
import random


os.system('cls')

print('=' * 70)
print('ADIVINHE O NÚMERO ENTRE 1 E 20')
print('=' * 70)

# Entrada
numero = int(input('Digite um número entre 1 e 20: '))

# Processamento e Saída
sorteado = random.randint(1, 20)
if numero == sorteado:
    print('-' * 70)
    print(f'Correto! o número escolhido foi: {sorteado}.')
else:
    print('-' * 70)
    print(f'Não foi desta vez! O número escolhido foi: {sorteado}.')
print('=' * 70)