# ATIVIDADE 004 - ATIVIDADE H
# ALUNO: BRUNO C. RODGERS
# Data: 06/11/2024
# FAÇA UM PROGRAMA QUE LEIA O NOME DE UM ALUNO E MOSTRE QUANTAS VEZES A LETRA 'O' APARECE E EM QUE POSIÇÃO ELA APARECE PELA PRIMEIRA E ÚLTIMA VEZ.

import os


os.system('cls')

print('=' * 70)
print('IDENTIFICAÇÃO E LOCALIZAÇÃO DE LETRA "O"')
print('=' * 70)

# Entrada
nome = input('Digite o nome do aluno: ').strip()

# Processamento e saída
print('.'*70)
minusculo = nome.lower()

if 'o' not in minusculo:
    print('O nome do aluno não possui a letra "o".')
else:
    
    qtd_o = minusculo.count('o')
    primeiro_o = minusculo.find('o')
    ultimo_o = minusculo.rfind('o')
    print(f'Quantidade letra "o": {qtd_o}')
    print(f'Posição da primeira aparição: {primeiro_o}')
    print(f'Posição da última aparição: {ultimo_o}')
print('='*70)