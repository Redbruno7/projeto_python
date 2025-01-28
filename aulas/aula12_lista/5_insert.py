# AULA 12 - ESTRUTURA DE DADOS - LISTA / INSERÇÃO DE ELEMENTOS EM POSIÇÃO DESEJADA
# Data: 21/11/2024

import os


os.system('cls')

print('=' * 70)
print('LISTAS - FUNÇÃO INSERT')
print('=' * 70)
print()

# Entrada lista
lista = [1, 2, 3, 4]

# Entrada usuário
print('=' * 70)
print(f'Lista Principal: {lista}')
print('=' * 70)
elemento = input('Elemento a ser inserido: ')
print('-' * 70)
posicao = int(input('Posição onde deseja inserir o elemento: '))
print('-' * 70)

# Validação de posição e saída
if posicao >= 0 and posicao <= len(lista):

    # Inserção de elemento
    lista.insert(posicao, elemento)
    print(f'Lista após a inserção: {lista}')
    print('=' * 70)
    print()
else:
    print(f'Posição fora do intervalo 0, {len(lista)}')
    print('=' * 70)
    print()