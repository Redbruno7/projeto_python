# AULA 12 - ESTRUTURA DE DADOS - LISTA / CRIAÇÃO DE CÓPIA RASA (SHALLOW COPY)
# Data: 22/11/2024

import os


os.system('cls')

print('=' * 70)
print('LISTAS - FUNÇÃO COPY')
print('=' * 70)
print()

# Entrada
numeros = []
print('=' * 70)
entrada = input('Digite números separados por espaço: ')
print('-' * 70)
escolha = input('Deseja criar uma cópia? (s/n): ').strip().lower()
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
    lista_copia = numeros.copy()
    print(f'Cópia da lista: {lista_copia}')
    print('=' * 70)
    print()
else:
    print('A lista não foi copiada.')