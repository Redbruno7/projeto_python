# AULA 12 - ESTRUTURA DE DADOS - LISTA / CONTAGEM DE ELEMENTOS
# Data: 21/11/2024

import os


os.system('cls')

print('=' * 70)
print('LISTAS - FUNÇÃO COUNT')
print('=' * 70)
print()

# Entrada
numeros = []
print('=' * 70)
entrada_numeros = input('Digite números separados por espaços: ')
print('-' * 70)
entrada_contagem = int(input('Digite o número que deseja contar: '))
print('=' * 70)
print()

# Transformaçãoem lista
lista_inteiros = entrada_numeros.split()

# Conversão para valores inteiros
for i in lista_inteiros:
    numeros.append(int(i))

# Contagem de elemento
contagem = numeros.count(entrada_contagem)

# Saída condicional
print('=' * 70)
print(f'Lista: {numeros}')
print('-' * 70)
if contagem > 0:
    print(f'O número {entrada_contagem} aparece {contagem} vezes na lista')
else:
    print(f'O número {entrada_contagem} não aparece na lista.')
print('=' * 70)
print()