# AULA 08 - BIBLIOTECA RANDOM
# Data: 31/10/2024

import os
import random


os.system('cls')

print('=' * 70)
print('BIBLIOTECA RANDOM')
print('=' * 70)

# Randomização de número entre 0 e 1
print(f'Número Aleatório entre 0 e 1')
numero_aleatorio = random.random()
print(f'O número gerado foi: {numero_aleatorio}')
print('.' * 70)

# Randomização de número inteiro no intervalo
print(f'Número  Inteiro Aleatório no Intervalo:')
aleatorio_inteiro = random.randint(1, 20)
print(f'O número inteiro gerado foi: {aleatorio_inteiro}')
print('.' * 70)

# Randomização de número decimal no intervalo
print(f'Número Decimal Aleatório entre no Intervalo:')
aleatorio_decimal = random.uniform(1, 10)
print(f'O número decimal gerado foi: {aleatorio_decimal}')
print('.' * 70)

# Sorteio em uma lista
print('Sorteio Individual em uma Lista:')
lista = ['Ágata', 'Coly', 'Isis', 'Bia']
nome_sorteado = random.choice(lista)
print(f'Lista: {lista}')
print(f'O nome escolhido foi: {nome_sorteado}')
print('.' * 70)

# Embaralhar sequência
print('Embaralhar sequência:')
lista_2 = ['Ágata', 'Coly', 'Isis', 'Bia']
print(f'Lista antiga: {lista_2}')
# Embaralhado: list(random.shuffle(lista)) - erro
# Embaralhado: random.shuffle(lista) - saída vazia
random.shuffle(lista_2)
print(f'Lista nova: {lista_2}')
print('.' * 70)

# Seleção de elementos aleatórios em um conjunto
print(f'Retorno de elementos únicos de um conjunto:')
numeros = [1, 2, 3, 4, 5, 6, 7]
amostra_aleatoria = random.sample(numeros, 5)
print(f'Retorno da amostragem: {amostra_aleatoria}')
print('=' * 70)