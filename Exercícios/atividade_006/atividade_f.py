# ATIVIDADE 006 - ATIVIDADE F
# ALUNO: BRUNO C. RODGERS
# Data: 22/11/2024
# Faça um programa que leia 5 nomes, depois imprima estes nomes com seus respectivos índices.

import os


os.system('cls')

# Título
print('=' * 70)
print('Posicionamento Nominal:')
print('=' * 70)
print()

# Entrada
lista_nomes = []

# Iteração 5 nomes
print('-' * 70)
for i in range(1, 6):
    nome = input(f'Digite o {i}º nome: ')
    print('-' * 70)

    # Inserção lista
    lista_nomes.append(nome)
print()

# Enumeração índice
print('=' * 70)
for indice, nome in enumerate(lista_nomes):
    print(f'Índice: {indice} | Nome: {nome}')
print('=' * 70)
print()