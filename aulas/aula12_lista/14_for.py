# AULA 12 - ESTRUTURA DE DADOS - LISTA / SAÍDA COM FOR
# Data: 22/11/2024

import os


os.system('cls')

print('=' * 70)
print('LISTAS - SAÍDA COM FOR')
print('=' * 70)
print()

# Entrada
lista_alunos = []

# Iteração 6 alunos
print('-' * 70)
for i in range(0, 6):
    nome = input('Digite o nome do aluno: ')
    print('-' * 70)
    lista_alunos.append(nome)
print()

# Saída
print('=' * 70)
print('Alunos:')
print('-' * 70)
for aluno in range(len(lista_alunos)):
    print(lista_alunos[aluno], end = ' ')

    # Quebrar linha no índice
    if aluno == 2:
        print()
print()
print('=' * 70)
print()