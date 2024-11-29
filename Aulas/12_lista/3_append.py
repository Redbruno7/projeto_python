# AULA 12 - ESTRUTURA DE DADOS - LISTA / ADIÇÃO DE ELEMENTO
# Data: 21/11/2024

import os


os.system('cls')

print('=' * 70)
print('LISTAS - FUNÇÃO APPEND')
print('=' * 70)
print()

# Entrada para lista vazia
lista_numeros = []

# Looping 3 números
print('=' * 70)
for i in range(1, 4):
    numero = int(input(f'Digite o {i}º número: '))

    # Inserção de valor à lista
    lista_numeros.append(numero)

# Saída
print('-' * 70)
print(f'Lista gerada: {lista_numeros}')
print('=' * 70)
print()

# Verificação de elemento inserido na lista
print('=' * 70)
verificacao = int(input('Digite um valor para busca: '))
print('-' * 70)

if verificacao in lista_numeros:
    print(f'O número {verificacao} está na lista.')
else:
    print(f'O número {verificacao} não está na lista.')

print('=' * 70)
print()