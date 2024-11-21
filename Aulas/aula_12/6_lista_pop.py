# AULA 12 - ESTRUTURA DE DADOS - LISTA / RECORTE DE ELEMENTO
# Data: 21/11/2024

import os


os.system('cls')

print('=' * 70)
print('LISTAS - FUNÇÃO POP')
print('=' * 70)
print()

# Entrada lista
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Entrada usuário
print('=' * 70)
print(f'Lista Principal: {lista}')
print('=' * 70)
indice = int(input('Digite o índice do elemento a ser removido (0-9): '))
print('-' * 70)

# Validação índice
if 0 <= indice < len(lista):

    # Remoção do elemento
    remocao = lista.pop(indice)
    print(f'Elemento removido: {remocao}')
    print('-' * 70)
else:
    print('Índice inválido.')
    print('=' * 70)

# Saída
print(f'Lista Final: {lista}')
print('=' * 70)
print()