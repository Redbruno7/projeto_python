# AULA 12 - ESTRUTURA DE DADOS - LISTA / SAÍDA COM FOR - ENUMERATE
# Data: 22/11/2024

import os


os.system('cls')

print('=' * 70)
print('LISTAS - SAÍDA COM FOR - ENUMERATE')
print('=' * 70)
print()

# Flag
soma = 0

# Entrada
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Comando "enumerate()" percorre a lista adiciona um índice para cada valor
# start opcional, para não começar no índice 0
# "enumerate(lista_numeros, start = 1)"

# Para cada NÚMERO  dentro da LISTA DE NÚMEROS, enumera com um ÍNDICE
print('=' * 70)
for indice, numero in enumerate(lista_numeros):
    soma += numero
    print(f'Índice: {indice} = Número: {numero}')
    print('-' * 70)

print(f'A soma de todos os números é: {soma}')
print('=' * 70)
print()