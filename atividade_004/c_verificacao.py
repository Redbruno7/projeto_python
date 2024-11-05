# ATIVIDADE 004 - ATIVIDADE C
# Data: 05/11/2024
# FAÇA UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E VERIFIQUE SE A PALAVRA 'OLIVEIRA' ESTÁ PRESENTE NESTE NOME, MOSTRANDO TRUE OU FALSE.

import os


os.system('cls')

print('=' * 70)
print('VERIFICAÇÃO DE PRESENÇA DE NOME: "OLIVEIRA"')
print('=' * 70)

# Entrada
nome = input('Digite seu nome Completo: ')
print('.' * 70)

# Processamento e Saída
upper_case = nome.upper()
if "OLIVEIRA" in upper_case:
    print('Então quer dizer que você é do clã oculto dos Oliveiras!')
else:
    print('Não é da família Oliveira!')
print('=' * 70)