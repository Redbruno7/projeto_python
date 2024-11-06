# ATIVIDADE 004 - ATIVIDADE I
# Data: 06/11/2024
# FAÇA UM PROGRAMA QUE RECEBA O NOME COMPLETO DE UMA PESSOA E, EM SEGUIDA, MOSTRE O PRIMEIRO E O ÚLTIMO NOME.

import os


os.system('cls')

print('=' * 70)
print('VIZUALIZAÇÃO DE NOME E SOBRENOME')
print('=' * 70)

# Entrada
nome_completo = input('Digite seu nome completo: ')

# Processamento
minusculo = nome_completo.lower()
lista_1 = minusculo.split()
inversao = lista_1[::-1]
nome = lista_1[0:1]
sobrenome = inversao[0:1]

# Saída
print('.' * 70)
print(f'Nome e Sobrenome: ')
print(f'{minusculo}')
print(f'{lista_1}')
print(f'{inversao}')
print(f'{nome}')
print(f'{sobrenome}')
print('=' * 70)