# AULA 12 - ESTRUTURA DE DADOS - LISTA / INVERSÃO DA ORDEM DOS ELEMENTOS
# Data: 22/11/2024

import os


os.system('cls')

print('=' * 70)
print('LISTAS - FUNÇÃO REVERSE')
print('=' * 70)
print()

# Entrada
numeros = []
print('=' * 70)
entrada = input('Digite números separados por espaço: ')
print('-' * 70)
escolha = input('Deseja inverter a ordem da lista? (s/n): ')
print('=' * 70)
print()

# Conversão lista
entrada_lista = entrada.split()

# Casting valores inteiros
for i in entrada_lista:
    numeros.append(int(i))

# Condição inversão e saída
print('=' * 70)
print(f'Lista inicial: {numeros}')
print('-' * 70)
if escolha == 's':
    numeros.reverse()
    print(f'Lista invertida: {numeros}')
    print('=' * 70)
    print()
else:
    print('A lista não foi invertida.')
    print('=' * 70)
    print()