# AULA 12 - ESTRUTURA DE DADOS - LISTA / SAÍDA COM IN E NOT IN
# Data: 22/11/2024

import os


os.system('cls')

print('=' * 70)
print('LISTAS - SAÍDA COM IN E NOT IN')
print('=' * 70)
print()

# In - Entrada
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# In - Condição e Saída
print('=' * 70)
if 3 in lista_numeros:
    print(f'Lista Inicial: {lista_numeros}')
    print('-' * 70)
    posicao = lista_numeros.index(3)
    print(f'O número 3 está no índice {posicao}')
else:
    print('O elemento não está na lista.')
print('=' * 70)
print()

# Not in - Entrada
lista_nomes = ['João', 'Joana', 'Carolina']

# Not in - Condição e Saída
print('=' * 70)
if 'Maria' not in lista_nomes:
    print(f'Lista Inicial: {lista_nomes}')
    print('-' * 70)
    
    # Acrescentar caso não esteja
    lista_nomes.append('Maria')
    print('O nome "Maria" foi acrescentado.')
    print('-' * 70)
    print(f'Lista Final: {lista_nomes}')
print('=' * 70)
print()