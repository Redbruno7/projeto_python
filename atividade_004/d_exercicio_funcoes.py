# ATIVIDADE 004 - ATIVIDADE D
# Data: 05/11/2024
# FAÇA UM PROGRAMA QUE LEIA UMA FRASE E DEPOIS EXIBA NA TELA:
# A FRASE EM MINÚSCULAS, A FRASE EM MAIÚSCULAS, A QUANTIDADE DE CARACTERES NA FRASE E QUANTAS LETRAS TEM A 2ª PALAVRA NA FRASE.

import os


os.system('cls')

print('=' * 70)
print('MUDANÇA ESTRUTURAL E INFORMAÇÕES')
print('=' * 70)

# Entrada
frase = input('Digite a frase: ')

# Processamento
minusculo = frase.lower()
maiusculo = frase.upper()
qtd_carac = len(frase) # Contagem de caracteres
lista = frase.split() # Divisão da frase em lista
segunda_palavra = lista[1:2]
palavra_2 = ''.join(segunda_palavra)
qtd_caract_2 = len(palavra_2)

# Saída
print('.' * 70)
print(f'Frase em minúsculo: {minusculo}')
print(f'Frase e maiúsculo: {maiusculo}')
print(f'Quatidade de caracteres da frase: {qtd_carac}')
print(f'Quantidade de caracteres da segunda palavra: {qtd_caract_2}')
print('=' * 70)