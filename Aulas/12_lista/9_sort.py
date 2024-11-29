# AULA 12 - ESTRUTURA DE DADOS - LISTA / ORDENAÇÃO CRESCENTE OU DECRESCENTE DOS ELEMENTOS
# Data: 22/11/2024

import os


os.system('cls')

print('=' * 80)
print('LISTAS - FUNÇÃO SORT')
print('=' * 80)
print()

# Entrada
numeros = []
print('=' * 80)
entrada = input('Digite números separados por espaço: ')
print('-' * 80)
ordem = input(
    'Digite "asc" para ordem crescente ou'
    '"desc" para ordem decrescente: ').strip().lower()
print('=' * 80)
print()

# Conversão lista
entrada_lista = entrada.split()

# Casting valores inteiros
for i in entrada_lista:
    numeros.append(int(i))

# Condição de escolha e saída
print('=' * 80)
print(f'Lista Principal: {numeros}')
print('-' * 80)
if ordem == 'asc':
    numeros.sort()
    print(f'Lista Crescente: {numeros}')
    print('=' * 80)
    print()
elif ordem == 'desc':
    numeros.sort(reverse = True)
    print(f'Lista Decrescente: {numeros}')
    print('=' * 80)
    print()
else:
    print('Oção inválida.')
    print('=' * 80)
    print()