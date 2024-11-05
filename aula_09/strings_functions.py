# AULA 09 - FATIAMENTO DE STRINGS
# Data: 05/11/2024

import os


print('=' * 70)
print('FUNÇÕES DE STRINGS')
print('=' * 70)

# Entrada
frase_1 = "Olá, Mundo!"
frase_2 = "    Olá, Mundo    "

# Contagem de caracteres
qtd_caracteres = len(frase_1)
print('Contagem de caracteres:')
print(f'A frase {frase_1} \ncontém {qtd_caracteres} caracteres')
print('.' * 70)

# Frase em minúsculo
minusculo = frase_1.lower()
print('Frase em minúsculo:')
print(f'Frase original: {frase_1}')
print(f'Frase nova: {minusculo}')
print('.' * 70)

# Frase capitalizada
maiusculo = frase_1.capitalize()
print('Frase capitalizada:')
print(f'Frase original: {frase_1}')
print(f'Frase nova: {maiusculo}')
print('.' * 70)

# Retirar espaços, antes e depois
sem_espacos = frase_2.strip()
print('Retirar espaços, antes e depois:')
print(f'Frase original: {frase_2}')
print(f'Frase nova: {sem_espacos}')
print('.' * 70)

# Trocar palavra
substituicao = frase_1.replace("Mundo", "Python")
print('Trocar palavra:')
print(f'Frase original: {frase_1}')
print(f'Frase nova: {substituicao}')
print('.' * 70)

# Separa palavras de uma str em lista
lista_1 = frase_1.split(',')
print('Separa palavras de uma str em lista:')
print(f'Frase original: {frase_1}')
print(f'Frase nova: {lista_1}')
print('.' * 70)

#  Transforma lista em string com separador
lista_2 = ['Olá', 'mundo']
juncao = '-'.join(lista_2)
print('Transforma lista em string com separador:')
print(f'Frase original: {lista_2}')
print(f'Frase nova: {juncao}')
print('=' * 70)