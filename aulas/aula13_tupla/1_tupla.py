# AULA 13 - ESTRUTURA DE DADOS - TUPLA
# Data: 29/11/2024

import os


os.system('cls')

print('=' * 70)
print('TUPLA ()')
print('=' * 70)
print()

# Lista
lista_nomes = ['Ágata', 'Bia', 'Coliana', 'Isis']

# Saída enumerada
for indice, nome in enumerate(lista_nomes):
    
    # Tupla
    tupla_nomes = (indice, nome)

    # Acessos ao índice e ao nome com tupla
    print('-' * 70)
    print(f'O nome {tupla_nomes[1]}, posição {tupla_nomes[0]} da lista.')

    # Acessos ao índice e ao nome com enumerate
    print(f'O nome {nome}, posição {indice} da lista.')
    print('-' * 70)
    print()