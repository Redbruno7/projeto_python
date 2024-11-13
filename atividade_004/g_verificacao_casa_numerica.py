# ATIVIDADE 004 - ATIVIDADE G
# ALUNO: BRUNO C. RODGERS
# Data: 06/11/2024
# FAÇA UM PROGRAMA QUE RECEBA UM NÚMERO INTEIRO E MOSTRE NA TELA: 
# A QUANTIDADE DE UNIDADES, A QUANTIDADE DE DEZENAS, A QUANTIDADE DE CENTENAS E A QUANTIDADE DE MILHARES.

import os


os.system('cls')

print('=' * 70)
print('VERIFICAÇÃO DE CASAS DE UM NÚMERO INTEIRO')
print('=' * 70)

# Entrada
numero = int(input('Digite um número inteiro: '))

# Processamento
if (numero > 9999) or (numero < 0):
    print(f'Número inválido! Insira um número positivo com até 4 caracteres.')
else:
    milhar = numero // 1000
    centena = (numero % 1000) // 100
    dezena = (numero % 100) // 10
    unidade = (numero % 10) // 1
    print('.'*70)
    print(f'Milhar: {milhar}')
    print(f'Centena: {centena}')
    print(f'Dezena: {dezena}')
    print(f'Unidade: {unidade}')
print('=' * 70)