# AULA 12 - ESTRUTURA DE DADOS - LISTA / REMOÇÃO DE PRIMEIRA OCORRÊNCIA DE ELEMENTO
# Data: 22/11/2024

import os


os.system('cls')

print('=' * 70)
print('LISTAS - FUNÇÃO REMOVE')
print('=' * 70)
print()

# Entrada
lista = [1, 2, 3, 4]

print('=' * 70)
print(f'Lista Inicial: {lista}')
print('-' * 70)
remocao = input('Digite um número para ser removido: ')
print('-' * 70)

# Condição para remoção e casting para valor inteiro
if remocao.isdigit():
    remocao = int(remocao)

# Validação elemento
if remocao in lista:
    lista.remove(remocao)
    print(f'Lista Final: {lista}')
    print('=' * 70)
    print()
else:
    print('Elemento não encontrado.')
    print('=' * 70)
    print()