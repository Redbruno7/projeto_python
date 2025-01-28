# AULA 12 - ESTRUTURA DE DADOS - LISTA / BUSCA DE PRIMEIRA OCORRÊNCIA
# Data: 21/11/2024

import os


os.system('cls')

print('=' * 70)
print('LISTAS - FUNÇÃO INDEX')
print('=' * 70)
print()

# Entrada
numeros = []
print('=' * 70)
entrada_numeros = input('Digite números separados por espaço: ')
print('-' * 70)
entrada_busca = int(input('Digite o número que deseja encontrar: '))
print('=' * 70)
print()

# Conversão em lista
lista_numeros = entrada_numeros.split()

# Casting valores inteiros
for i in lista_numeros:
    numeros.append(int(i))

# Busca por elemento
print('=' * 70)
print(f'Lista: {numeros}')
print('-' * 70)
if entrada_busca in numeros:
    indice = numeros.index(entrada_busca)
    print(f'O número {entrada_busca} está no índice {indice}.')
else:
    print(f'O número {entrada_busca} não foi encontrado na lista.')
print('=' * 70)
print()