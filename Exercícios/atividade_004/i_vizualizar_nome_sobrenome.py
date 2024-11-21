# ATIVIDADE 004 - ATIVIDADE I
# ALUNO: BRUNO C. RODGERS
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
lista = minusculo.split()
lista_inversa = lista[::-1]
lista_chamada = lista[0:1] + lista_inversa[0:1]
chamada_capitalizada = [i.capitalize() for i in lista_chamada]
chamada_final = ' '.join(chamada_capitalizada)

# Saída
print('.' * 70)
print(f'Nome e Sobrenome: {chamada_final}')
print('=' * 70)