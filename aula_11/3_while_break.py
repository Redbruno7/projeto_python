# AULA 11 - COMANDO WHILE, BREAK
# Data: 12/11/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('ESTRUTURA DE CONTROLE - WHILE - BREAK')
print('=' * 70)
print()

# Iteração de nomes digitados
print('=' * 70)
while True:
    nome = input('Digite um nome [s - Sair]: ').lower()

# Condição para quebra do loop
    if (nome != 's'):
        print('-' * 70)
        print('Continue digitando:')
        print('-' * 70)
    else:
        print('=' * 70)
        print()
        print('=' * 70)
        print('Programa encerrado!')
        print('=' * 70)
        print()
        break