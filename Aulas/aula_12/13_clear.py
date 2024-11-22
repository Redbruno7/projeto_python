# AULA 12 - ESTRUTURA DE DADOS - LISTA / REMOÇÃO DE TODOS OS ELEMENTOS
# Data: 22/11/2024

import os


os.system('cls')

print('=' * 70)
print('LISTAS - FUNÇÃO CLEAR')
print('=' * 70)
print()

# Entrada
numeros = []
print('=' * 70)
entrada = input('Digite números separados por espaço: ')
print('-' * 70)
escolha = input('Deseja limpar a lista? (s/n): ').strip().lower()
print('=' * 70)
print()

# Conversão lista
entrada_lista = entrada.split()

# Casting valores inteiros
for i in entrada_lista:
    numeros.append(int(i))

# Condição de escolha e saída
print('=' * 70)
print(f'Lista Inicial: {numeros}')
print('-' * 70)
if escolha == 's':
    numeros.clear()
    print(f'Lista Final: {numeros}')
    print('=' * 70)
    print()
else:
    print(f'Lista Final: {numeros}')
    print('=' * 70)
    print()