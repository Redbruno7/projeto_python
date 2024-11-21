# ATIVIDADE 004 - ATIVIDADE E
# ALUNO: BRUNO C. RODGERS
# Data: 06/11/2024
# FAÇA UM PROGRAMA QUE RECEBA UMA FRASE E, EM SEGUIDA, MOSTRE QUANTAS VEZES AS VOGAIS FORAM UTILIZADAS.

import os


os.system('cls')

print('=' * 70)
print('CONTAGEM DE VOGAIS')
print('=' * 70)

# Entrada
frase = input('Digite uma frase sem acentuação: ')

# Processamento
minusculo = frase.lower()
qtd_a = minusculo.count('a')
qtd_e = minusculo.count('e')
qtd_i = minusculo.count('i')
qtd_o = minusculo.count('o')
qtd_u = minusculo.count('u')
qtd_vogais = qtd_a + qtd_e + qtd_i + qtd_o + qtd_u

# Saída
print('.'*70)
print(f'Quantidade de aplicações:')
print(f'Vogal "A"......: {qtd_a}')
print(f'Vogal "E"......: {qtd_e}')
print(f'Vogal "I"......: {qtd_i}')
print(f'Vogal "O"......: {qtd_o}')
print(f'Vogal "U"......: {qtd_u}')
print(f'Total de vogais: {qtd_vogais}')
print('='*70)