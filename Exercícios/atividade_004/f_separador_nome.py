# ATIVIDADE 004 - ATIVIDADE F
# ALUNO: BRUNO C. RODGERS
# Data: 06/11/2024
# FAÇA UM PROGRAMA QUE RECEBA O NOME COMPLETO DE UMA PESSOA E, POSTERIORMENTE, IMPRIMA ESSE NOME SEPARADAMENTE.

import os


os.system('cls')

print('=' * 70)
print('SEPARAÇÃO DE NOME COMPLETO')
print('=' * 70)

# Entrada
frase = input('Digite seu nome completo: ')

# Processamento
lista = frase.split()

# Saída
print('.' * 70)
print(f'{lista}')
print('=' * 70)