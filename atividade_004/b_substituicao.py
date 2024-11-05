# ATIVIDADE 004 - ATIVIDADE B
# Data: 05/11/2024
# FAÇA UM PROGRAMA QUE RECEBA O NOME 'JOÃO DA SILVA' E, EM SEGUIDA, SUBSTITUA 'SILVA' POR 'OLIVEIRA'.

import os


os.system('cls')

print('=' * 70)
print('SUBSTITUIÇÃO DE NOME')
print('=' * 70)

# Entrada
nome = 'João da Silva'

# Processamento
troca = nome.replace('da Silva', 'de Oliveira')

# Saída
print(f'Nome original: {nome}.')
print(f'Nome alterado para: {troca}.')
print('=' * 70)