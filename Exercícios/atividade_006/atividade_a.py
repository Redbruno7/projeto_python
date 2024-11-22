# ATIVIDADE 006 - ATIVIDADE A
# ALUNO: BRUNO C. RODGERS
# Data: 22/11/2024
# Crie a lista [1, 2, 3, 5, 6] e depois insira o valor que está faltando na posição correta.

import os


os.system('cls')

# Título
print('=' * 70)
print('Inserção de número em lista:')
print('=' * 70)
print()

# Entrada
lista = [1, 2, 3, 5, 6]
print('=' * 70)
print(f'Lista Inicial: {lista}')
print('-' * 70)

# Inserção de elemento
lista.append(4)
print(f'Elemento Acrescentado: {lista}')
print('-' * 70)

# Ordenação crescente
lista.sort()
print(f'Lista Final: {lista}')
print('=' * 70)
print()