# AULA 12 - ESTRUTURA DE DADOS - LISTA / NAVEGAÇÃO
# Data: 21/11/2024

import os


os.system('cls')

print('=' * 70)
print('ESTRUTURA DE DADOS: LISTAS []')
print('=' * 70)
print()

# Entradas de listas
lista_inteiros = [1, 2, 3, 4]
lista_vogais = ['a', 'e', 'i', 'o', 'u']
lista_nomes = ['João', 'Joana', 'Carolina']
lista_heterogenea = ['João', 80, 1.90, 'AB']
lista_lista = [[1, 2, 3, 4], ['a', 'b', 'i', 'o', 'u']]

# Saídas
print('=' * 70)
print('Tipos de Lista:')
print('-' * 70)
print(f'Lista de números: {lista_inteiros}')
print(f'Lista de vogais: {lista_vogais}')
print(f'Lista de nomes: {lista_nomes}')
print(f'Lista misturada: {lista_heterogenea}')
print(f'Lista de lista: {lista_lista}')
print('=' * 70)
print()

# Varrer índices manualmente
indice_inteiros = lista_inteiros[0]
indice_vogais = lista_vogais[1]
indice_nomes = lista_nomes[2]
indice_heterogenea = lista_heterogenea[3]
indice_lista = lista_lista[1]

# Saída de varredura
print('=' * 70)
print('Acesso à elemento da lista:')
print('-' * 70)
print(f'Lista de números: {indice_inteiros}')
print(f'Lista de vogais: {indice_vogais}')
print(f'Lista de nomes: {indice_vogais}')
print(f'Lista misturada: {indice_heterogenea}')
print(f'Lista de lista: {indice_lista}')
print('=' * 70)