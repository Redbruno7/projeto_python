# AULA 12 - ESTRUTURA DE DADOS - LISTA / SAÍDA DE LISTAS DENTRO DE LISTA
# Data: 22/11/2024

import os


os.system('cls')

print('=' * 70)
print('LISTAS - SAÍDA DE LISTAS DENTRO DE LISTA')
print('=' * 70)
print()

# Entrada
jogo_velha = [
    #   0   1   2
    ['X', 'O', 'X'], # 0
    ['X', 'X', 'O'], # 1
    ['O', 'O', 'O']  # 2
]

# Processamento Manual
print('=' * 70)
print(f'Na linha 1 e coluna 1, existe um: {jogo_velha[1][1]}')
print('-' * 70)
print(f'Na linha 0 e coluna 2, existe um: {jogo_velha[0][2]}')
print('=' * 70)
print()

# Saída
print('=' * 70)
for linha in range(0, len(jogo_velha)):
    for coluna in range(0, len(jogo_velha)):
        print(jogo_velha[linha][coluna], end = ' ')
    print()
print('=' * 70)
print()